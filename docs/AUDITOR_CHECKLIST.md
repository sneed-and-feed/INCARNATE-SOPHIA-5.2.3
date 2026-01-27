# Auditor Quick Checklist

Use this checklist to verify the integrity of the Quantum Sovereignty Pleroma Stack release.

- [ ] **Download Artifacts**:
    - Binary
    - `manifest.json`
    - `manifest.json.sig`
    - SBOM
    - Test XML (`test-results.xml`)

- [ ] **Verify Signature**:
    ```bash
    gpg --verify manifest.json.sig manifest.json
    ```

- [ ] **Confirm Provenance**:
    - Check that `manifest.json.commit` matches the GitHub tag/commit.

- [ ] **Run Safety Audit**:
    ```bash
    python sovereign_cli.py --safety-audit --format json
    ```
    - Compare JSON output to manifest fields.

- [ ] **Run Tests**:
    ```bash
    pytest
    ```
    - Compare results to `test-results.xml`.

- [ ] **Extract Manifesto**:
    ```bash
    python sovereign_cli.py --extract-wisdom
    ```
    - Inspect the generated `logos_hash.json` and SBOM.

- [ ] **Report**:
    - Follow `SECURITY.md` for any critical findings.
