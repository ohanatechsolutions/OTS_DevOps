#!/usr/bin/env python3
"""Install the OTS universal security caller into an owned GitHub repository via PR."""
import argparse
import base64
import json
import os
import re
import subprocess
import sys

OWNER = "ohanatechsolutions"
HUB = "OTS_DevOps"
PATH = ".github/workflows/ots-universal-security.yml"
BASELINE = "b50882793af0a1e01a8c193b2b6317b94ffa0b6f"
PRECOMMIT_PATH = ".pre-commit-config.yaml"


def precommit_config():
    return ("# OTS local secret detection. Enable on each developer machine with:\n"
            "#   python -m pip install pre-commit\n"
            "#   pre-commit install\n"
            "# Requires Go for installation of the upstream Gitleaks hook.\n"
            "repos:\n"
            "  - repo: https://github.com/gitleaks/gitleaks\n"
            "    rev: v8.30.1\n"
            "    hooks:\n"
            "      - id: gitleaks\n")


def gh(method, endpoint, payload=None, allow_404=False):
    cmd = ["gh", "api", "--method", method, endpoint]
    if payload is not None:
        cmd += ["--input", "-"]
    proc = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                          text=True, capture_output=True, check=False)
    if proc.returncode:
        if allow_404 and "HTTP 404" in proc.stderr:
            return None
        raise RuntimeError(f"GitHub API {method} {endpoint}: {proc.stderr.strip()}")
    return json.loads(proc.stdout) if proc.stdout.strip() else {}


def caller():
    return f"""name: OTS Universal Security
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '17 16 * * 1'
  workflow_dispatch:
permissions:
  contents: read
jobs:
  universal-security:
    name: Universal security baseline
    uses: {OWNER}/{HUB}/.github/workflows/security-baseline.yml@{BASELINE}
    permissions:
      contents: read
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True, help="Target owner/repo")
    args = parser.parse_args()
    if not os.getenv("GH_TOKEN"):
        parser.error("GH_TOKEN is required (repository-scoped installation token)")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("Repository must be owner/name")
    owner, name = args.repository.split("/")
    if owner.lower() != OWNER.lower():
        parser.error("Only repositories owned by ohanatechsolutions are supported")
    if name.lower() == HUB.lower():
        parser.error("The central repository already calls its baseline locally")

    repo = gh("GET", f"repos/{owner}/{name}")
    if repo.get("archived") or repo.get("disabled"):
        raise RuntimeError("Target repository is archived or disabled")
    if repo.get("fork"):
        raise RuntimeError("Forks require a separate security review")
    default = repo["default_branch"]
    if not re.fullmatch(r"[A-Za-z0-9_./-]+", default) or ".." in default:
        raise RuntimeError("Unsupported default branch")
    if default != "main":
        raise RuntimeError(f"Target default branch is {default!r}; this template currently requires main")
    files = {PATH: caller(), PRECOMMIT_PATH: precommit_config()}
    pending = {}
    for path, expected in files.items():
        existing = gh("GET", f"repos/{owner}/{name}/contents/{path}?ref={default}", allow_404=True)
        if existing:
            old = base64.b64decode(existing["content"]).decode("utf-8")
            if old != expected:
                raise RuntimeError(
                    f"{path} already exists with different content. "
                    "Review manually; installer will not overwrite it."
                )
        else:
            pending[path] = expected
    if not pending:
        print("Security workflow and local secret-scanning configuration already installed.")
        return 0
    base = gh("GET", f"repos/{owner}/{name}/git/ref/heads/{default}")
    branch = f"ots/security-onboarding-{BASELINE[:10]}"
    try:
        gh("POST", f"repos/{owner}/{name}/git/refs",
           {"ref": f"refs/heads/{branch}", "sha": base["object"]["sha"]})
    except RuntimeError as exc:
        raise RuntimeError(
            f"Could not create onboarding branch {branch}. "
            "Resolve any existing branch or missing permissions and retry."
        ) from exc
    for path, expected in pending.items():
        gh("PUT", f"repos/{owner}/{name}/contents/{path}", {
            "message": f"security: install {path}",
            "content": base64.b64encode(expected.encode()).decode(),
            "branch": branch,
        })
    pr = gh("POST", f"repos/{owner}/{name}/pulls", {
        "title": "Security: install OTS universal DevSecOps checks",
        "head": branch,
        "base": default,
        "body": (
            "Installs the shared, commit-pinned OTS_DevOps security workflow "
            "Includes Trivy, TruffleHog, Semgrep CE, OSV, applicable tests, "
            "linting/type checks and conditional skill inspection.\n\n"
            "This PR does not change branch protection, release pipelines, "
            "autonomous-agent runtime sandboxing, or OWASP ZAP environments. "
            "Review the checks and repository-specific applicability before merging."
        ),
        "draft": False,
    })
    print(f"Onboarding PR created: {pr['html_url']}")
    print("Review the PR and merge only after checks pass.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, KeyError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
