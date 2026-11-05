# 03 — Engineering Foundations and Implementation

**Purpose:** Create the real repository, reproducible environments and secure build workflow; then deliver every feature as an end-to-end vertical slice. Applies during setup, implementation, integrations, refactoring and code reviews.

> **Source-library usage:** These five files are reusable reference material for a ChatGPT Project or other coding AI. They are *not* an application, code repository, evidence of passing tests, or automatically updated project records. Create and maintain project-specific working records in the actual software repository or another explicitly writable workspace. Upload all five to the ChatGPT Project and tell the AI to apply the relevant parts. AI access to a GitHub repository must be connected/authorized separately.
> **Status rule:** These source checkboxes remain reusable templates. In the *writable project tracker*, check an item only after verifying the real project; otherwise record `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, or `N/A — reason`. Small projects can mark genuinely irrelevant work N/A. Never waive safety-critical checks silently.


## Implementation contract

A feature is **not complete** when a UI button looks correct, a mock response works, a test file merely exists, or a code generator declares success. Complete means the intended user action works from interface/input through authorization, business logic, data persistence (if required), integrations and recoverable output, with representative tests and logged evidence.

1. Confirm requirement ID and definition of done.
2. Reproduce baseline and protect existing changes.
3. Plan smallest complete vertical slice, including error cases and security boundaries.
4. Code with maintainability, bounded external calls, safe secrets handling and meaningful failure modes.
5. Test, review diff, inspect dependency/licenses, document actual results.
6. Update the project's traceability, status, risk/decision records and handoff.

## Phase 03 — Engineering foundations and operations design

> **Phase gate:** Clean-clone setup, coding standards, secrets, dependencies and recovery paths are understood.

**Module index** (use only modules applicable to this project):

- [03.01 — Repository Setup and Reproducible Environment](#0301-repository-setup-and-reproducible-environment) — 12 checks
- [03.02 — Environment Configuration and Secret Management](#0302-environment-configuration-and-secret-management) — 12 checks
- [03.03 — Git Branching, Reviews and Change Control](#0303-git-branching-reviews-and-change-control) — 12 checks
- [03.04 — Dependencies, Licensing and Software Supply Chain](#0304-dependencies-licensing-and-software-supply-chain) — 12 checks
- [03.05 — Coding Conventions and Maintainability](#0305-coding-conventions-and-maintainability) — 12 checks
- [03.06 — Logging, Metrics, Diagnostics and Auditability](#0306-logging-metrics-diagnostics-and-auditability) — 11 checks
- [03.07 — Backups, Recovery, Data Migration and Disaster Readiness](#0307-backups-recovery-data-migration-and-disaster-readiness) — 11 checks
- [03.08 — Cost Controls, Privacy Defaults and Operational Limits](#0308-cost-controls-privacy-defaults-and-operational-limits) — 11 checks

### 03.01 — Repository Setup and Reproducible Environment

**When to use:** All software projects. **Goal:** Establish an installable, auditable starting point.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.01.01** — Inspect existing repository and preserve working functionality.
- [ ] **03.01.02** — Set README, license decision, code owners and contribution guidance.
- [ ] **03.01.03** — Choose one package manager per ecosystem and lock dependencies.
- [ ] **03.01.04** — Define supported runtime, SDK and compiler versions.
- [ ] **03.01.05** — Create documented bootstrap commands for Windows/macOS/Linux as supported.
- [ ] **03.01.06** — Initialize source, tests, docs, scripts and assets structure.
- [ ] **03.01.07** — Configure formatter, linter, type checker and editor defaults.
- [ ] **03.01.08** — Configure .gitignore, .gitattributes and generated artifact policy.
- [ ] **03.01.09** — Add .env.example with fake values, never real secrets.
- [ ] **03.01.10** — Set up local test data and reset/development seed command.
- [ ] **03.01.11** — Verify clean clone installation on a separate environment.
- [ ] **03.01.12** — Record explicit build and launch commands, expected outputs and troubleshooting.

**Required proof / deliverables**

- [ ] Clean-clone quickstart tested with captured commands.
- [ ] Repo tree and environment compatibility documented.

**Exit criterion:** A contributor or coding agent can reproduce a working baseline from scratch.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.02 — Environment Configuration and Secret Management

**When to use:** All software projects. **Goal:** Avoid environment drift and credential leaks.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.02.01** — Define local, test, staging and production environments if used.
- [ ] **03.02.02** — Document variable names, types, defaults and validation rules.
- [ ] **03.02.03** — Keep real credentials out of code, Markdown, fixtures and logs.
- [ ] **03.02.04** — Use OS secret store or approved secrets manager rather than plaintext files.
- [ ] **03.02.05** — Use least-privilege credentials scoped per environment.
- [ ] **03.02.06** — Define secret rotation, revocation and compromise response.
- [ ] **03.02.07** — Prevent production data from being copied into test without approval/anonymization.
- [ ] **03.02.08** — Specify toggles/feature flags with owners and safe defaults.
- [ ] **03.02.09** — Identify environment-specific network addresses and allowed origins.
- [ ] **03.02.10** — Define configuration startup validation and fail-closed behavior.
- [ ] **03.02.11** — Document local-only services, ports and firewall exposure.
- [ ] **03.02.12** — Verify a missing/invalid critical secret yields a safe error.

**Required proof / deliverables**

- [ ] Config matrix and safe `.env.example`.
- [ ] Documented secret access/revocation procedure.

**Exit criterion:** No real secret appears in the repository and environment setup is deterministic.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.03 — Git Branching, Reviews and Change Control

**When to use:** All software projects. **Goal:** Keep AI changes isolated, reviewable and reversible.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.03.01** — Record default branch and whether direct pushes are allowed.
- [ ] **03.03.02** — Prefer small feature/fix branches or isolated working trees.
- [ ] **03.03.03** — Require issue/requirement link for meaningful changes.
- [ ] **03.03.04** — Limit each change set to one coherent objective.
- [ ] **03.03.05** — Check diff, untracked files and unintended deletions before commit.
- [ ] **03.03.06** — Run relevant tests and checks before proposing merge.
- [ ] **03.03.07** — Document review expectations and required human approvals.
- [ ] **03.03.08** — Configure branch protection/rulesets where supported and affordable.
- [ ] **03.03.09** — Define merge method, conflict resolution and branch deletion policy.
- [ ] **03.03.10** — Do not delete branches until merge state and remote are verified.
- [ ] **03.03.11** — Keep generated binaries separate from code history where practical.
- [ ] **03.03.12** — Record release tagging and version naming convention.

**Required proof / deliverables**

- [ ] Documented branch and review policy.
- [ ] At least one trial change demonstrates checks and review workflow.

**Exit criterion:** Main is recoverable and AI work can be reviewed and reverted.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.04 — Dependencies, Licensing and Software Supply Chain

**When to use:** All software projects. **Goal:** Know what runs in the product and whether it may be distributed.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.04.01** — Inventory all direct and transitive dependencies and licenses.
- [ ] **03.04.02** — Verify project/release legitimacy before adopting new packages.
- [ ] **03.04.03** — Use lockfiles and explicit version constraints.
- [ ] **03.04.04** — Run dependency vulnerability scans locally or in approved CI.
- [ ] **03.04.05** — Identify EOL runtimes, abandonware and critical advisories.
- [ ] **03.04.06** — Record third-party API data sharing and recurring costs.
- [ ] **03.04.07** — Track asset/font/icon/media licenses and attribution requirements.
- [ ] **03.04.08** — Review packages with install scripts or postinstall network access.
- [ ] **03.04.09** — Generate SBOM when distribution or risk level warrants it.
- [ ] **03.04.10** — Apply artifact hashes, signatures/provenance when available.
- [ ] **03.04.11** — Document dependency update ownership and regression process.
- [ ] **03.04.12** — Remove unused libraries and forbidden packages.

**Required proof / deliverables**

- [ ] Dependency inventory, license review and unresolved findings.
- [ ] Reproducible dependency install and update policy.

**Exit criterion:** Distribution rights are clear and high-risk dependencies are evaluated.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.05 — Coding Conventions and Maintainability

**When to use:** All software projects. **Goal:** Prevent vibe-coding from producing an unmaintainable monolith.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.05.01** — Set naming, module layout, formatting and documentation conventions.
- [ ] **03.05.02** — Choose type checking/static analysis settings and enforcement scope.
- [ ] **03.05.03** — Define functions and module complexity thresholds or review triggers.
- [ ] **03.05.04** — Use small focused functions, meaningful errors and explicit interfaces.
- [ ] **03.05.05** — Separate UI, domain logic, persistence and integration code.
- [ ] **03.05.06** — Favor simple architecture over speculative abstraction.
- [ ] **03.05.07** — Ban duplicate business rules across frontend/backend.
- [ ] **03.05.08** — Handle exceptions explicitly; avoid silent catch-all success.
- [ ] **03.05.09** — Define logging levels with sensitive-data redaction.
- [ ] **03.05.10** — Write comments for intent/tradeoffs, not obvious syntax.
- [ ] **03.05.11** — Document public APIs and non-obvious algorithms.
- [ ] **03.05.12** — Set policy for generated code, code review and refactoring.

**Required proof / deliverables**

- [ ] Style and architecture conventions with test/lint enforcement.
- [ ] Example module and acceptance of code review standards.

**Exit criterion:** New code is understandable, testable, consistent and reviewable.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.06 — Logging, Metrics, Diagnostics and Auditability

**When to use:** All software projects. **Goal:** Make problems detectable without exposing private information.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.06.01** — Define structured event names and correlation/request IDs.
- [ ] **03.06.02** — Separate user-visible activity history from security audit logs.
- [ ] **03.06.03** — Specify log data minimization, redaction and access controls.
- [ ] **03.06.04** — Define metrics for failure, latency, queue depth and resource use.
- [ ] **03.06.05** — Instrument critical paths and background jobs.
- [ ] **03.06.06** — Create useful error codes and actionable user-facing recovery text.
- [ ] **03.06.07** — Define health/readiness checks for hosted services if applicable.
- [ ] **03.06.08** — Implement crash capture only with consent and privacy controls where appropriate.
- [ ] **03.06.09** — Define log rotation, storage ceilings, retention and deletion.
- [ ] **03.06.10** — Set time synchronization and timezone representation for timestamps.
- [ ] **03.06.11** — Verify alerting and diagnostic workflow in a test scenario.

**Required proof / deliverables**

- [ ] Event/metric catalog and sample sanitized diagnostic record.
- [ ] Evidence that one injected failure is traceable.

**Exit criterion:** A failure can be diagnosed while sensitive information remains protected.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.07 — Backups, Recovery, Data Migration and Disaster Readiness

**When to use:** All software projects. **Goal:** Ensure update or disaster cannot silently destroy user data.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.07.01** — Classify critical persistent state and determine backup frequency.
- [ ] **03.07.02** — Set recovery point/recovery time targets or mark not applicable.
- [ ] **03.07.03** — Choose encrypted backups with separated authorization.
- [ ] **03.07.04** — Ensure backup credentials cannot be abused by the app runtime.
- [ ] **03.07.05** — Define retention, immutability/offline copy and deletion schedules.
- [ ] **03.07.06** — Define export/import data formats and schema versioning.
- [ ] **03.07.07** — Document migration rollback or forward-fix strategy.
- [ ] **03.07.08** — Test interrupted writes, disk-full conditions and corrupt state handling.
- [ ] **03.07.09** — Restore backup into isolated test environment and validate data.
- [ ] **03.07.10** — Test data portability and account/device migration where required.
- [ ] **03.07.11** — Record backup restore operator, required approvals and evidence.

**Required proof / deliverables**

- [ ] Backup and restoration runbooks with tested restore result.
- [ ] Migration and corruption recovery evidence.

**Exit criterion:** A realistic data loss scenario has a verified recovery path.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 03.08 — Cost Controls, Privacy Defaults and Operational Limits

**When to use:** All software projects. **Goal:** Keep AI-generated architecture aligned with budget and consent.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **03.08.01** — List every service that can incur recurring or usage charges.
- [ ] **03.08.02** — Document cost-free/local alternative and tradeoff where possible.
- [ ] **03.08.03** — Define monthly budget ceiling, usage cap and shutdown behavior.
- [ ] **03.08.04** — Do not enable paid CI, API calls or cloud hosts without approval.
- [ ] **03.08.05** — Require opt-in for telemetry, analytics and third-party AI processing as applicable.
- [ ] **03.08.06** — Default to local processing for restricted data when required.
- [ ] **03.08.07** — Set file, queue, rate, concurrency and model token limits.
- [ ] **03.08.08** — Define vendor outage degradation rather than unlimited retries.
- [ ] **03.08.09** — Avoid indefinite retention of prompts, screen contents or personal activity.
- [ ] **03.08.10** — Ensure opt-out actually stops collection and processing.
- [ ] **03.08.11** — Test a quota exhaustion and privacy revocation scenario.

**Required proof / deliverables**

- [ ] Cost/vendor inventory and opt-in matrix.
- [ ] Evidence of quota fallback and data-sharing boundaries.

**Exit criterion:** Costs cannot silently run away and privacy choices are enforceable.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---
## Phase 04 — Implementation and documentation

> **Phase gate:** Each scoped vertical slice is functional, tested and linked to its acceptance criteria.

**Module index** (use only modules applicable to this project):

- [04.01 — Feature-by-Feature Vertical Slice Delivery](#0401-feature-by-feature-vertical-slice-delivery) — 12 checks
- [04.02 — User Interface and Frontend Implementation](#0402-user-interface-and-frontend-implementation) — 12 checks
- [04.03 — Backend, Jobs and Business Logic](#0403-backend-jobs-and-business-logic) — 12 checks
- [04.04 — External Integrations and Automation Connectors](#0404-external-integrations-and-automation-connectors) — 12 checks
- [04.05 — Implement Defensive Controls](#0405-implement-defensive-controls) — 12 checks
- [04.06 — Implementation Documentation and Change Tracking](#0406-implementation-documentation-and-change-tracking) — 11 checks

### 04.01 — Feature-by-Feature Vertical Slice Delivery

**When to use:** All software projects. **Goal:** Deliver complete working behavior rather than disconnected layers.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.01.01** — Select one approved story with priority and requirement IDs.
- [ ] **04.01.02** — Review dependencies, permissions, data flows and acceptance criteria.
- [ ] **04.01.03** — Create a thin implementation plan showing files to change.
- [ ] **04.01.04** — Write/adjust a failing test that expresses the user outcome when practical.
- [ ] **04.01.05** — Implement data model, domain rule, interface and UI path as needed.
- [ ] **04.01.06** — Cover normal, invalid, unauthorized and retry/cancel cases.
- [ ] **04.01.07** — Preserve existing behavior and avoid speculative feature additions.
- [ ] **04.01.08** — Add visible progress and user-readable failure handling.
- [ ] **04.01.09** — Include audit, logging and privacy checks at relevant boundaries.
- [ ] **04.01.10** — Run targeted unit, contract and end-to-end tests.
- [ ] **04.01.11** — Perform manual walkthrough of the whole journey on supported environment.
- [ ] **04.01.12** — Update traceability and status only when evidence is recorded.

**Required proof / deliverables**

- [ ] Working demonstration of the story with commands and evidence.
- [ ] Updated tests, docs and requirement links.

**Exit criterion:** A real user can finish the chosen task from entry to result; no hidden placeholder paths.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 04.02 — User Interface and Frontend Implementation

**When to use:** All software projects. **Goal:** Build usable, accessible stateful UI, not a static mockup.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.02.01** — Use approved design tokens, components and navigation.
- [ ] **04.02.02** — Connect all buttons, menus and inputs to real behavior.
- [ ] **04.02.03** — Implement validation, pending, empty, success and error states.
- [ ] **04.02.04** — Implement data fetching, caching and stale data indications.
- [ ] **04.02.05** — Protect unsaved changes and provide cancellation/undo where feasible.
- [ ] **04.02.06** — Handle loading races, double clicks and repeated submissions.
- [ ] **04.02.07** — Avoid exposing secrets or sensitive data to client bundles.
- [ ] **04.02.08** — Validate role restrictions on server, not only by hiding UI.
- [ ] **04.02.09** — Support keyboard interaction, focus management and screen readers.
- [ ] **04.02.10** — Test responsive sizes, content overflow and long text.
- [ ] **04.02.11** — Write component tests and capture key UI regression baselines.
- [ ] **04.02.12** — Verify external links, downloads, permissions and navigation.

**Required proof / deliverables**

- [ ] Screens with functional controls, tests and responsive checks.
- [ ] Evidence for empty/error/permission states.

**Exit criterion:** There are no decorative controls misrepresented as completed features.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 04.03 — Backend, Jobs and Business Logic

**When to use:** All software projects. **Goal:** Implement reliable processing with explicit security boundaries.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.03.01** — Define input schema and reject invalid/unexpected fields.
- [ ] **04.03.02** — Authenticate requests and enforce authorization on every resource.
- [ ] **04.03.03** — Separate business logic from framework and persistence adapters.
- [ ] **04.03.04** — Use transactions and concurrency guards for multi-step state changes.
- [ ] **04.03.05** — Make retried operations idempotent where necessary.
- [ ] **04.03.06** — Implement timeouts, bounded retries and partial failure handling.
- [ ] **04.03.07** — Use background workers for long tasks with status and cancellation.
- [ ] **04.03.08** — Control resource exhaustion and third-party usage limits.
- [ ] **04.03.09** — Never trust browser-supplied roles, prices, owners or workflow states.
- [ ] **04.03.10** — Implement consistent error types and sanitized logs.
- [ ] **04.03.11** — Test logic, authorization, race conditions and external failures.
- [ ] **04.03.12** — Document operators' recovery steps for stuck jobs.

**Required proof / deliverables**

- [ ] Verified endpoint/job behavior and negative test results.
- [ ] Operational notes for retries and stuck work.

**Exit criterion:** Business operations are safe under bad inputs, retries, concurrency and access violations.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 04.04 — External Integrations and Automation Connectors

**When to use:** All software projects. **Goal:** Make vendor boundaries reliable, affordable and revocable.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.04.01** — Inventory permissions/scopes and use least privilege.
- [ ] **04.04.02** — Check platform API terms, request quotas and cost before activating.
- [ ] **04.04.03** — Create isolated adapter per provider with stable internal interface.
- [ ] **04.04.04** — Store tokens in approved secrets store and plan refresh/revocation.
- [ ] **04.04.05** — Use explicit user approval before sending/publishing/deleting externally.
- [ ] **04.04.06** — Validate provider responses and sanitize untrusted fields.
- [ ] **04.04.07** — Handle rate limits, webhooks, outages and schema changes.
- [ ] **04.04.08** — Add bounded retries with backoff and dead-letter/recovery path.
- [ ] **04.04.09** — Avoid duplicating effects on retry with idempotency or dedupe keys.
- [ ] **04.04.10** — Provide a disconnect/revoke option and stop new processing after revocation.
- [ ] **04.04.11** — Mock integration in tests and use sandbox/staging account first.
- [ ] **04.04.12** — Record data egress, permissions and failure modes.

**Required proof / deliverables**

- [ ] Integration capability matrix with permission and cost notes.
- [ ] Sandbox test evidence for success, denial and outage.

**Exit criterion:** Integration succeeds, safely degrades and can be revoked without data leakage.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 04.05 — Implement Defensive Controls

**When to use:** All software projects. **Goal:** Put security decisions into code and validate their effectiveness.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.05.01** — Implement identity verification and secure session management where applicable.
- [ ] **04.05.02** — Enforce least-privilege roles at every data and action boundary.
- [ ] **04.05.03** — Use established password/token mechanisms rather than invented cryptography.
- [ ] **04.05.04** — Prevent injection with parameterized queries and context-aware encoding.
- [ ] **04.05.05** — Apply CSRF defenses to state-changing browser requests where applicable.
- [ ] **04.05.06** — Apply safe upload validation, limits and quarantining where warranted.
- [ ] **04.05.07** — Enforce origin, CORS and Content Security Policy as applicable.
- [ ] **04.05.08** — Harden headers, redirects, cookies and TLS configuration.
- [ ] **04.05.09** — Define secrets handling and rotation hooks.
- [ ] **04.05.10** — Limit abusive requests, file sizes and expensive job execution.
- [ ] **04.05.11** — Ensure no private data appears in errors, analytics or logs.
- [ ] **04.05.12** — Test access violations and malicious input before marking complete.

**Required proof / deliverables**

- [ ] Security control mapping to threat IDs and test evidence.
- [ ] Document exceptions and approved residual risks.

**Exit criterion:** Controls are verified with negative tests, not merely documented.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 04.06 — Implementation Documentation and Change Tracking

**When to use:** All software projects. **Goal:** Keep documentation synchronized as AI iterates rapidly.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **04.06.01** — Update affected docs in the same change as code.
- [ ] **04.06.02** — Record new environment variables and startup commands.
- [ ] **04.06.03** — Record new or modified public interfaces.
- [ ] **04.06.04** — Update schemas, migration and backup instructions.
- [ ] **04.06.05** — Update requirement traceability and test mappings.
- [ ] **04.06.06** — Record ADR when design materially changes.
- [ ] **04.06.07** — Add a concise changelog entry for user-visible behavior.
- [ ] **04.06.08** — Update known issues and technical debt with priority.
- [ ] **04.06.09** — Verify that referenced paths and commands exist.
- [ ] **04.06.10** — Include example input/output for complex modules.
- [ ] **04.06.11** — Produce handoff notes with current branch and uncommitted changes.

**Required proof / deliverables**

- [ ] Consistent docs and changelog with each completed slice.
- [ ] Handoff sufficient for another agent to resume safely.

**Exit criterion:** No essential implementation knowledge lives only in chat history.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

## Embedded delivery and code-review templates

### Template — Feature Task

```markdown
# Feature / Task: [title]

