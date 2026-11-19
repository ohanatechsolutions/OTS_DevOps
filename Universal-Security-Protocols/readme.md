# OTS Universal DevOps Security — Deployment and Audit

**Account:** `ohanatechsolutions` · **Scope:** five accessible active repositories · **Deployment:** November 18, 2026 (Hawaii time)

## Shared security infrastructure

The canonical workflow is [`.github/workflows/security-baseline.yml`](../.github/workflows/security-baseline.yml).
Each of the five repositories calls it through `.github/workflows/ots-universal-security.yml`.
External caller repositories pin an exact OTS_DevOps commit rather than the mutable `main` branch.
This pin must be updated intentionally whenever the central workflow changes.

Security checks run on pull requests, pushes to `main`, weekly, and by manual dispatch.
All scanner jobs use read-only repository contents and no production secrets.

| Control | Implementation | Interpretation |
| --- | --- | --- |
| Trivy | Repository filesystem SCA, secrets and configuration | High/critical findings fail |
| TruffleHog | Full Git-history credential scanning | Verified and unknown credential results, fails if detected |
| Semgrep CE | Registry security-audit rules; source scan on tracked supported languages | ERROR-level rules fail; listed extensions are not coverage guarantees |
| OSV-Scanner | Official container checks manifests and lockfiles recursively | Vulnerability findings fail; no artifact upload needed |
| Python QA | Compile check; Ruff correctness rules; existing E4/E7 style debt reported | Errors fail; existing style debt nonblocking and disclosed |
| Python type checking | Mypy for Jarvis and TanDM | Failing errors now block CI; initial Meta webhook payload type issue has been corrected |
| Python automated tests | Project-specific pytest/unittest suites for Jarvis, TanDM, Suite | Failing suite fails |
| Go QA | `go test ./...`, `go vet ./...` in Security Suite scanner | Failing commands fail |
| JavaScript | `node --check` for JS/CJS source files | Syntax errors fail; not a full linter/type checker |
| .NET | Windows .NET 10 Release builds; projects under tests are exercised | Compilation or applicable tests fail |
| NVIDIA SkillSpector | Detect `SKILL.md`, invoke static `skillspector scan --no-llm` if present | N/A if none found; no external LLM is used |
| NVIDIA OpenShell | Runtime sandbox policy for autonomous agents | Not automatically deployed; current Jarvis action surface is administrator-click-only, not an autonomous tool registry |
| OWASP ZAP | Isolated loopback-only passive baseline CI for Jarvis and TanDM | Weekly/manual, never scans public production URLs; unauthenticated surface only |
| Release packages | Project-specific hash verification, plus signed GitHub provenance generation and verification added to Jarvis, Clipboard-History and Security Suite build workflows | Must pass actual release build; not yet proven by an attestation verification run |

## Not installed or not yet provable

1. **Branch protection/rulesets are NOT configured by this integration.** GitHub returned HTTP 403 (`Resource not accessible by integration`) for reading protection settings. An account administrator must configure and verify them.
2. **OpenShell sandbox runtime is NOT installed.** It becomes a required deployment gate *before enabling autonomous code execution or unrestricted tool calling* in Jarvis or any other agent application. Current CI merely records this dependency; it cannot prove a runtime deployment.
3. **Cryptographic build attestations are now configured for the three public Windows application pipelines, but their execution/verification has not yet been proven.** TanDM is private: GitHub's artifact-attestation feature on GitHub Free/Pro/Team is restricted to public repositories. SHA-256 comparison alone proves integrity against the build-produced checksum, not authenticity of the builder or signing identity.
4. ZAP does not authenticate as users, inspect production deployments, or substitute for penetration tests. Execute solely against ephemeral, synthetic-test instances.
5. This common scan is not a complete language-specific type-check for every language; each project retains existing build/type-check jobs.
6. GitHub-hosted Actions and artifact storage have plan-specific limits. GitHub security attestation eligibility also differs for public and private repositories. During initial rollout, GitHub reported an artifact storage quota failure in the previous OSV workflow; the shared OSV implementation avoids uploading artifacts.

## Administrator action: protect `main`

For each repository go to **Settings → Rules → Rulesets** (or **Settings → Branches → Branch protection rules**, depending on available controls). Create an active rule targeting `main`:

- Require a pull request before merging (recommended: at least one review).
- Require passing *stable, successfully tested* checks:
  - `Universal security baseline / Trivy filesystem baseline`
  - `Universal security baseline / TruffleHog credential history`
  - `Universal security baseline / Semgrep CE source scan`
  - `Universal security baseline / OSV dependency and lockfile audit`
  - `Universal security baseline / Applicable tests and source checks`
  - For C# repos, also `Universal security baseline / .NET build and test`
- Prevent force pushes and branch deletion.
- Apply protections to administrators unless an explicit, documented emergency exception exists.
- Restrict releases to successful QA and signing/provenance requirements separately.
- Confirm plan eligibility, especially for the private TanDM repository. Do not mark protection completed until GitHub displays and enforces the rule.

Do **not** make the weekly ZAP workflow a required PR check; it is not triggered per pull request.

## Triage policy

A green check means that individual job passed for its tested scope. Never convert `SKIPPED`, `N/A`, `BLOCKED`, `NOT RUN`, or a report-only lint result to `PASS`.
TruffleHog findings may include real credentials: rotate and revoke any exposed token before removing it from code/history.
For Semgrep or OSV findings, confirm exploitability and fixed version before changing dependencies. Keep justified exceptions narrowly scoped and reviewed.

## Per-repository risk priorities

- **OTS-Jarvis:** Require sandboxing for autonomous agent tool execution, admin MFA, remote-access isolation, least privilege, prompt-injection tests.
- **OTS-Security-Suite:** Treat scanned repositories as hostile, enforce file/archive bounds, test native scanners and installer signatures.
- **TanDM:** Protect OAuth secrets, webhook signatures, role permissions, session data and customer messages; address discovered dependency CVEs.
- **Clipboard-History:** Protect sensitive clipboard history and Windows startup/tray behavior; verify installer integrity.
- **OTS_DevOps:** Pin reusable actions and workflow revisions, audit change control, avoid unauthorized token permissions.

## Maintainer workflow

Review **Actions → OTS Universal Security** in each repository. Fix failing jobs and rerun.
Pin new reusable-workflow commits deliberately after reviewing central changes. Existing app release workflows remain separate and must not be replaced by generic security jobs.
