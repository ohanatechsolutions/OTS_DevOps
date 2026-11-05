# 05 — Release, Operations and Platform-Specific Checklists

**Purpose:** Convert verified code into a real installable or accessible release, maintain it safely, and apply the extra checks appropriate to the software platform.

> **Source-library usage:** These five files are reusable reference material for a ChatGPT Project or other coding AI. They are *not* an application, code repository, evidence of passing tests, or automatically updated project records. Create and maintain project-specific working records in the actual software repository or another explicitly writable workspace. Upload all five to the ChatGPT Project and tell the AI to apply the relevant parts. AI access to a GitHub repository must be connected/authorized separately.
> **Status rule:** These source checkboxes remain reusable templates. In the *writable project tracker*, check an item only after verifying the real project; otherwise record `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, or `N/A — reason`. Small projects can mark genuinely irrelevant work N/A. Never waive safety-critical checks silently.


## Go / no-go contract

**Never ship solely because code compiles.** The release owner must confirm: supported requirements and P0/P1 tests, security/privacy review, known risks, real artifact/deploy, clean install or equivalent, upgrade/migration/rollback where relevant, accurate documentation and cost/permissions approval. Publishing or messaging users requires explicit authorization.

**Specialized addenda are conditional:** Do not force mobile store procedures on Windows desktop utilities; do not omit agent approval controls for an automation system. Apply each relevant subsection of Phase 08 and mark unrelated ones `N/A — reason` in the *project* tracker.

## Phase 06 — Packaging, deployment and launch

> **Phase gate:** Signed-off real artifact/deployment has been independently tested and published.

**Module index** (use only modules applicable to this project):

- [06.01 — Reproducible Builds and CI/CD](#0601-reproducible-builds-and-cicd) — 12 checks
- [06.02 — Packaging, Installer, Artifact Integrity and Signatures](#0602-packaging-installer-artifact-integrity-and-signatures) — 12 checks
- [06.03 — Staging, Production and Deployment Strategy](#0603-staging-production-and-deployment-strategy) — 12 checks
- [06.04 — Versions, Changelog, Release Notes and Compatibility](#0604-versions-changelog-release-notes-and-compatibility) — 10 checks
- [06.05 — Distribution, Store Approval and Public Presence](#0605-distribution-store-approval-and-public-presence) — 11 checks
- [06.06 — Final Go/No-Go Release Gate](#0606-final-gono-go-release-gate) — 12 checks
- [06.07 — Launch Day Execution and Smoke Checks](#0607-launch-day-execution-and-smoke-checks) — 12 checks
- [06.08 — Rollback, Hotfix and Kill Switches](#0608-rollback-hotfix-and-kill-switches) — 10 checks

### 06.01 — Reproducible Builds and CI/CD

**When to use:** All software projects. **Goal:** Make deliverables reproducible without hidden paid infrastructure.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.01.01** — Define build commands and pinned toolchain versions.
- [ ] **06.01.02** — Create local build/test script as primary source of truth.
- [ ] **06.01.03** — Configure CI only if its cost, permissions and availability are approved.
- [ ] **06.01.04** — Limit CI token permissions and protect secrets and artifacts.
- [ ] **06.01.05** — Run formatting, lint, type, unit, integration and security checks in order.
- [ ] **06.01.06** — Use caching cautiously without masking stale dependencies.
- [ ] **06.01.07** — Build on intended target OS/architecture and capture logs.
- [ ] **06.01.08** — Verify deterministic/repeatable output or document nondeterminism.
- [ ] **06.01.09** — Record build source commit, runtime, dependency lock and build timestamp.
- [ ] **06.01.10** — Keep release signing keys outside CI unless approved secure mechanism exists.
- [ ] **06.01.11** — Retain build results and show pass/fail per step.
- [ ] **06.01.12** — Prohibit automatic publishing without explicit approved release policy.

**Required proof / deliverables**

- [ ] Local reproducible build runbook and optional approved CI config.
- [ ] Green checks and source-to-artifact mapping.

**Exit criterion:** A clean checkout can produce a testable artifact without manual hidden steps.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.02 — Packaging, Installer, Artifact Integrity and Signatures

**When to use:** All software projects. **Goal:** Ship authentic installable output, not renamed or placeholder files.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.02.01** — Define target artifact type (.exe/.msi/.dmg/.app/.apk/.aab/package/container etc.).
- [ ] **06.02.02** — Choose platform-specific packaging and required metadata.
- [ ] **06.02.03** — Verify binary magic/header, architecture and entrypoint.
- [ ] **06.02.04** — Bundle required runtime/assets or document prerequisites accurately.
- [ ] **06.02.05** — Define app ID, publisher, version, paths and file associations as needed.
- [ ] **06.02.06** — Verify clean install without developer tools present.
- [ ] **06.02.07** — Test launch, update, repair and uninstall including user data rules.
- [ ] **06.02.08** — Compute SHA-256 hash and verify downloaded/copied artifact matches it.
- [ ] **06.02.09** — Sign artifacts with legitimate publisher identity when feasible; disclose unsigned limitations.
- [ ] **06.02.10** — Avoid distributing private signing keys or credentials.
- [ ] **06.02.11** — Check antivirus/OS reputation warnings; never claim a hash eliminates warnings.
- [ ] **06.02.12** — Record artifact size, hash, platform, commit and release notes.

**Required proof / deliverables**

- [ ] Real executable or package plus checksum, manifest and install-test evidence.
- [ ] Signing/unsigned status accurately documented.

**Exit criterion:** Release artifact actually runs on intended target and its integrity can be verified.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.03 — Staging, Production and Deployment Strategy

**When to use:** All software projects. **Goal:** Treat deployment as a controlled state change.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.03.01** — Define release target and infrastructure ownership.
- [ ] **06.03.02** — Create staging close enough to production for meaningful verification.
- [ ] **06.03.03** — Inventory production secrets, domains, certificates and infrastructure state.
- [ ] **06.03.04** — Define schema migration ordering and compatibility.
- [ ] **06.03.05** — Define maintenance/lockdown/read-only windows if required.
- [ ] **06.03.06** — Prepare feature flags, canary, phased rollouts or manual staged install.
- [ ] **06.03.07** — Write commands, expected outputs and responsible operator.
- [ ] **06.03.08** — Verify infrastructure access and least-privilege permissions.
- [ ] **06.03.09** — Plan health checks and traffic routing after deployment.
- [ ] **06.03.10** — Define rollback trigger and recovery path before deployment.
- [ ] **06.03.11** — Check backup and restore readiness with timestamps.
- [ ] **06.03.12** — Require human approval for production changes unless delegated explicitly.

**Required proof / deliverables**

- [ ] Versioned deployment runbook and go/no-go checklist.
- [ ] Staging verification record and rollback plan.

**Exit criterion:** A person other than author can deploy and recover from failure using instructions.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.04 — Versions, Changelog, Release Notes and Compatibility

**When to use:** All software projects. **Goal:** Explain what users receive and how it impacts existing installations.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.04.01** — Select meaningful version strategy and label pre-releases distinctly.
- [ ] **06.04.02** — Record exact commit/tag associated with release.
- [ ] **06.04.03** — Summarize user-facing features, fixes and breaking changes.
- [ ] **06.04.04** — Document required migrations, backups and downtime.
- [ ] **06.04.05** — List compatible OS/browser/runtime versions and minimum hardware.
- [ ] **06.04.06** — Note known limitations and workarounds transparently.
- [ ] **06.04.07** — Document upgrade and downgrade compatibility where applicable.
- [ ] **06.04.08** — Include security changes without revealing exploitable details prematurely.
- [ ] **06.04.09** — Update installation/usage docs and support contacts.
- [ ] **06.04.10** — Keep past release notes available for support and rollback.

**Required proof / deliverables**

- [ ] Versioned release notes and updated changelog.
- [ ] Compatibility and upgrade notes.

**Exit criterion:** Users can decide whether/how to install or upgrade safely.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.05 — Distribution, Store Approval and Public Presence

**When to use:** All software projects. **Goal:** Make release obtainable and compliant with its target channel.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.05.01** — Choose website, GitHub Release, app store, browser store or managed rollout.
- [ ] **06.05.02** — Check platform listing, review, privacy and permission policies.
- [ ] **06.05.03** — Create accurate product description, screenshots and icon assets.
- [ ] **06.05.04** — Prepare license, privacy notice, support link and publisher identity.
- [ ] **06.05.05** — Prepare domain ownership, download URLs and secure hosting if required.
- [ ] **06.05.06** — Document user onboarding, download steps and troubleshooting.
- [ ] **06.05.07** — Choose download verification and update channel strategy.
- [ ] **06.05.08** — Provide release checksums and signatures when relevant.
- [ ] **06.05.09** — Test download from a clean browser/device and verify exact artifact.
- [ ] **06.05.10** — Record any store review/rejection and correction.
- [ ] **06.05.11** — Do not declare published until public listing/download actually resolves.

**Required proof / deliverables**

- [ ] Verified distribution location and installation instructions.
- [ ] Listing and policy review evidence.

**Exit criterion:** Intended audience can find, obtain, verify and use the exact released build.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.06 — Final Go/No-Go Release Gate

**When to use:** All software projects. **Goal:** Consolidate proof from every preceding stage.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.06.01** — Confirm approved scope and requirements coverage.
- [ ] **06.06.02** — Confirm tests pass on supported platforms with report links.
- [ ] **06.06.03** — Confirm no open blocker/critical bugs or unapproved severe security findings.
- [ ] **06.06.04** — Confirm secrets, dependencies and licenses reviewed.
- [ ] **06.06.05** — Confirm performance and accessibility targets or approved deviations.
- [ ] **06.06.06** — Confirm backups, restore, migration and rollback tested where needed.
- [ ] **06.06.07** — Confirm real artifact exists and hash/install verification passes.
- [ ] **06.06.08** — Confirm docs, release notes, support path and privacy notices accurate.
- [ ] **06.06.09** — Confirm monitoring, ownership and incident contacts ready.
- [ ] **06.06.10** — Confirm cost caps, data egress and external permissions approved.
- [ ] **06.06.11** — Record human product/security/operations go/no-go decisions.
- [ ] **06.06.12** — Freeze commit/tag and artifact identifiers prior to publication.

**Required proof / deliverables**

- [ ] Signed release decision in `RELEASE_STATUS.md`.
- [ ] Evidence index of tests, scans, artifacts and approvals.

**Exit criterion:** All P0 gates pass; exceptions are explicit, dated and owned.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.07 — Launch Day Execution and Smoke Checks

**When to use:** All software projects. **Goal:** Verify production/public release, not only local tests.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.07.01** — Record planned launch window and on-call owner.
- [ ] **06.07.02** — Verify latest backup and rollback prerequisites.
- [ ] **06.07.03** — Confirm final build hash/tag matches approved artifact.
- [ ] **06.07.04** — Deploy/publish using the documented runbook.
- [ ] **06.07.05** — Verify service/app availability from a clean independent environment.
- [ ] **06.07.06** — Complete top three critical end-to-end smoke flows.
- [ ] **06.07.07** — Verify authentication, core data persistence and permissions.
- [ ] **06.07.08** — Verify telemetry/diagnostics work without exposing private data.
- [ ] **06.07.09** — Check payment, email or external integration if applicable with safe test method.
- [ ] **06.07.10** — Monitor errors, resource usage, crash rate and cost after release.
- [ ] **06.07.11** — Record actual release links, timestamps and outcomes.
- [ ] **06.07.12** — Declare release complete only after independent confirmation.

**Required proof / deliverables**

- [ ] Completed launch log and live smoke test evidence.
- [ ] Final release location and public version recorded.

**Exit criterion:** Released artifact is accessible and P0 flows work in the target environment.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 06.08 — Rollback, Hotfix and Kill Switches

**When to use:** All software projects. **Goal:** Make bad releases recoverable.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **06.08.01** — Define immediate stop/disable mechanism for dangerous functionality.
- [ ] **06.08.02** — Document rollback by app type: binary, service, extension or mobile.
- [ ] **06.08.03** — Determine database backward compatibility and forward-fix strategy.
- [ ] **06.08.04** — Keep previous verified release artifact or image accessible.
- [ ] **06.08.05** — Practice restore/rollback in staging when practical.
- [ ] **06.08.06** — Define emergency hotfix branch and approval expectations.
- [ ] **06.08.07** — Prepare incident communications for affected users.
- [ ] **06.08.08** — Define conditions requiring security notification or credential rotation.
- [ ] **06.08.09** — Test feature flag kill switch and permissions revocation.
- [ ] **06.08.10** — Record incident timeline and postmortem follow-up after rollback.

**Required proof / deliverables**

- [ ] Executable rollback/hotfix runbook and rehearsal evidence.
- [ ] Owner and decision trigger for rollback.

**Exit criterion:** Operators can stop impact and restore critical service/data safely.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---
## Phase 07 — Monitoring, support and maintenance

> **Phase gate:** Ownership, incident response, vulnerability updates and sunset plan exist.

**Module index** (use only modules applicable to this project):

- [07.01 — Monitoring, Health and Operational Alerts](#0701-monitoring-health-and-operational-alerts) — 10 checks
- [07.02 — User Help, Support and Troubleshooting](#0702-user-help-support-and-troubleshooting) — 10 checks
- [07.03 — Incidents, Outages and Security Response](#0703-incidents-outages-and-security-response) — 10 checks
- [07.04 — Vulnerability Handling and Dependency Maintenance](#0704-vulnerability-handling-and-dependency-maintenance) — 10 checks
- [07.05 — Feedback, Product Analytics and Iteration](#0705-feedback-product-analytics-and-iteration) — 10 checks
- [07.06 — Handover, Deprecation and End-of-Life](#0706-handover-deprecation-and-end-of-life) — 10 checks

### 07.01 — Monitoring, Health and Operational Alerts

**When to use:** All software projects. **Goal:** Detect outages and silent failure after launch.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.01.01** — List critical health indicators and expected normal range.
- [ ] **07.01.02** — Track crashes, latency, errors, failures and job backlog as relevant.
- [ ] **07.01.03** — Track disk, CPU, RAM, storage and network saturation.
- [ ] **07.01.04** — Track external dependency health, rate limits and cost.
- [ ] **07.01.05** — Set privacy-safe metrics and alert routing rules.
- [ ] **07.01.06** — Set actionable alert thresholds, owners and severity.
- [ ] **07.01.07** — Create synthetic smoke or periodic manual check for P0 workflow.
- [ ] **07.01.08** — Test one alert end-to-end and document response.
- [ ] **07.01.09** — Define noise reduction, deduplication and escalation.
- [ ] **07.01.10** — Review SLO or quality targets on an agreed cadence.

**Required proof / deliverables**

- [ ] Live health dashboard or manual operational checks.
- [ ] Alert response checklist and test evidence.

**Exit criterion:** A significant failure will be noticed by someone accountable.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 07.02 — User Help, Support and Troubleshooting

**When to use:** All software projects. **Goal:** Ensure people can recover without contacting original developer.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.02.01** — Create install, first-run and daily-use quickstart.
- [ ] **07.02.02** — Document screenshots/commands for core features.
- [ ] **07.02.03** — Write frequently encountered errors with probable cause and next steps.
- [ ] **07.02.04** — Specify compatibility limitations and system requirements.
- [ ] **07.02.05** — Provide support/contact or issue-report path as promised.
- [ ] **07.02.06** — Define diagnostic bundle that excludes secrets and private data by default.
- [ ] **07.02.07** — Document export, backup, restore and uninstall behavior.
- [ ] **07.02.08** — Provide how to revoke access and delete data.
- [ ] **07.02.09** — Set support boundaries and response expectations truthfully.
- [ ] **07.02.10** — Test documentation with someone unfamiliar with code.

**Required proof / deliverables**

- [ ] User guide and troubleshooting FAQ.
- [ ] Verified help/contact path.

**Exit criterion:** Users can perform primary operations and recover common mistakes.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 07.03 — Incidents, Outages and Security Response

**When to use:** All software projects. **Goal:** Handle unexpected harm with controlled response.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.03.01** — Define incident severity, owner and triage channel.
- [ ] **07.03.02** — Identify who can disable a feature, revoke tokens or roll back.
- [ ] **07.03.03** — Maintain contact and escalation list securely.
- [ ] **07.03.04** — Define evidence preservation without unnecessary personal data.
- [ ] **07.03.05** — Define containment, diagnosis, remediation and recovery phases.
- [ ] **07.03.06** — Prepare user status updates and notification decision tree.
- [ ] **07.03.07** — List legal/regulatory notice triggers for qualified review.
- [ ] **07.03.08** — Document restoration validation and monitoring after recovery.
- [ ] **07.03.09** — Run at least a tabletop of data loss or compromised token.
- [ ] **07.03.10** — Complete a blameless postmortem with tracked improvements.

**Required proof / deliverables**

- [ ] Incident runbook and tabletop result.
- [ ] Postmortem/lessons learned template.

**Exit criterion:** A severe incident can be triaged and contained without relying on chat memory.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 07.04 — Vulnerability Handling and Dependency Maintenance

**When to use:** All software projects. **Goal:** Keep shipped software safe as the world changes.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.04.01** — Publish or document responsible vulnerability reporting channel.
- [ ] **07.04.02** — Monitor runtime, dependency and platform security advisories.
- [ ] **07.04.03** — Schedule dependency updates and regression testing.
- [ ] **07.04.04** — Triages findings by exploitation risk and exposure.
- [ ] **07.04.05** — Rotate/revoke compromised secrets promptly and investigate scope.
- [ ] **07.04.06** — Issue security patches and accurate advisories when appropriate.
- [ ] **07.04.07** — Review user-granted scopes and vendor tokens periodically.
- [ ] **07.04.08** — Audit backups, update channels and signing keys.
- [ ] **07.04.09** — Review access controls and departing contributor permissions.
- [ ] **07.04.10** — Track unsupported versions and end-of-support date.

**Required proof / deliverables**

- [ ] Maintenance calendar and vulnerability tracking record.
- [ ] Patch and customer notification procedure.

**Exit criterion:** Maintenance ownership and a path to fix future vulnerabilities exist.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 07.05 — Feedback, Product Analytics and Iteration

**When to use:** All software projects. **Goal:** Use evidence to guide updates without surveillance.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.05.01** — Define essential success metrics before collecting data.
- [ ] **07.05.02** — Choose privacy-preserving aggregate analytics or local-only metrics.
- [ ] **07.05.03** — Disclose collection and honor consent preferences.
- [ ] **07.05.04** — Track onboarding completion, errors and task success.
- [ ] **07.05.05** — Review support reports, usage feedback and performance regression.
- [ ] **07.05.06** — Separate anecdotal requests from validated patterns.
- [ ] **07.05.07** — Update backlog and product decisions with supporting evidence.
- [ ] **07.05.08** — Run small releases with versioned acceptance tests.
- [ ] **07.05.09** — Track whether automations actually saved time or improved outcomes.
- [ ] **07.05.10** — Check feature deprecation impact on real users.

**Required proof / deliverables**

- [ ] Post-launch review and evidence-backed backlog.
- [ ] Versioned changes to success metrics.

**Exit criterion:** Next work is prioritized by outcomes, safety and real usage evidence.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 07.06 — Handover, Deprecation and End-of-Life

**When to use:** All software projects. **Goal:** Plan for software eventually changing owners or being discontinued.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **07.06.01** — Document current architecture, environments and credentials custody.
- [ ] **07.06.02** — Provide reproducible build, release and restoration runbooks.
- [ ] **07.06.03** — Inventory service contracts, domains and paid subscriptions.
- [ ] **07.06.04** — Identify unsupported OS, dependency and API sunset timelines.
- [ ] **07.06.05** — Define upgrade path, deprecation notice and support window.
- [ ] **07.06.06** — Provide user data export and deletion route.
- [ ] **07.06.07** — Revoke tokens, keys and external permissions during shutdown.
- [ ] **07.06.08** — Retire hosting, monitoring and renewals deliberately.
- [ ] **07.06.09** — Archive source/build evidence and audit records appropriately.
- [ ] **07.06.10** — Confirm data destruction/retention obligations are met.

**Required proof / deliverables**

- [ ] Handover inventory and end-of-life plan.
- [ ] Verified data portability and service shutdown tasks.

**Exit criterion:** Product can be transferred or retired without abandoning sensitive data or costs.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---
## Phase 08 — Platform- and product-specific addenda

> **Phase gate:** All relevant addenda are passed; unrelated ones marked N/A with reason.

**Module index** (use only modules applicable to this project):

- [08.01 — Windows Desktop App Addendum](#0801-windows-desktop-app-addendum) — 13 checks
- [08.02 — Web App and SaaS Addendum](#0802-web-app-and-saas-addendum) — 12 checks
- [08.03 — Browser Extension Addendum](#0803-browser-extension-addendum) — 12 checks
- [08.04 — Mobile App Addendum](#0804-mobile-app-addendum) — 12 checks
- [08.05 — AI Agent, Local LLM and Automation Addendum](#0805-ai-agent-local-llm-and-automation-addendum) — 17 checks
- [08.06 — Local-First, Offline and Synchronization Addendum](#0806-local-first-offline-and-synchronization-addendum) — 11 checks
- [08.07 — Security or System Utility Addendum](#0807-security-or-system-utility-addendum) — 14 checks
- [08.08 — Hardware, Edge and IoT Addendum](#0808-hardware-edge-and-iot-addendum) — 11 checks
- [08.09 — Payments, Billing and Subscription Addendum](#0809-payments-billing-and-subscription-addendum) — 11 checks

### 08.01 — Windows Desktop App Addendum

**When to use:** Windows desktop applications. **Goal:** Check Windows-specific concerns missing in generic web checklists.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.01.01** — Choose user-scope versus admin-scope installation and justify elevation.
- [ ] **08.01.02** — Test non-admin account, UAC prompt and denied elevation behavior.
- [ ] **08.01.03** — Test Win10/Win11 versions actually claimed supported.
- [ ] **08.01.04** — Test x64/ARM64 where offered and verify PE headers/architecture.
- [ ] **08.01.05** — Handle file paths, profile folders, roaming and permission-denied gracefully.
- [ ] **08.01.06** — Choose installer/uninstaller, app identity and upgrade code correctly.
- [ ] **08.01.07** — Plan code signing and clearly document unsigned installer warnings.
- [ ] **08.01.08** — Test SmartScreen/Defender interactions; avoid security-bypass instructions.
- [ ] **08.01.09** — Test startup registration, tray behavior and global hotkeys if used.
- [ ] **08.01.10** — Test single-instance behavior, crashes, auto-update and rollback.
- [ ] **08.01.11** — Verify data location, cleanup and preservation during uninstall.
- [ ] **08.01.12** — Check packaging includes dependencies/assets without developer runtime.
- [ ] **08.01.13** — Publish real .exe/.msi plus version, hash, and clean-machine evidence.

**Required proof / deliverables**

- [ ] Windows test matrix and installer verification record.
- [ ] Evidence that release EXE/MSI is genuine and installable.

**Exit criterion:** A non-developer machine can install, run, update and remove safely.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.02 — Web App and SaaS Addendum

**When to use:** Websites, SaaS and hosted APIs. **Goal:** Cover browser, multiuser and hosted operations.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.02.01** — Verify TLS/HTTPS, secure cookies, security headers and CSP.
- [ ] **08.02.02** — Enforce server-side access checks for all objects and tenant boundaries.
- [ ] **08.02.03** — Protect state-changing operations from CSRF as relevant.
- [ ] **08.02.04** — Review CORS/origin and untrusted redirect behavior.
- [ ] **08.02.05** — Test sessions, logout, reset and MFA if offered.
- [ ] **08.02.06** — Test multi-tenant data isolation and cross-account access.
- [ ] **08.02.07** — Design file upload security and stored content serving.
- [ ] **08.02.08** — Set hosted rate/usage limits and billing protections.
- [ ] **08.02.09** — Prepare database migrations, backups, restore and environment isolation.
- [ ] **08.02.10** — Define uptime, monitoring, incident and deployment rollback paths.
- [ ] **08.02.11** — Test common browsers, responsive layouts and slow connections.
- [ ] **08.02.12** — Review SEO, robots, metadata and cookie consent where relevant.

**Required proof / deliverables**

- [ ] Browser and tenant-isolation test matrix.
- [ ] Verified live-domain security/deployment smoke test.

**Exit criterion:** Production web flows are isolated, recoverable, browser-compatible and observable.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.03 — Browser Extension Addendum

**When to use:** Chrome/Edge/Firefox and related extensions. **Goal:** Respect extension permissions and store policies.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.03.01** — Confirm current target browser manifest and extension APIs.
- [ ] **08.03.02** — Request only minimum permissions and narrowly scoped host access.
- [ ] **08.03.03** — Use content security policy compatible with store policies.
- [ ] **08.03.04** — Review background/service-worker lifecycle and persistence behavior.
- [ ] **08.03.05** — Test popup, options, injected content scripts and messaging boundaries.
- [ ] **08.03.06** — Validate untrusted page input and cross-origin data.
- [ ] **08.03.07** — Prevent exposing tokens/storage across page-extension boundaries.
- [ ] **08.03.08** — Test extension upgrade, browser restart and permission revocation.
- [ ] **08.03.09** — Provide clear privacy disclosure and data deletion method.
- [ ] **08.03.10** — Review store listing assets, screenshots and submission requirements.
- [ ] **08.03.11** — Test on clean browser profile with relevant browser versions.
- [ ] **08.03.12** — Verify the installed packed extension matches reviewed source.

**Required proof / deliverables**

- [ ] Manifest permission review and store readiness notes.
- [ ] Fresh-profile extension lifecycle test results.

**Exit criterion:** Minimal-permission extension works safely on supported browser versions.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.04 — Mobile App Addendum

**When to use:** Android and iOS applications. **Goal:** Account for mobile OS lifecycle and app-store review.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.04.01** — Define minimum iOS/Android versions and device/CPU support.
- [ ] **08.04.02** — Test cold launch, backgrounding, resume and process termination.
- [ ] **08.04.03** — Test OS permissions, denial paths and consent copy.
- [ ] **08.04.04** — Check secure keystore/keychain, local encryption and backups.
- [ ] **08.04.05** — Test battery, network transitions, offline mode and push handling.
- [ ] **08.04.06** — Test varied screen sizes, notches, orientations and accessibility.
- [ ] **08.04.07** — Define code signing, provisioning and developer accounts.
- [ ] **08.04.08** — Implement safe deep links and authentication callback validation.
- [ ] **08.04.09** — Test upgrade from last supported version without data loss.
- [ ] **08.04.10** — Review app store privacy declarations and policy requirements.
- [ ] **08.04.11** — Prepare app bundle, screenshots, age rating and review accounts as needed.
- [ ] **08.04.12** — Test crash reporting and support path without sensitive data exposure.

**Required proof / deliverables**

- [ ] Real-device test matrix and signed release package plan.
- [ ] Store declaration and upgrade test evidence.

**Exit criterion:** Real devices and store checks support all published claims.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.05 — AI Agent, Local LLM and Automation Addendum

**When to use:** LLM-powered assistants, autonomous agents and RPA. **Goal:** Prevent autonomous systems from becoming unsafe, costly or uncontrollable.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.05.01** — Define agent mission, allowed tasks, excluded tasks and human oversight.
- [ ] **08.05.02** — Separate untrusted instructions (web/email/files) from trusted system policy.
- [ ] **08.05.03** — Allowlist tools and grant minimum required filesystem/network permissions.
- [ ] **08.05.04** — Use distinct read-only, draft and execute permission levels.
- [ ] **08.05.05** — Require explicit approval for sending, publishing, deleting, purchasing and privilege changes.
- [ ] **08.05.06** — Implement dry-run/preview for material external side effects.
- [ ] **08.05.07** — Validate tool input/output schemas before executing actions.
- [ ] **08.05.08** — Isolate execution in sandbox/container or constrained local user where possible.
- [ ] **08.05.09** — Protect secrets and sensitive local data; redact before cloud handoff.
- [ ] **08.05.10** — Define when cloud inference is prohibited or explicitly opt-in.
- [ ] **08.05.11** — Cap tokens, cost, recursion, retries, API calls and runtime.
- [ ] **08.05.12** — Keep memory bounded, scoped and user-removable.
- [ ] **08.05.13** — Log redacted decision/action metadata for audit and recovery.
- [ ] **08.05.14** — Test indirect prompt injection, poisoned retrieved content and tool-output manipulation.
- [ ] **08.05.15** — Test unauthorized tool calls, approval bypass and multi-step action chaining.
- [ ] **08.05.16** — Define stop/pause/kill switch and compensation/undo behavior.
- [ ] **08.05.17** — Benchmark task accuracy, failure rate and human-time savings using evidence.

**Required proof / deliverables**

- [ ] Agent permission matrix, local/cloud routing rules and red-team report.
- [ ] Verified approval gates, kill switch, spending limits and task tests.

**Exit criterion:** Agent cannot execute forbidden/expensive/high-risk actions without proper authorization.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.06 — Local-First, Offline and Synchronization Addendum

**When to use:** Local-first, hybrid local/cloud and offline-capable apps. **Goal:** Treat local data and network changes as first-class behavior.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.06.01** — Define which features must work fully without network access.
- [ ] **08.06.02** — Define authoritative store and sync trigger policy.
- [ ] **08.06.03** — Specify data replication, conflict detection and merge rules.
- [ ] **08.06.04** — Protect offline secrets and encrypted local caches.
- [ ] **08.06.05** — Test interrupted sync, network flapping and duplicate delivery.
- [ ] **08.06.06** — Test clock skew, timezone and event ordering.
- [ ] **08.06.07** — Test device loss, local restore and re-enrollment.
- [ ] **08.06.08** — Provide transparent offline/sync status and retry controls.
- [ ] **08.06.09** — Enforce data retention and deletion across replicas.
- [ ] **08.06.10** — Test reconnect after schema upgrade and long disconnection.
- [ ] **08.06.11** — Define what gets sent to any external AI service and obtain consent.

**Required proof / deliverables**

- [ ] Offline behavior matrix, conflict strategy and sync test cases.
- [ ] Restore/reenrollment scenario results.

**Exit criterion:** Core flows survive disconnection and sync without silent data corruption.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.07 — Security or System Utility Addendum

**When to use:** Antimalware, firewall, file cleanup and security tools. **Goal:** Apply stricter standards for privileged or destructive tools.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.07.01** — Define exact detection/protection claims and evidence standard.
- [ ] **08.07.02** — Use least privilege; avoid permanent admin rights where possible.
- [ ] **08.07.03** — Require scope-limited authorization before scanning or changing systems.
- [ ] **08.07.04** — Separate detection, review, quarantine, delete and restore actions.
- [ ] **08.07.05** — Prefer reversible quarantine and reliable rollback before destruction.
- [ ] **08.07.06** — Use safe file handling, atomic operations and conflict checks.
- [ ] **08.07.07** — Protect scan results, personal paths and log content.
- [ ] **08.07.08** — Test false positives, protected files, locked files and symlinks.
- [ ] **08.07.09** — Prevent race conditions and TOCTOU in filesystem actions.
- [ ] **08.07.10** — Build disposable test VMs and fixtures for destructive tests.
- [ ] **08.07.11** — Document third-party antivirus compatibility and warnings.
- [ ] **08.07.12** — Avoid claims of perfect threat detection or certification without proof.
- [ ] **08.07.13** — Verify actual binaries/installers rather than placeholder artifacts.
- [ ] **08.07.14** — Require human approval for destructive actions and risky privilege escalation.

**Required proof / deliverables**

- [ ] Safety case for privileged operations and recovery tests.
- [ ] Threat-detection limitation disclosure and functional evidence.

**Exit criterion:** No unreviewed destructive operation and reversible recovery is validated.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.08 — Hardware, Edge and IoT Addendum

**When to use:** Mini PC appliances, edge services, IoT and hardware-assisted software. **Goal:** Account for physical devices and field update failure.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.08.01** — Define CPU/RAM/disk/power and thermal budget with measured test hardware.
- [ ] **08.08.02** — Specify network interfaces, ports, pairing and provisioning.
- [ ] **08.08.03** — Ensure device identity and default credentials are secure.
- [ ] **08.08.04** — Verify boot behavior, brownouts, power loss and filesystem integrity.
- [ ] **08.08.05** — Define signed firmware/updates and rollback/recovery mode.
- [ ] **08.08.06** — Plan secure local network discovery and firewall exposure.
- [ ] **08.08.07** — Define fan/noise/thermal and enclosure constraints.
- [ ] **08.08.08** — Test hardware revision variation, accessories and peripheral disconnection.
- [ ] **08.08.09** — Define physical access risks and stored secret protection.
- [ ] **08.08.10** — Define factory reset, secure wipe and device transfer.
- [ ] **08.08.11** — Define diagnostics and update path for disconnected devices.

**Required proof / deliverables**

- [ ] Hardware compatibility matrix and field recovery instructions.
- [ ] Power-loss, update and reset test evidence.

**Exit criterion:** Device operates and can recover in real field conditions.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 08.09 — Payments, Billing and Subscription Addendum

**When to use:** Checkout, billing, subscriptions and commerce. **Goal:** Protect financial actions and avoid inaccurate accounting.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **08.09.01** — Choose compliant third-party payment processing; do not store raw card data.
- [ ] **08.09.02** — Define product, tax, refund, currency and pricing rules clearly.
- [ ] **08.09.03** — Validate payment status using server-side provider events.
- [ ] **08.09.04** — Verify webhook signatures and duplicate event handling.
- [ ] **08.09.05** — Ensure no user can change server-owned price or entitlement fields.
- [ ] **08.09.06** — Implement invoice/receipt and audit record retention rules.
- [ ] **08.09.07** — Test failed, delayed, disputed, refunded and reversed payments.
- [ ] **08.09.08** — Prevent duplicate charge on retry or browser refresh.
- [ ] **08.09.09** — Define subscription renewal, cancellation and grace period behavior.
- [ ] **08.09.10** — Test financial rounding, timezone and currency formatting.
- [ ] **08.09.11** — Prepare customer support/refund workflow and legal review as required.

**Required proof / deliverables**

- [ ] Payment lifecycle state diagram and sandbox results.
- [ ] Verified reconciliation, entitlement and refund scenarios.

**Exit criterion:** Money and access rights remain correct despite retries and provider failures.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

## Release status and go / no-go template

```markdown
# Release Record
Version: [ ] | Source commit/tag: [ ] | Status: NO-GO
Target platform / channel: [ ] | Human release owner: [ ]
- [ ] Approved scope and release-blocking acceptance verified
- [ ] No critical/high unresolved exploit or unapproved release blocker
- [ ] Clean build, artifact integrity/hash and real install/upgrade tested
- [ ] Privacy, data egress, dependencies, licenses and costs reviewed
- [ ] Data backup/migration and rollback tested as applicable
- [ ] Accessibility, performance and compatibility checked
- [ ] Support, changelog, privacy notices and docs accurate
- [ ] Owner/operations/security approvals documented
- [ ] After approval, actual release published and independently verified
Decision / exceptions / approvers & date: [...]
Artifact path/URL/hash: [...] | Live verification: [...]
```

## Living changelog template

```markdown
# Changelog
## [Unreleased]
### Added
- [ ]
### Changed
- [ ]
### Fixed
- [ ]
### Security
- [ ]
## [VERSION] — [YYYY-MM-DD]
- Link to release artifact and verified source commit.
```

## Embedded operations and release templates

### Template — Release Record

```markdown
# Release Record — [version]

