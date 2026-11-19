Please take the project across the finish line by completing all remaining technical, engineering, and release-preparation tasks autonomously. Do NOT stop, pause for approval, or ask clarifying questions on technical decisions—use best-practice engineering judgment to resolve everything you can yourself, and isolate ONLY the steps that strictly require my direct human action, physical testing, private credentials, or legal/business sign-off.

Execute every phase below thoroughly in sequence before reporting back:

---

### Phase 1: Codebase Polish, Edge-Case Hardening & Final Cleanup
1. **Resolve Remaining Loose Ends:**
   - Scan the entire repository for lingering `TODO`, `FIXME`, `HACK`, placeholder logic, dead/commented-out code, or unused imports/assets, and clean them up properly.
   - Verify all error handling, graceful fallbacks, input validations, and user-facing error messages so the app fails safely and clearly rather than crashing silently.
2. **Dependency, Security & Configuration Audit:**
   - Ensure lockfiles (`package-lock.json`, `poetry.lock`, `Cargo.lock`, etc.) are in sync and free of critical vulnerabilities or missing peer dependencies.
   - Verify `.env.example` / configuration templates document every required environment variable or config key without exposing secrets.
   - Confirm `.gitignore` excludes build artifacts, local caches, logs, and sensitive files.
3. **Branch & CI/CD Alignment:**
   - Ensure all work is cleanly merged and consolidated into the default branch (`main`/`master`).
   - Run the full automated test suite (unit, integration, end-to-end, linting, and type-checking) and verify 100% green CI/CD status. *(Keep extra branches intact until I confirm after testing.)*

---

### Phase 2: Documentation & User Readiness
1. **Update `README.md` & Quickstart Guide:**
   - Ensure installation, configuration, build commands, and troubleshooting steps accurately reflect the final codebase.
2. **Generate Release Notes / Changelog:**
   - Draft clear, human-readable release notes summarizing new features, bug fixes, known limitations, and system requirements for this pre-release.

---

### Phase 3: Final `.exe` Pre-Release Build & Verification
1. **Clean Packaging & Build:**
   - Run a clean production/pre-release build of the Windows `.exe` installer/executable.
   - Confirm all assets, icons, binaries, runtime dependencies, and version metadata are properly bundled inside the `.exe`.
   - Run automated post-build smoke checks to ensure the packaged binary launches and initializes cleanly without missing-DLL or path errors.
2. **Publish Pre-Release Artifact:**
   - Publish the verified `.exe` to GitHub Pre-Releases (or attach it to a completed release workflow run) tagged cleanly with the current commit hash and version number.

---

### Phase 4: Final Handoff & "Human-Only" Action List
Once every automated step above is complete, deliver a structured handoff report divided into two clear sections:

1. **Completed Autonomous Work & Build Delivery:**
   - **Direct Download Link:** Exact URL to the `.exe` pre-release or artifact.
   - **Build Metadata:** Version tag, commit hash, and CI run status.
   - **Summary of Finishing Touches Completed:** Itemized list of code cleanups, fixes, docs updates, and packaging checks you completed.

2. **What Is Left for Me (Human-Only Tasks):**
   Provide a prioritized, step-by-step checklist of *only* the tasks you cannot perform autonomously, clearly grouped by:
   - **Credentials, API Keys & Secrets Setup:** Any external accounts, tokens, OAuth apps, or `.env` values I need to supply or configure locally.
   - **Windows Installation & Manual QA Testing:** Step-by-step instructions to download, bypass/approve any Windows SmartScreen unsigned-binary warning (if applicable), install, and test core user flows and edge cases on a real Windows machine.
   - **External / Third-Party Approvals & Distribution:** Any code-signing certificates, store submissions, webhook registrations, or production domain/DNS steps that require my account ownership.
   - **Final Sign-Off:** Confirmation criteria for when I am safe to give you the green light to delete the old extra branches and promote this pre-release to a full public release.