- **ID:** TASK-___
- **Requirement / Story:** REQ-___ / STORY-___
- **Priority:** P0 / P1 / P2
- **Owner / Reviewer:** [ ] / [ ]
- **Status:** NOT STARTED / IN PROGRESS / BLOCKED / VERIFIED

## User outcome
As a [role], I want [capability], so that [benefit].

## Acceptance criteria
- [ ] Given [state], when [action], then [observable result].
- [ ] Invalid and unauthorized inputs fail safely.
- [ ] Retry/cancel/undo behavior is defined where relevant.

## Constraints / dependencies
[Relevant PRD, design, architecture, risk, cost, permissions and security links.]

## Proposed files and plan
1. [Small change]
2. [Small change]
3. [Relevant tests]

## Tests and evidence
| Check | Command/environment | Actual result | Evidence link |
|---|---|---|---|
| Unit | NOT RUN | NOT RUN | — |
| Integration | NOT RUN | NOT RUN | — |
| Manual flow | NOT RUN | NOT RUN | — |

## Human signoff
[Reviewer, date, pass/fail, known exceptions]
```

### Template — Change Request

```markdown
# Change Request — CR-[number]

**Requested by/date:** [ ]  **Status:** PROPOSED  **Target version:** [ ]

## Requested change and business case
[Observable behavior requested]

## Impact analysis
- [ ] PRD and acceptance criteria
- [ ] UI / workflows / accessibility
- [ ] Architecture, schemas and APIs
- [ ] Auth, security, privacy and compliance
- [ ] Hosting, dependencies, costs and permissions
- [ ] Tests, migrations, documentation and rollback

## Alternatives and recommendation
[Keep / defer / reject; rationale]

## Approval and result
[Decision owner, date, implementation evidence]
```

### Template — Pr Review

```markdown
# Pull Request / Change Review — [title]

**Issue/requirement:** [ ]  **Branch:** [ ]  **Commit(s):** [ ]

## What changed and why
[ ]

## Review checklist
- [ ] Scope matches approved task; no unrelated edits.
- [ ] Correctness, edge states and error handling reviewed.
- [ ] Auth, privacy, secrets and untrusted input reviewed.
- [ ] Tests added/updated and executed with real result.
- [ ] Accessibility and performance impact considered.
- [ ] Data schema, migration and compatibility considered.
- [ ] Documentation/changelog/status updated.
- [ ] User approval needed for any high-risk action was obtained.

## Evidence
[Commands, logs and links]

## Merge decision
APPROVE / CHANGES REQUIRED / BLOCKED  
**Reviewer/date:** [ ]
```