**Release date/time/timezone:** [ ]  
**Source commit/tag:** [ ]  
**Artifact/link:** [ ]  
**SHA-256:** [ ]  
**Publisher/signing status:** [ ]

## Gate checks
- [ ] Requirements, UAT and smoke tests PASS.
- [ ] Security scans reviewed; critical issues absent or formally blocked.
- [ ] Real package/installer tested cleanly.
- [ ] Privacy, permissions, licenses and costs reviewed.
- [ ] Backup/migration/rollback verified as applicable.
- [ ] User documentation, support and release notes ready.
- [ ] Human go/no-go recorded.

## Approval
**Product:** [ ]  **Security:** [ ]  **Ops:** [ ]  **Decision:** GO / NO-GO

## Production smoke test
**Actual release URL/location:** [ ]  
**Version observed:** [ ]  
**Test results:** [ ]

## Rollback plan/result
[Trigger, commands, backups, actual outcome]
```

### Template — Incident

```markdown
# Incident — INC-[number]

**Opened:** [ ]  **Severity:** [ ]  **Commander/owner:** [ ]  **Status:** [ ]

## Impact and scope
[Users, data, functions affected; confirmed vs suspected]

## Timeline (with timezone)
- [time] Detection:
- [time] Containment:
- [time] Recovery:

## Evidence (sanitized)
[References only; do not copy secrets]

## Containment and remediation
- [ ] Stop affected functionality safely.
- [ ] Protect evidence and restrict access.
- [ ] Restore critical function and verify data integrity.
- [ ] Notify affected parties when required.

## Root cause and actions
| Action | Owner | Due | Verification |
|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] |
```
