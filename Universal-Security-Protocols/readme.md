# OTS Universal DevOps Security — Active Protocol

**Scope:** all five active repositories accessible to the connected GitHub account: OTS_DevOps, OTS-Jarvis, OTS-Security-Suite, TanDM, Clipboard-History.

This document deliberately distinguishes **active automated checks**, **conditional checks**, and **not deployed / removed from the active protocol**. A passing scan is not proof that pushing a secret is impossible: GitHub Actions scan after the push, not before.

## Active automated GitHub Actions baseline — all five repositories

The central source is [security-baseline.yml](../.github/workflows/security-baseline.yml). Each repository has a caller named `.github/workflows/ots-universal-security.yml`; application callers pin the reviewed central commit `b50882793af0a1e01a8c193b2b6317b94ffa0b6f`.

These jobs run on pull requests, pushes to `main`, weekly, and manually:

| Control | Actual enforcement |
| --- | --- |
| Trivy | High/critical dependency, secret and misconfiguration findings block the scan |
| TruffleHog | Scans Git history for verified and unknown credentials; findings block the scan |
| Semgrep CE | Source-code security rules at ERROR severity block the scan; language coverage varies |
| OSV-Scanner | Scans dependency manifests and lockfiles for known vulnerable components |
| Applicable tests | Project-specific Python tests, Go tests/vet, .NET build/test checks where configured |
| Source checks | Python compilation and selected Ruff correctness checks; JS/CJS syntax checks; Mypy for Jarvis and TanDM; .NET compilation |

**Scope limits:** Python style rules E4/E7 currently report findings but are not a blocking gate. JavaScript syntax checking is not a comprehensive JS/TS linter. Scan results reflect the code and rules examined, not a guarantee of complete coverage.

## Additional checks that have an actual project workflow

- **OWASP ZAP:** Jarvis and TanDM have separate isolated, loopback-only passive web baseline workflows; both had verified successful runs. These jobs are not in the all-repository workflow, and do not scan production.
- **Release integrity:** Windows application workflows have their own package, checksum and/or build attestation checks. TanDM and Security Suite had successful Windows verification runs. Clipboard History's broken workflow YAML was repaired November 19, 2026; validate the new build before claiming release checks pass. Jarvis Windows pilot is manual-only and has not been re-run after the YAML repair.
- **Local pre-commit detection:** All five repositories contain a Gitleaks `.pre-commit-config.yaml`. This configuration **does not activate itself**. Each developer must install Python, Go, pre-commit and run `pre-commit install` inside every local clone. Cloud-based AI commits can bypass these hooks.

## Not deployed — excluded from the active protection claims

| Item | Status and rationale |
| --- | --- |
| NVIDIA SkillSpector | Conditional job only: runs if a repository contains `SKILL.md`; no skills were present at initial rollout. Do not claim it has performed a skill scan. |
| NVIDIA OpenShell | **Not deployed.** This is an agent runtime sandbox, not GitHub Actions scanning. Must be addressed separately before giving Jarvis autonomous code/tool execution. |
| GitHub branch enforcement | **Not configured across all repositories.** GitHub App cannot administer rules. Clipboard History has an active ruleset preventing deletion and force pushes, but it does **not** require successful checks. Other accessible public repositories had no reported rulesets; TanDM ruleset inspection was blocked by GitHub plan restrictions. |
| GitHub secret scanning / push protection | Account and repository setting cannot be read or changed through this GitHub connection. Not verified. GitHub Actions scans occur **after** pushes; do not treat them as preventive push blocking. |
| GitHub release provenance everywhere | Per-project and plan-dependent. Do not count as universal until each actual release workflow verifies signatures/attestations. |

Items in this section are **not counted as deployed universal controls**. They remain security risks or future architecture requirements; removing them from the active checklist does not make the underlying risk disappear.

## Onboard future repositories

[Run the OTS_DevOps installer](https://github.com/ohanatechsolutions/OTS_DevOps/actions/workflows/install-universal-security.yml) to create a reviewable pull request adding the shared CI caller and the local Gitleaks configuration.

**Activation is currently blocked by an account-owner-only step:** The workflow needs an Actions repository secret named `OTS_SECURITY_INSTALL_TOKEN`. The connected GitHub App cannot create fine-grained personal access tokens or write GitHub Actions secrets, so this secret has **not** been created.

One-time setup by the owner:

1. [Create a fine-grained personal access token](https://github.com/settings/personal-access-tokens/new) for the `ohanatechsolutions` account, scoped to target repositories with Contents read/write and Pull requests read/write.
2. [Add it as the `OTS_SECURITY_INSTALL_TOKEN` Actions secret](https://github.com/ohanatechsolutions/OTS_DevOps/settings/secrets/actions) in OTS_DevOps. Never paste the token into ChatGPT or commit it to a file.
3. For future repositories, give the token access to the new repository, then run the OTS_DevOps installation workflow and merge its pull request after reviewing the checks.

The installer never grants itself administrative access or activates GitHub push protection, branch rulesets or local Git hooks. The shared workflow stays pinned to an audited revision; upgrades require review.

## Keep these expectations

- A green security scan indicates **the listed checks passed** on a particular run, not that all leaks are impossible.
- Never commit actual tokens, customer records, `.env` values or private key material. Use a secret manager/environment variables, and a project-specific `.gitignore`.
- If a credential is pushed, revoke/rotate it immediately: removing it from the latest commit does not remove historical exposure.
- [Actions tab](https://github.com/ohanatechsolutions/OTS_DevOps/actions) is the authoritative place to inspect live results, failures and skipped jobs.
