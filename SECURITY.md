# Security Policy & FAQ

## Short FAQ and Safety Notes

### Q: Is dozenal encryption?
**A:** No. Dozenal is **semantic obfuscation** to frustrate naive decimal scrapers. It is not a substitute for encryption or integrity controls.

### Q: What does `--safety-audit` check?
**A:** Network ports, telemetry bindings, dependency list, and a manifest signature check. Use `--format json` for automation.

### Q: How do I report a real vulnerability?
**A:** Encrypt your Proof-of-Concept (PoC) with the published PGP key and open a GitHub Issue tagged `[CRITICAL]`. See the Safe Harbor terms below.

### Q: Can I reproduce the binary?
**A:** Yes — `BUILD.md` and SBOM are published. Follow deterministic build steps and confirm `manifest.json.commit`.

### Q: Are there privacy or legal risks running this?
**A:** The code is experimental and labeled **hazardous**. Run in isolated sandboxes and follow the safety audit before exposing to networks or sensitive systems.

### Q: Who do I contact for coordination?
**A:** Use the PGP channel and the `[CRITICAL]` issue flow in this document. Good‑faith researchers are protected by the stated safe‑harbor.

---

## Reporting a Vulnerability

**Do not disclose vulnerabilities publicly without coordination.**

1.  **Encrypt** your findings using our PGP Key (Key ID: `0xDEADBEEF...`).
2.  **Submit** an issue with the tag `[CRITICAL]`, containing only the encrypted blob.
3.  **Wait** for acknowledgement within 48 hours.

## Safe Harbor
Researchers acting in good faith to identify and report security vulnerabilities are permitted to perform research on this project. We will not pursue legal action against researchers who:
*   Report vulnerabilities to us first.
*   Do not exploit vulnerabilities for any reason other than proving their existence.
*   Do not compromise user data or system availability.
