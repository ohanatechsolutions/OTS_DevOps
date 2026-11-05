# 04 — Testing, Security and Quality Assurance

**Purpose:** Prove the actual application works under expected and adverse conditions. Applies throughout development and must be revisited before every release or security-sensitive change.

> **Source-library usage:** These five files are reusable reference material for a ChatGPT Project or other coding AI. They are *not* an application, code repository, evidence of passing tests, or automatically updated project records. Create and maintain project-specific working records in the actual software repository or another explicitly writable workspace. Upload all five to the ChatGPT Project and tell the AI to apply the relevant parts. AI access to a GitHub repository must be connected/authorized separately.
> **Status rule:** These source checkboxes remain reusable templates. In the *writable project tracker*, check an item only after verifying the real project; otherwise record `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, or `N/A — reason`. Small projects can mark genuinely irrelevant work N/A. Never waive safety-critical checks silently.


## Verification matrix (adapt by risk)

| Layer | Proves | Example evidence |
|---|---|---|
| Static/lint/type | Code quality / common mistakes | tool, version, actual output |
| Unit | individual rules and functions | passed + failed count, environment |
| Integration/contract | boundaries and real interfaces | API/database/test-service results |
| End-to-end | user journeys work through the real application | test logs/video/manual trace |
| Negative and abuse | invalid and hostile inputs fail safely | risk-linked negative cases |
| Security/privacy | least privilege, secrets, data egress and vulnerability controls | scoped scans, manual reviews, retests |
| Performance/reliability | realistic load, memory, latency, recovery | measured metrics against targets |
| Accessibility/compatibility | supported devices, assistive tech and environments | matrix, actual device/browser tests |
| Installation/upgrade | deployable user-ready package | clean-install and migration evidence |
| User acceptance | stakeholder verifies business outcomes | signed UAT cases |

**Truthful reporting:** Differentiate `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` and `N/A — reason`. A simulated or mocked run must be labeled as such. Security testing must be authorized and scoped; avoid dangerous or destructive scans without permission.

## Phase 05 — Verification, security and user acceptance

> **Phase gate:** P0/P1 flows and security/compatibility targets are verified with traceable evidence.

**Module index** (use only modules applicable to this project):

- [05.01 — Testing Strategy and Coverage Plan](#0501-testing-strategy-and-coverage-plan) — 12 checks
- [05.02 — Unit, Integration and Contract Testing](#0502-unit-integration-and-contract-testing) — 11 checks
- [05.03 — End-to-End and Regression Testing](#0503-end-to-end-and-regression-testing) — 11 checks
- [05.04 — Security Testing and Abuse Cases](#0504-security-testing-and-abuse-cases) — 12 checks
- [05.05 — Performance, Load, Stress and Reliability Verification](#0505-performance-load-stress-and-reliability-verification) — 11 checks
- [05.06 — Accessibility and Cross-Platform Compatibility QA](#0506-accessibility-and-cross-platform-compatibility-qa) — 11 checks
- [05.07 — Privacy, Legal, License and Compliance Review](#0507-privacy-legal-license-and-compliance-review) — 11 checks
- [05.08 — User Acceptance Testing, Bug Triage and Signoff](#0508-user-acceptance-testing-bug-triage-and-signoff) — 11 checks

### 05.01 — Testing Strategy and Coverage Plan

**When to use:** All software projects. **Goal:** Match test types to risks and launch requirements.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.01.01** — Identify test levels: unit, component, integration, contract, end-to-end and manual.
- [ ] **05.01.02** — Prioritize P0/P1 user journeys and security boundaries.
- [ ] **05.01.03** — Use test IDs linked to requirement IDs.
- [ ] **05.01.04** — Define unit test targets for logic, validation and state transitions.
- [ ] **05.01.05** — Define integration tests across storage and vendor adapters.
- [ ] **05.01.06** — Define end-to-end tests for critical actual workflows.
- [ ] **05.01.07** — Define negative tests for invalid, denied and malicious inputs.
- [ ] **05.01.08** — Define performance, stress, soak and resource tests as relevant.
- [ ] **05.01.09** — Define accessibility and compatibility test devices.
- [ ] **05.01.10** — Create deterministic fixtures and isolated test accounts.
- [ ] **05.01.11** — Define test data lifecycle and no-production-data policy.
- [ ] **05.01.12** — Record pass/fail, environment, command, evidence and known limitations.

**Required proof / deliverables**

- [ ] Risk-based test matrix and test command reference.
- [ ] Test coverage gap list with owners.

**Exit criterion:** All release-blocking risks have defined verification methods.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.02 — Unit, Integration and Contract Testing

**When to use:** All software projects. **Goal:** Verify implementation boundaries with repeatable automation.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.02.01** — Test all nontrivial business rule branches and boundary values.
- [ ] **05.02.02** — Test storage read/write, transactions and migrations.
- [ ] **05.02.03** — Test permission checks for owner/nonowner/admin/anonymous as relevant.
- [ ] **05.02.04** — Test parser and file import/export with malformed files.
- [ ] **05.02.05** — Test serialization, validation and backward compatibility.
- [ ] **05.02.06** — Test external service timeout, quota, invalid response and retries.
- [ ] **05.02.07** — Test event ordering, duplicate requests and idempotency.
- [ ] **05.02.08** — Test time zones, DST, rounding and locale where relevant.
- [ ] **05.02.09** — Eliminate flakiness and test-order dependencies.
- [ ] **05.02.10** — Capture exact local command and pass result.
- [ ] **05.02.11** — Link failing cases to actionable bug records.

**Required proof / deliverables**

- [ ] Passing automated tests and retained test report/evidence.
- [ ] Documented exceptions with risk approval.

**Exit criterion:** Core domain and integration behavior is repeatable and regression-tested.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.03 — End-to-End and Regression Testing

**When to use:** All software projects. **Goal:** Ensure working user outcomes survive changes.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.03.01** — Create P0 smoke test from fresh install/login to completed result.
- [ ] **05.03.02** — Test each major journey against realistic but synthetic data.
- [ ] **05.03.03** — Test new, returning, and unauthorized user experiences.
- [ ] **05.03.04** — Test interrupted workflows, refresh/relaunch and resume.
- [ ] **05.03.05** — Test network unavailable, intermittent and service timeout behavior.
- [ ] **05.03.06** — Test duplicate inputs, large files and long lists.
- [ ] **05.03.07** — Test imports/exports and data integrity end to end.
- [ ] **05.03.08** — Test upgrade from previous supported release.
- [ ] **05.03.09** — Run regression suite after any feature or dependency change.
- [ ] **05.03.10** — Capture screenshots or recordings only with sanitized test data.
- [ ] **05.03.11** — Record environment, exact version, results and reproducible failures.

**Required proof / deliverables**

- [ ] E2E report linked to feature acceptance matrix.
- [ ] Regression baseline and known exception list.

**Exit criterion:** No P0/P1 journey is broken on a supported installation.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.04 — Security Testing and Abuse Cases

**When to use:** All software projects. **Goal:** Challenge assumptions with adversarial verification.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.04.01** — Run code and dependency vulnerability scans appropriate to stack.
- [ ] **05.04.02** — Scan current files and available Git history for exposed secrets.
- [ ] **05.04.03** — Validate auth bypass and direct object reference attacks.
- [ ] **05.04.04** — Test injection, XSS, CSRF, SSRF and traversal where applicable.
- [ ] **05.04.05** — Test upload and archive extraction abuse cases where applicable.
- [ ] **05.04.06** — Test session fixation, expiration, logout and token revocation.
- [ ] **05.04.07** — Test rate limiting and resource exhaustion.
- [ ] **05.04.08** — Review insecure defaults, debug endpoints and exposed management ports.
- [ ] **05.04.09** — Test malware/suspicious file handling safely if product processes untrusted files.
- [ ] **05.04.10** — For agents, test prompt injection and tool misuse using benign adversarial inputs.
- [ ] **05.04.11** — Triage findings, fix critical/high, retest and document residual risk.
- [ ] **05.04.12** — Arrange qualified independent review for high-impact or regulated systems.

**Required proof / deliverables**

- [ ] Findings report with remediation and verification evidence.
- [ ] Signed-off residual risk list and no-open-critical gate.

**Exit criterion:** Known critical exploits are resolved; no prohibited high-risk path remains untested.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.05 — Performance, Load, Stress and Reliability Verification

**When to use:** All software projects. **Goal:** Verify numeric quality claims under representative workload.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.05.01** — Choose representative low/mid/high hardware profiles and test data size.
- [ ] **05.05.02** — Measure cold start, warm start and interactive latency.
- [ ] **05.05.03** — Measure CPU, RAM, GPU, disk, network and battery use where relevant.
- [ ] **05.05.04** — Simulate concurrent users/tasks and define saturation behavior.
- [ ] **05.05.05** — Test large files, datasets and growing histories.
- [ ] **05.05.06** — Test slow networks, storage latency and vendor timeouts.
- [ ] **05.05.07** — Test long-running processes for leaks and stuck workers.
- [ ] **05.05.08** — Test graceful shutdown, crash recovery and resume.
- [ ] **05.05.09** — Verify rate limits and task cancellation bound resource use.
- [ ] **05.05.10** — Compare results against nonfunctional criteria and record test setup.
- [ ] **05.05.11** — Profile and fix proven bottlenecks, avoiding speculative rewrites.

**Required proof / deliverables**

- [ ] Performance results with device, versions, dataset and methodology.
- [ ] Signed-off deviations and capacity assumptions.

**Exit criterion:** Release meets agreed SLO/resource thresholds on supported profiles.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.06 — Accessibility and Cross-Platform Compatibility QA

**When to use:** All software projects. **Goal:** Confirm promised environments actually work.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.06.01** — Build supported-platform matrix with OS/browser/device versions.
- [ ] **05.06.02** — Test clean install, update, launch, normal use and uninstall.
- [ ] **05.06.03** — Test monitor scaling, DPI, zoom and small windows as relevant.
- [ ] **05.06.04** — Test keyboard-only operation across major journeys.
- [ ] **05.06.05** — Test screen-reader names, order and status announcements.
- [ ] **05.06.06** — Verify text contrast and focus indicator standards.
- [ ] **05.06.07** — Check no critical information depends on color alone.
- [ ] **05.06.08** — Check reduced motion, long text and localization overflow.
- [ ] **05.06.09** — Test offline/reconnect behaviors on each relevant platform.
- [ ] **05.06.10** — Test permissions denied, security software restrictions and locked-down user accounts.
- [ ] **05.06.11** — Record actual device/version results and unsupported combinations.

**Required proof / deliverables**

- [ ] Compatibility table and accessibility issue list.
- [ ] Evidence of essential journeys on each declared supported platform.

**Exit criterion:** Compatibility/support claims match tested reality, not developer assumptions.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.07 — Privacy, Legal, License and Compliance Review

**When to use:** All software projects. **Goal:** Verify trust, disclosure and distribution obligations before public release.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.07.01** — Confirm data collection is minimal and matches product claims.
- [ ] **05.07.02** — Test consent, opt-out and local-vs-cloud routing choices.
- [ ] **05.07.03** — Test export, deletion, retention and account removal.
- [ ] **05.07.04** — Check logs, screenshots, analytics and support bundles for sensitive content.
- [ ] **05.07.05** — Verify privacy policy, terms and contact details match actual processing.
- [ ] **05.07.06** — Review open-source dependencies, attribution and asset licenses.
- [ ] **05.07.07** — Check vendor agreements and permitted redistribution.
- [ ] **05.07.08** — Determine applicable privacy, sector and geographic obligations with qualified counsel as needed.
- [ ] **05.07.09** — Validate age/consent requirements where applicable.
- [ ] **05.07.10** — Review regulated claims (security, medical, financial) for evidence and disclaimers.
- [ ] **05.07.11** — Check marketing claims, performance assertions and screenshots for accuracy.

**Required proof / deliverables**

- [ ] Privacy/compliance review matrix and open issues.
- [ ] Approved policies and license notices as applicable.

**Exit criterion:** Product behavior and public claims match documented obligations and evidence.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 05.08 — User Acceptance Testing, Bug Triage and Signoff

**When to use:** All software projects. **Goal:** Separate engineering success from genuine user readiness.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **05.08.01** — Recruit representative reviewers appropriate to launch risk.
- [ ] **05.08.02** — Create test scripts using user goals rather than implementation hints.
- [ ] **05.08.03** — Provide realistic but synthetic test accounts/data.
- [ ] **05.08.04** — Observe whether user completes tasks without AI developer assistance.
- [ ] **05.08.05** — Record usability defects, missing requirements and accessibility barriers.
- [ ] **05.08.06** — Classify bugs as blocker/critical/high/medium/low with reproducible steps.
- [ ] **05.08.07** — Assign owner, target fix and retest method.
- [ ] **05.08.08** — Verify bug fixes against original report and adjacent regressions.
- [ ] **05.08.09** — Record documented workarounds for accepted low-severity bugs.
- [ ] **05.08.10** — Require explicit product and security owner signoff at release gate.
- [ ] **05.08.11** — Create a go/no-go decision with dated evidence.

**Required proof / deliverables**

- [ ] UAT report, triaged defects and release signoff.
- [ ] List of accepted known issues and mitigation.

**Exit criterion:** Stakeholders approve the actual tested product, not just a demo.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

## Embedded QA templates

### Template — Test Case

```markdown
# Test Case: TEST-[number] — [description]

