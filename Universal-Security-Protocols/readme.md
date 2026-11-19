# OTS Universal DevOps Security

This directory documents the baseline security checks used by Ohana Tech Solutions repositories.

## What is deployed

The source of truth is [the reusable GitHub Actions workflow](../.github/workflows/security-baseline.yml).
Each participating repository has its own `.github/workflows/ots-universal-security.yml`
calling the shared workflow. The central repository calls it locally.

The shared workflow uses Trivy to inspect the checked-out repository for:
- known vulnerabilities in dependencies detectable from repository manifests/lockfiles;
- suspected hard-coded secrets;
- detectable misconfigurations.

High and critical findings return a nonzero exit code. All scans run in GitHub-hosted
Actions runners; they do not require business production credentials.

## Execution and limits

Runs on every pull request, on pushes to `main`, manually, and at 16:17 UTC on Mondays.
This is **not** evidence of zero vulnerabilities. Coverage depends on the supported
ecosystems and manifest/lockfile quality. It does not replace CodeQL/SAST, a full
historical secrets scan, penetration testing, license review, malware sandboxing,
or runtime testing.

The shared workflow version in application repositories is **commit-pinned** to
`db739a5baa60c667b5621ab028583063a807218d`. Changes to the central
workflow must be reviewed and explicitly adopted by updating that SHA in each
calling repository. The central repository itself calls the local workflow.

## Reviewing results

1. Open the repository's **Actions** tab.
2. Open **OTS Universal Security**, then **Universal security baseline**.
3. Inspect the **Scan dependencies, secrets, and configuration** step.
4. Confirm severity, affected package or file, exploitability, and remediation.
5. Fix confirmed high/critical findings and rerun. Document justified false positives
   rather than disabling scanning globally.
6. For releases, require the successful baseline status and project-specific tests.

The workflow has read-only `contents` permissions and does not require repository
secrets. Never add production tokens to scan inputs. Dependency databases and
third-party action downloads may require outbound network access.

## Repo-specific security requirements

| Repository | Additional review beyond baseline |
| --- | --- |
| OTS-Jarvis | Agent tool permissions, prompt injection, local inference service binding, remote access |
| OTS-Security-Suite | Untrusted archives/files, scanner sandboxing, installer and signature verification |
| TanDM | Google/Meta OAuth, employee authorization, webhooks, message privacy, session controls |
| Clipboard-History | Clipboard confidentiality, secure local storage, startup behavior, installer integrity |
| OTS_DevOps | Workflow permissions, dependency pinning, template change reviews |

## Governance

- Do not grant write or admin tokens to pull-request security jobs.
- Do not execute untrusted PR code with privileged credentials.
- Keep application build/release workflows intact; this baseline is additive.
- Review versions and security advisories for GitHub Actions dependencies.
- Enable protected main branches and required security checks once check names are
  confirmed stable and initial findings have been triaged.
- If a repository is private, verify plan and organization access to any additional
  GitHub Advanced Security features before depending on them.

## Next improvements

Add language-aware SAST, build/test quality gates, verified SBOMs, signing
and provenance controls, and private-repository access policies on a
per-project basis. These controls are not claimed to be installed by this baseline.
