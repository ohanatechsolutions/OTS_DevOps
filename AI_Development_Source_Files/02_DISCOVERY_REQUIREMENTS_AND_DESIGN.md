# 02 — Discovery, Requirements and Design

**Purpose:** Turn an idea into an implementable, testable product specification and architecture. Covers user research, scope, requirements, privacy/data inventory, UX/UI, APIs, persistence and threat modeling. Read before major new features and whenever requirements or architecture change.

> **Source-library usage:** These five files are reusable reference material for a ChatGPT Project or other coding AI. They are *not* an application, code repository, evidence of passing tests, or automatically updated project records. Create and maintain project-specific working records in the actual software repository or another explicitly writable workspace. Upload all five to the ChatGPT Project and tell the AI to apply the relevant parts. AI access to a GitHub repository must be connected/authorized separately.
> **Status rule:** These source checkboxes remain reusable templates. In the *writable project tracker*, check an item only after verifying the real project; otherwise record `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, or `N/A — reason`. Small projects can mark genuinely irrelevant work N/A. Never waive safety-critical checks silently.


## Decision sequence

1. **What problem and for whom?** Confirm user value, constraints and a measurable outcome.
2. **What is in v1?** Define explicit must-have, later and out-of-scope requirements.
3. **How will success be verified?** Write user journeys, negative cases, measurable quality targets and a traceability matrix.
4. **What architecture is justified?** Select the simplest viable platform, data and permission model; document assumptions and tradeoffs.
5. **Can it fail safely?** Threat model data flows, authorization and privacy before building integrations.

**IDs:** Use `REQ-###` for requirements, `STORY-###` for stories, `ADR-###` for decisions, `TH-###` for threats and `TEST-###` for tests. Link each high-risk requirement to a test and evidence ID in the actual repo.

## Phase 00 — Discovery, feasibility and scope

> **Phase gate:** Problem, users, v1 scope, feasibility, costs, owners and risks accepted.

**Module index** (use only modules applicable to this project):