**Requirement:** REQ-___  
**Priority:** P0 / P1 / P2  
**Type:** unit / integration / E2E / security / performance / accessibility / manual

## Preconditions and environment
[OS, build commit, test fixture, permissions]

## Steps
1. [ ] [Action]
2. [ ] [Action]
3. [ ] [Action]

## Expected results
[Observable state, error code, persisted data]

## Actual execution
**Status:** NOT RUN / PASS / FAIL / BLOCKED / N/A  
**Date:** [ ]  
**Verifier:** [ ]  
**Command:** [ ]  
**Evidence:** [ ]

## Cleanup
[Reset synthetic data, revoke ephemeral credentials]
```

### Template — Bug Report

```markdown
# Bug Report: [title]

- **ID:** BUG-___
- **Severity:** blocker / critical / high / medium / low
- **Version, commit, environment:** [ ]
- **Owner / Status:** [ ] / OPEN

## Steps to reproduce
1. [ ]
2. [ ]
3. [ ]

## Expected
[Precise expected result]

## Actual
[Precise observed result; no secrets or personal information]

## Minimal safe reproduction / fixture
[Sample input and prerequisites]

## Evidence
[Sanitized log, screenshot, link]

## Root cause
[Confirmed vs hypothesis]

## Fix and regression test
- [ ] Create a test that fails before fix.
- [ ] Implement smallest safe fix.
- [ ] Run related and regression checks.
- [ ] Record observed result and verifier.
```

### Template — Uat

```markdown
# User Acceptance Session — [feature/release]

**Version/commit:** [ ]  
**Date:** [ ]  
**Reviewer persona:** [ ]

## Scenario
[Real-world goal, sample data, starting conditions]

## Steps/outcomes
- [ ] Reviewer completes setup unaided.
- [ ] Reviewer completes primary task unaided.
- [ ] Reviewer can find and recover from a mistake.
- [ ] Reviewer understands permissions and data sharing.

## Observations
[Exact issues; avoid personal data]

## Result
PASS / FAIL / CONDITIONAL  
**Accepted issues:** [ ]  
**Owner signoff:** [ ]
```
