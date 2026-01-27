# Quickstart Sandbox Guide

**Goal:** Run and verify the release in an isolated environment without network exposure.

## 1. Create Sandbox
Use a disposable VM or container with no external network access.
```bash
# Example: Docker with no network
docker run --rm -it --network none python:3.11 bash
```

## 2. Install and Verify
Copy signed binary and `manifest.json` into the sandbox.

*   **Verify signature:**
    ```bash
    gpg --verify manifest.json.sig manifest.json
    # (Ensure you use the published PGP key)
    ```
*   **Extract manifest:**
    ```bash
    cat manifest.json
    # Confirm commit, tag, and build_timestamp match your expectations.
    ```

## 3. Run Safety Audit
Generate a machine-readable safety report.
```bash
python sovereign_cli.py --safety-audit --format json > safety.json
```
*   **Action:** Inspect `safety.json`. Confirm `network = isolated` and `dependencies = standard library only` (or minimal numpy).

## 4. Run Tests
Execute the verification suite.
```bash
pytest -q --junitxml=results/test-results.xml
```
*   **Action:** Compare `results/test-results.xml` to the official release artifact to ensure parity.

## 5. Extract Manifesto
Unlock the embedded Logos.
```bash
python sovereign_cli.py --manifesto-extract /tmp/manifesto
```
*   **Action:** Inspect `manifest.json` and SBOM in `/tmp/manifesto`.

## 6. Run a Safe Demo
Use provided demo scripts in `demos/` that form the "Star Stuff" visualization. These are explicitly sandboxed.
```bash
# Run with a deterministic seed for reproducible visuals
python demo.py
```
*(Note: Visuals are ASCII-based standard output)*