- [00.01 — Vision, Problem and Project Charter](#0001-vision-problem-and-project-charter) — 12 checks
- [00.02 — Users, Personas and Workflow Research](#0002-users-personas-and-workflow-research) — 12 checks
- [00.03 — Feasibility, Cost and Build-vs-Buy](#0003-feasibility-cost-and-build-vs-buy) — 13 checks
- [00.04 — MVP Scope, Prioritization and Roadmap](#0004-mvp-scope-prioritization-and-roadmap) — 12 checks
- [00.05 — Risk Register, Ownership and Approvals](#0005-risk-register-ownership-and-approvals) — 11 checks

### 00.01 — Vision, Problem and Project Charter

**When to use:** All software projects. **Goal:** Prove why the product should exist before asking AI to code.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **00.01.01** — Write the product name, version target, purpose and one-sentence promise.
- [ ] **00.01.02** — Describe the real problem with concrete examples rather than proposed technology.
- [ ] **00.01.03** — Name primary users, buyers, operators and administrators separately.
- [ ] **00.01.04** — Describe the current manual workflow and why it is inadequate.
- [ ] **00.01.05** — Record desired outcome, measurable benefit and baseline if known.
- [ ] **00.01.06** — List explicit non-goals and features intentionally excluded.
- [ ] **00.01.07** — Set target platforms, supported locales and distribution model.
- [ ] **00.01.08** — Record business owner, technical owner and final sign-off authority.
- [ ] **00.01.09** — Define success metrics and measurable launch criteria.
- [ ] **00.01.10** — Identify known risks, assumptions, dependencies and failure modes.
- [ ] **00.01.11** — Decide whether the product is internal, commercial, open-source or experimental.
- [ ] **00.01.12** — Record whether paid APIs, cloud hosts or subscriptions are prohibited.

**Required proof / deliverables**

- [ ] Complete `PROJECT_BRIEF.md` and link to supporting evidence.
- [ ] Capture approved product promise and project owner sign-off.

**Exit criterion:** Problem, audience, goals and exclusions are clear enough that two developers would build essentially the same MVP.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 00.02 — Users, Personas and Workflow Research

**When to use:** All software projects. **Goal:** Anchor scope to real workflows and access needs.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **00.02.01** — Identify user segments and the jobs each needs completed.
- [ ] **00.02.02** — Distinguish users, purchasers, technical operators and support contacts.
- [ ] **00.02.03** — Gather real examples, interviews or observed tasks where feasible.
- [ ] **00.02.04** — Record top frustrations, workarounds and frequency of each pain point.
- [ ] **00.02.05** — Map current user journey from trigger to result.
- [ ] **00.02.06** — Identify novice, power-user and accessibility needs.
- [ ] **00.02.07** — Record typical devices, network quality and environmental constraints.
- [ ] **00.02.08** — Identify potentially vulnerable users and foreseeable misuse.
- [ ] **00.02.09** — List roles and what each role can see, edit, export or delete.
- [ ] **00.02.10** — Prioritize needs by frequency, business impact and severity.
- [ ] **00.02.11** — Validate draft workflow with at least one representative stakeholder or note evidence unavailable.
- [ ] **00.02.12** — Mark assumptions still requiring user validation.

**Required proof / deliverables**

- [ ] Personas/jobs-to-be-done and current-state workflow documented.
- [ ] Research sources, dates and uncertainties logged.

**Exit criterion:** User needs, roles and top workflows are justified rather than invented.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 00.03 — Feasibility, Cost and Build-vs-Buy

**When to use:** All software projects. **Goal:** Check that the solution is practical within real constraints.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **00.03.01** — Inventory required capabilities and identify existing libraries or services.
- [ ] **00.03.02** — Compare build, integrate, outsource and omit for major components.
- [ ] **00.03.03** — Research platform limitations, permissions and distribution rules.
- [ ] **00.03.04** — Check compatibility with target OS versions, browsers and hardware.
- [ ] **00.03.05** — Estimate CPU, RAM, GPU, disk, bandwidth and battery needs.
- [ ] **00.03.06** — Estimate development, hosting, license, maintenance and support costs separately.
- [ ] **00.03.07** — Define a recurring-cost ceiling and alerts or a zero-spend policy.
- [ ] **00.03.08** — Document external vendor limits, rate caps and outage dependencies.
- [ ] **00.03.09** — Review SDK licenses, security posture and maintenance activity.
- [ ] **00.03.10** — Prototype the highest-uncertainty technical assumption with a disposable spike.
- [ ] **00.03.11** — Record legal, data residency and regulated-domain concerns for qualified review.
- [ ] **00.03.12** — Estimate initial support burden and who will fulfill it.
- [ ] **00.03.13** — List constraints that require a product redesign.

**Required proof / deliverables**

- [ ] Feasibility decision, cost model and dependency shortlist recorded.
- [ ] Spike results captured with commands, artifacts and limitations.

**Exit criterion:** No critical feasibility assumption remains unsupported or hidden.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 00.04 — MVP Scope, Prioritization and Roadmap

**When to use:** All software projects. **Goal:** Avoid endless feature expansion and premature polish.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **00.04.01** — Group ideas into Must, Should, Could and Won't (for this release).
- [ ] **00.04.02** — Identify the smallest end-to-end user outcome delivering value.
- [ ] **00.04.03** — Write a feature inventory with unique IDs (F-001 etc.).
- [ ] **00.04.04** — Rank features by value, effort, risk and dependency.
- [ ] **00.04.05** — Record v1 inclusions and explicit exclusions.
- [ ] **00.04.06** — Break the MVP into testable vertical slices rather than UI-only milestones.
- [ ] **00.04.07** — Define a milestone order that tests the highest risks early.
- [ ] **00.04.08** — Set a capacity and timeline assumption, without making a delivery promise.
- [ ] **00.04.09** — Separate demo readiness, beta readiness and production readiness.
- [ ] **00.04.10** — Set scope-change criteria and an approval process.
- [ ] **00.04.11** — Track deferred items in backlog, not as half-implemented features.
- [ ] **00.04.12** — Confirm launch cutline with product owner.

**Required proof / deliverables**

- [ ] Approved MVP feature table and prioritized roadmap.
- [ ] Explicit out-of-scope list and change-control rule.

**Exit criterion:** MVP is bounded, coherent and demonstrable by a real user.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 00.05 — Risk Register, Ownership and Approvals

**When to use:** All software projects. **Goal:** Establish governance before automation makes irreversible choices.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **00.05.01** — Create risk IDs (R-001 etc.) with likelihood, impact and owner.
- [ ] **00.05.02** — Separate product, security, privacy, compliance, reliability and commercial risks.
- [ ] **00.05.03** — Define severity criteria and acceptable residual risk.
- [ ] **00.05.04** — Name decision maker for architecture, security, product and release.
- [ ] **00.05.05** — Define actions requiring human approval: spend, delete, publish, email, deploy, permissions.
- [ ] **00.05.06** — Specify stop-work criteria for exposed secrets, data loss and critical vulnerabilities.
- [ ] **00.05.07** — Record required third-party/legal review where applicable.
- [ ] **00.05.08** — Define escalation path for blocked AI tasks or unresolved disagreements.
- [ ] **00.05.09** — Document data ownership, intellectual property and third-party obligations.
- [ ] **00.05.10** — Create a decision log and record rejected alternatives with rationale.
- [ ] **00.05.11** — Set review cadence for stale assumptions and risk treatment.

**Required proof / deliverables**

- [ ] the project risk register (template in File 01) initialized.
- [ ] Approval owners and no-go conditions documented.

**Exit criterion:** The agent and human know who can authorize which classes of action.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---
## Phase 01 — Product requirements and traceability

> **Phase gate:** Every in-scope feature and critical nonfunctional target has testable acceptance criteria.

**Module index** (use only modules applicable to this project):

- [01.01 — Product Requirements Document (PRD)](#0101-product-requirements-document-prd) — 12 checks
- [01.02 — User Stories and End-to-End Journeys](#0102-user-stories-and-end-to-end-journeys) — 11 checks
- [01.03 — Functional Specification and Business Rules](#0103-functional-specification-and-business-rules) — 13 checks
- [01.04 — Nonfunctional Requirements and Service Levels](#0104-nonfunctional-requirements-and-service-levels) — 13 checks
- [01.05 — Data Inventory, Classification and Lifecycle](#0105-data-inventory-classification-and-lifecycle) — 13 checks
- [01.06 — Requirements-to-Tests Traceability](#0106-requirements-to-tests-traceability) — 10 checks

### 01.01 — Product Requirements Document (PRD)

**When to use:** All software projects. **Goal:** Translate the approved idea into testable product behavior.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.01.01** — State product goal, users, platform, scope and release version.
- [ ] **01.01.02** — List every MVP feature by ID with why it matters.
- [ ] **01.01.03** — Define workflows: entry, success, failure, cancel and retry.
- [ ] **01.01.04** — Describe all screens, commands or endpoints required by each feature.
- [ ] **01.01.05** — List inputs, outputs, defaults, constraints and edge conditions.
- [ ] **01.01.06** — Define roles, permissions and feature visibility.
- [ ] **01.01.07** — Document external integrations and degraded/offline behavior.
- [ ] **01.01.08** — Specify error messages and recovery actions, not just happy paths.
- [ ] **01.01.09** — Describe onboarding, first-run setup and uninstall/account deletion.
- [ ] **01.01.10** — Define acceptance criteria per feature using observable outcomes.
- [ ] **01.01.11** — Trace each requirement to a milestone and planned test.
- [ ] **01.01.12** — Identify open questions rather than letting AI guess answers.

**Required proof / deliverables**

- [ ] Approved PRD, feature IDs and acceptance criteria.
- [ ] Link from `PROJECT_BRIEF.md` to this PRD.

**Exit criterion:** Every MVP feature has a specific observable definition of done.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 01.02 — User Stories and End-to-End Journeys

**When to use:** All software projects. **Goal:** Specify how users achieve outcomes, not isolated screens.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.02.01** — Write each story as role + goal + reason.
- [ ] **01.02.02** — Add unique story IDs and link them to feature IDs.
- [ ] **01.02.03** — Specify prerequisites, permission requirements and setup steps.
- [ ] **01.02.04** — Capture main flow with numbered user/system actions.
- [ ] **01.02.05** — Capture alternative flows, errors, cancellations and timeouts.
- [ ] **01.02.06** — Define loading, empty, invalid, partial success and denied states.
- [ ] **01.02.07** — Define how users return to or undo a previous step.
- [ ] **01.02.08** — Include accessibility and keyboard-only paths when relevant.
- [ ] **01.02.09** — Include privacy notices and approvals within the actual flow.
- [ ] **01.02.10** — Add concrete acceptance examples and data fixtures.
- [ ] **01.02.11** — Have a human walk the journey for gaps.

**Required proof / deliverables**

- [ ] User story table with acceptance scenarios and trace links.
- [ ] Journey map or ordered flow, with exceptions.

**Exit criterion:** Stories can be implemented and verified without asking what success means.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 01.03 — Functional Specification and Business Rules

**When to use:** All software projects. **Goal:** Make calculations, workflow decisions and state transitions unambiguous.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.03.01** — Describe domain entities and glossary of business terms.
- [ ] **01.03.02** — State validation rules, thresholds, allowed values and units.
- [ ] **01.03.03** — Define permissions and ownership checks for every operation.
- [ ] **01.03.04** — Specify input normalization, deduplication and conflict resolution.
- [ ] **01.03.05** — Write state machine transitions and forbidden transitions.
- [ ] **01.03.06** — Define time zone, date, currency, rounding and localization logic.
- [ ] **01.03.07** — Define file import, export, parsing and encoding behavior.
- [ ] **01.03.08** — Specify idempotency and duplicate request behavior.
- [ ] **01.03.09** — Define external integration retries, timeout and failure rules.
- [ ] **01.03.10** — Define notification conditions, channels and user preferences.
- [ ] **01.03.11** — Specify audit events and retention requirements.
- [ ] **01.03.12** — Write examples for nontrivial formulas and edge cases.
- [ ] **01.03.13** — Tie each rule to an automated test ID.

**Required proof / deliverables**

- [ ] Reviewed rules catalog and transition diagrams/tables.
- [ ] Examples available as test fixtures.

**Exit criterion:** A developer could implement and test business logic without inventing missing rules.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 01.04 — Nonfunctional Requirements and Service Levels

**When to use:** All software projects. **Goal:** Define what acceptable quality means in measurable terms.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.04.01** — Set target startup and interactive response thresholds with devices measured.
- [ ] **01.04.02** — Set throughput, concurrency, background work and queue limits.
- [ ] **01.04.03** — Set RAM, CPU, disk, storage growth and power budgets if relevant.
- [ ] **01.04.04** — Define availability objective and planned maintenance window if hosted.
- [ ] **01.04.05** — Define recovery time and recovery point targets where data persists.
- [ ] **01.04.06** — Set data integrity and consistency requirements.
- [ ] **01.04.07** — Define authentication, authorization, encryption and audit requirements.
- [ ] **01.04.08** — Set offline, poor-network and reconnect expectations.
- [ ] **01.04.09** — Set supported browsers, operating systems, screen sizes and locales.
- [ ] **01.04.10** — Set accessibility target (e.g., WCAG 2.2 AA where applicable).
- [ ] **01.04.11** — Define observability and privacy-safe diagnostic requirements.
- [ ] **01.04.12** — Define retention, deletion, export and migration requirements.
- [ ] **01.04.13** — Record cost and vendor usage ceilings.

**Required proof / deliverables**

- [ ] Numeric or otherwise verifiable nonfunctional criteria.
- [ ] Measurement and verification method beside each criterion.

**Exit criterion:** Every nonfunctional promise is testable or explicitly labeled aspirational.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 01.05 — Data Inventory, Classification and Lifecycle

**When to use:** All software projects. **Goal:** Protect information before selecting storage and AI providers.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.05.01** — Inventory every collected, generated, imported and transmitted field.
- [ ] **01.05.02** — Classify data as public, internal, confidential or restricted.
- [ ] **01.05.03** — Mark personal, credential, financial, health and regulated data.
- [ ] **01.05.04** — Record purpose and lawful basis where legally applicable.
- [ ] **01.05.05** — Minimize collection; justify every sensitive field.
- [ ] **01.05.06** — Define source, owner, access roles, storage location and destination.
- [ ] **01.05.07** — Define encryption at rest/in transit and key custody for each sensitive class.
- [ ] **01.05.08** — Map local versus cloud processing and external AI exposure rules.
- [ ] **01.05.09** — Define retention and secure deletion or anonymization behavior.
- [ ] **01.05.10** — Define backup inclusion, backup retention and restore authorization.
- [ ] **01.05.11** — Specify export, correction, account removal and consent flows.
- [ ] **01.05.12** — Define diagnostic log redaction and support-access controls.
- [ ] **01.05.13** — Review third-party data processing terms and cross-border concerns.

**Required proof / deliverables**

- [ ] Data flow diagram, inventory table and retention schedule.
- [ ] Approved sensitive-data handling and cloud-routing policy.

**Exit criterion:** Every sensitive data class has an approved purpose, store, destination, owner and deletion path.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 01.06 — Requirements-to-Tests Traceability

**When to use:** All software projects. **Goal:** Prevent polished interfaces hiding missing functionality.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **01.06.01** — Assign stable IDs to functional requirements (REQ-001 etc.).
- [ ] **01.06.02** — Map requirement to feature, story and owner.
- [ ] **01.06.03** — Map each requirement to implementing module/file after coding.
- [ ] **01.06.04** — Map each requirement to unit, integration or end-to-end test IDs.
- [ ] **01.06.05** — Record test execution result, evidence link and date.
- [ ] **01.06.06** — Track dependencies and upstream decisions explicitly.
- [ ] **01.06.07** — Show untested and unimplemented requirements as gaps.
- [ ] **01.06.08** — Flag changed requirements for impact review and regression tests.
- [ ] **01.06.09** — Record N/A exclusions with rationale and sign-off.
- [ ] **01.06.10** — Generate launch coverage and unresolved critical gap lists.

**Required proof / deliverables**

- [ ] Maintained coverage matrix in this file or linked project table.
- [ ] All P0/P1 requirements have test evidence before launch.

**Exit criterion:** No critical accepted requirement is missing implementation and a passing verification path.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---
## Phase 02 — UX, architecture and threat modeling

> **Phase gate:** Navigation, architecture, data model, permissions, interfaces and key risks are reviewed.

**Module index** (use only modules applicable to this project):

- [02.01 — Information Architecture and Navigation](#0201-information-architecture-and-navigation) — 11 checks
- [02.02 — UX Flows, Wireframes and Interaction States](#0202-ux-flows-wireframes-and-interaction-states) — 12 checks
- [02.03 — Visual Design System and UI Components](#0203-visual-design-system-and-ui-components) — 12 checks
- [02.04 — Accessibility, Internationalization and Inclusive UX](#0204-accessibility-internationalization-and-inclusive-ux) — 13 checks
- [02.05 — System Architecture and Component Boundaries](#0205-system-architecture-and-component-boundaries) — 13 checks
- [02.06 — Data Model, Storage and Migrations](#0206-data-model-storage-and-migrations) — 13 checks
- [02.07 — API, Events, Files and Integration Contracts](#0207-api-events-files-and-integration-contracts) — 12 checks
- [02.08 — Threat Modeling and Security Architecture](#0208-threat-modeling-and-security-architecture) — 12 checks
- [02.09 — Architecture Decision Records (ADRs)](#0209-architecture-decision-records-adrs) — 9 checks

### 02.01 — Information Architecture and Navigation

**When to use:** All software projects. **Goal:** Define how users find capabilities and understand state.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.01.01** — Inventory screens, routes, dialogs, command groups and system states.
- [ ] **02.01.02** — Create navigation tree from real user journeys.
- [ ] **02.01.03** — Define default landing view and first-use path.
- [ ] **02.01.04** — Define search, filters, sorting, pagination and selection behavior.
- [ ] **02.01.05** — Design empty/loading/error/permission/maintenance states.
- [ ] **02.01.06** — Specify breadcrumbs, back actions and deep-link behavior.
- [ ] **02.01.07** — Specify session timeout and unsaved-work warnings.
- [ ] **02.01.08** — Define role-based visibility and authorization independently.
- [ ] **02.01.09** — Specify keyboard shortcuts with conflicts and discovery.
- [ ] **02.01.10** — Review cognitive complexity and reduce unnecessary steps.
- [ ] **02.01.11** — Validate labels with users rather than internal engineering terminology.

**Required proof / deliverables**

- [ ] Screen/route inventory and navigation map.
- [ ] Every critical journey has an approved entry and exit.

**Exit criterion:** Primary flows are discoverable and no screen is functionally orphaned.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.02 — UX Flows, Wireframes and Interaction States

**When to use:** All software projects. **Goal:** Design interaction before implementation and account for failures.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.02.01** — Sketch each P0 flow and its success state.
- [ ] **02.02.02** — Annotate primary and secondary actions per screen.
- [ ] **02.02.03** — Design confirmations for destructive, expensive and external actions.
- [ ] **02.02.04** — Show progress, cancellation and retry for long-running tasks.
- [ ] **02.02.05** — Specify autosave, manual save and unsaved changes behavior.
- [ ] **02.02.06** — Specify validation timing and useful field-level errors.
- [ ] **02.02.07** — Define permission request timing and denial fallback.
- [ ] **02.02.08** — Show loading, skeleton, zero-results and partial-data states.
- [ ] **02.02.09** — Design responsive layouts and touch targets where relevant.
- [ ] **02.02.10** — Define focus movement and modal exit behavior.
- [ ] **02.02.11** — Test representative workflows with a clickable prototype or walkthrough.
- [ ] **02.02.12** — Record decisions and unresolved usability issues.

**Required proof / deliverables**

- [ ] Reviewed wireframes or text-described layouts with screen IDs.
- [ ] State inventory attached to screen IDs.

**Exit criterion:** All P0 workflows and error states are specified before UI coding.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.03 — Visual Design System and UI Components

**When to use:** All software projects. **Goal:** Give the AI stable styling rules and component contracts.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.03.01** — Define typography, spacing scale, color tokens and elevations.
- [ ] **02.03.02** — Specify light/dark themes, contrast and color semantics.
- [ ] **02.03.03** — Specify minimum window/view sizes and responsive breakpoints.
- [ ] **02.03.04** — Define component anatomy and variants: buttons, inputs, tables, dialogs.
- [ ] **02.03.05** — Define icon sources, sizes, licensing and accessible names.
- [ ] **02.03.06** — Define focus, hover, pressed, disabled, error and success states.
- [ ] **02.03.07** — Specify density and text truncation/wrapping behavior.
- [ ] **02.03.08** — Define consistent empty/loading/error/success illustrations or patterns.
- [ ] **02.03.09** — Document layout grids, padding, alignment and overflow.
- [ ] **02.03.10** — Create reusable component API/props rather than duplicate UI.
- [ ] **02.03.11** — Approve reference screens and regression screenshot baseline.
- [ ] **02.03.12** — Prevent styling-only components from hiding incomplete functionality.

**Required proof / deliverables**

- [ ] Design tokens and component inventory.
- [ ] Reviewed UI sample/reference and state examples.

**Exit criterion:** Every new component has a consistent reusable specification.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.04 — Accessibility, Internationalization and Inclusive UX

**When to use:** All software projects. **Goal:** Make product usable across abilities, languages and locales.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.04.01** — Determine accessibility target and relevant legal requirements.
- [ ] **02.04.02** — Ensure semantic labels, roles, headings and meaningful control names.
- [ ] **02.04.03** — Test keyboard-only access and visible focus order.
- [ ] **02.04.04** — Avoid keyboard traps; provide escape/close paths.
- [ ] **02.04.05** — Check text and non-text contrast against chosen target.
- [ ] **02.04.06** — Support zoom, text resizing, reflow and reduced motion.
- [ ] **02.04.07** — Provide status updates readable by assistive technology.
- [ ] **02.04.08** — Give errors clear causes and actionable fixes.
- [ ] **02.04.09** — Support captions/transcripts for essential media when relevant.
- [ ] **02.04.10** — Externalize strings and avoid text in images where feasible.
- [ ] **02.04.11** — Format dates, numbers, currency, pluralization and time zones correctly.
- [ ] **02.04.12** — Test longer translated strings and right-to-left layouts if supported.
- [ ] **02.04.13** — Test with at least one screen reader or relevant accessibility tool.

**Required proof / deliverables**

- [ ] Accessibility audit results and known gaps.
- [ ] Locale policy and string inventory.

**Exit criterion:** Core journeys can be completed with supported assistive input and target locales.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.05 — System Architecture and Component Boundaries

**When to use:** All software projects. **Goal:** Choose a maintainable architecture with explicit trust boundaries.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.05.01** — Draw system context: users, services, data stores and external providers.
- [ ] **02.05.02** — Identify frontend, backend, workers, databases and optional local agents.
- [ ] **02.05.03** — Draw data and control flow across component boundaries.
- [ ] **02.05.04** — Specify local/cloud split and trust boundary for each call.
- [ ] **02.05.05** — Select technology stack with rationale and supported versions.
- [ ] **02.05.06** — Choose modular boundaries and dependency direction.
- [ ] **02.05.07** — Define contracts for background jobs, events and message queues.
- [ ] **02.05.08** — Define failure isolation, retry budgets, circuit breaking and fallbacks.
- [ ] **02.05.09** — Determine environment separation and deployment topology.
- [ ] **02.05.10** — Specify horizontal/vertical scaling and resource constraints if relevant.
- [ ] **02.05.11** — Document secrets, certificates and identity boundaries.
- [ ] **02.05.12** — Choose minimal privilege for each runtime component.
- [ ] **02.05.13** — List architectural alternatives and tradeoffs using ADRs.

**Required proof / deliverables**

- [ ] System/context/component diagrams or text equivalents.
- [ ] Approved architecture decision records with tradeoffs.

**Exit criterion:** A newcomer can explain where each key behavior and trust boundary lives.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.06 — Data Model, Storage and Migrations

**When to use:** All software projects. **Goal:** Make persisted state correct, secure and recoverable.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.06.01** — Select storage engine according to consistency, workload and offline needs.
- [ ] **02.06.02** — Model tables/collections, fields, types, defaults and constraints.
- [ ] **02.06.03** — Define primary IDs, ownership keys, relationships and cascades.
- [ ] **02.06.04** — Specify indexes based on query paths and cardinality.
- [ ] **02.06.05** — Define uniqueness and concurrency constraints.
- [ ] **02.06.06** — Specify transaction boundaries and race-condition handling.
- [ ] **02.06.07** — Separate secrets from business data when appropriate.
- [ ] **02.06.08** — Define schema migrations with up, down or forward-fix approach.
- [ ] **02.06.09** — Write backup, restore, import/export and corruption recovery strategy.
- [ ] **02.06.10** — Define expiration, archival, retention and deletion queries.
- [ ] **02.06.11** — Create representative test fixtures and prohibited data examples.
- [ ] **02.06.12** — Document encryption, key rotation and sensitive-field masking.
- [ ] **02.06.13** — Test a migration against a realistic copy of non-sensitive data.

**Required proof / deliverables**

- [ ] ERD/schema documentation, migration plan and test fixtures.
- [ ] Restore and migration verification steps.

**Exit criterion:** Data can be created, read, updated, deleted, migrated and restored safely.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.07 — API, Events, Files and Integration Contracts

**When to use:** All software projects. **Goal:** Make boundaries stable and testable for AI-assisted changes.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.07.01** — List public/private endpoints and exposed capabilities.
- [ ] **02.07.02** — Specify methods, paths, schemas, types and status codes.
- [ ] **02.07.03** — Define authn/authz, scopes and object ownership at each endpoint.
- [ ] **02.07.04** — Define request size limits, pagination, filtering and sorting.
- [ ] **02.07.05** — Specify validation errors in a consistent schema.
- [ ] **02.07.06** — Define retry/idempotency keys for mutating operations.
- [ ] **02.07.07** — Define rate limits, timeouts, backoff and circuit breaker behavior.
- [ ] **02.07.08** — Version contracts and state compatibility/deprecation policy.
- [ ] **02.07.09** — Define file size, MIME sniffing, scanning and safe storage.
- [ ] **02.07.10** — Verify webhook signatures, replay prevention and event order.
- [ ] **02.07.11** — Define third-party field mapping and data minimization.
- [ ] **02.07.12** — Write contract tests and mock response fixtures.

**Required proof / deliverables**

- [ ] API or interface specification with example requests/responses.
- [ ] Contract test plan and integration failure behavior.

**Exit criterion:** Every boundary has a validated contract and permission model.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.08 — Threat Modeling and Security Architecture

**When to use:** All software projects. **Goal:** Consider misuse and attack paths before building features.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.08.01** — List assets and what would be harmed if compromised.
- [ ] **02.08.02** — Draw trust boundaries, actors and entry points.
- [ ] **02.08.03** — Identify user roles, machine identities and privileged operations.
- [ ] **02.08.04** — Consider spoofing, tampering, information disclosure, denial of service and privilege escalation.
- [ ] **02.08.05** — Assess injection, XSS, CSRF, SSRF, deserialization and path traversal as relevant.
- [ ] **02.08.06** — Consider broken object authorization and cross-tenant access.
- [ ] **02.08.07** — Assess account compromise, password reset, session theft and token leakage.
- [ ] **02.08.08** — Review import/upload parsing and untrusted content execution risks.
- [ ] **02.08.09** — Assess supply-chain risks and malicious dependency updates.
- [ ] **02.08.10** — For agents, model prompt injection and tool escalation separately.
- [ ] **02.08.11** — Rate threats by likelihood/impact and specify preventive/detective controls.
- [ ] **02.08.12** — Assign owners, test evidence and accepted residual risks.

**Required proof / deliverables**

- [ ] Threat register and trust-boundary diagram.
- [ ] Security controls mapped to planned verification tests.

**Exit criterion:** Critical threats have planned defenses or explicitly approved stop/no-go decisions.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

### 02.09 — Architecture Decision Records (ADRs)

**When to use:** All software projects. **Goal:** Prevent AI from silently rewriting settled technical choices.

**Decisions to record:** Current state; chosen approach; budget/privacy/security constraints; dependencies; open questions.

**Detailed checklist**

- [ ] **02.09.01** — Record each irreversible/high-impact decision as an ADR.
- [ ] **02.09.02** — List context, decision, considered alternatives and why rejected.
- [ ] **02.09.03** — Document implications for security, privacy, performance and cost.
- [ ] **02.09.04** — Record affected files/modules and required migration steps.
- [ ] **02.09.05** — Identify owner, date, status and review trigger.
- [ ] **02.09.06** — Avoid creating ADRs for trivial stylistic edits.
- [ ] **02.09.07** — Record when a previous ADR is superseded rather than deleting it.
- [ ] **02.09.08** — Verify implementation matches the accepted ADR.
- [ ] **02.09.09** — Link ADRs from architecture and task documents.

**Required proof / deliverables**

- [ ] Numbered decisions in the project decision log (template in File 01) or separate ADRs.
- [ ] Change impact recorded for superseded decisions.

**Exit criterion:** Implementation follows approved decisions and deviations are visible.

**Gate review:** Record PASS / FAIL / BLOCKED / N/A (with rationale), reviewer, date, linked evidence, and unresolved work in the actual project tracker.

---

## Embedded project and design templates

### Template — Project Brief

```markdown
# Project Brief — [name]

**Owner:** [ ]  **Target audience:** [ ]  **Primary platform:** [ ]  **Current stage:** Discovery

## One-sentence problem
[ ]

## Product promise
[ ]

## Users and primary workflow
[ ]

## MVP must-have capabilities
- [ ] [F-001]
- [ ] [F-002]

## Explicit non-goals
- [ ] [not in v1]

## Technical/budget requirements
**OS/device:** [ ]  **Network:** [ ]  **Data location:** [ ]  **Recurring-cost cap:** [ ]

## Security, privacy and permissions
[ ]

## Acceptance criteria for shipping
[ ]

## Outstanding owner decisions
[ ]
```

### Template — Adr

```markdown
# ADR-[number]: [decision title]

**Status:** PROPOSED / ACCEPTED / SUPERSEDED  
**Date:** [YYYY-MM-DD]  
**Decision owner:** [name]

## Context
[Problem, requirements, existing constraints]

## Options
1. [Option]: benefits, drawbacks, cost and security implications.
2. [Option]: benefits, drawbacks, cost and security implications.

## Decision
[Chosen option and precise reasons]

## Consequences
[Modules affected, migrations, operational or security tradeoffs]

## Verification / review trigger
[Evidence and when to reconsider]

## Supersedes / superseded by
[ADR links]
```

### Template — Api Contract

```markdown
# API / Interface Contract: [name]

- **Owner:** [ ]
- **Version:** [ ]
- **Consumers:** [ ]
- **Authentication / authorization:** [ ]
- **Rate and size limits:** [ ]

## Request
**Method / path / topic:** [ ]  
**Headers:** [ ]  
**Body schema and valid example:** [ ]

## Responses
| Code | Meaning | Body schema | Retry? |
|---|---|---|---|
| 200 | success | [ ] | no |
| 400 | invalid | [ ] | no |
| 401/403 | unauthenticated/forbidden | [ ] | no |
| 429/5xx | transient/overload | [ ] | bounded |

## Trust boundaries and data classification
[Input validation, PII, token handling, ownership checks]

## Idempotency, timeouts and versioning
[ ]

## Contract tests
- [ ] Normal success
- [ ] Invalid input
- [ ] Unauthorized
- [ ] Timeouts/duplicates/rate limits
```

### Template — Threat Model

```markdown
# Threat Model — [feature/system]

## Assets and objectives
[Data, systems, integrity, availability, physical safety]

## Diagram / trust boundaries
[Who/what talks to whom; which calls leave the trusted environment]

## Threats
| ID | Attack path | Impact | Likelihood | Control | Test ID | Residual risk |
|---|---|---|---|---|---|---|
| TH-001 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## Abuse tests
- [ ] Unauthenticated and cross-user access
- [ ] Malformed and malicious-looking benign inputs
- [ ] Replay/duplicate and rate exhaustion
- [ ] Permission/approval bypass
- [ ] Prompt injection (if LLM is involved)

## Security owner signoff
[Name/date, remaining risks]
```
