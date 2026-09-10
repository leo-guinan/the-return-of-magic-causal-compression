# The Return of Magic: Causal Compression in Adaptive Systems

A LaTeX research paper developing causal compression as a theory of how historical work becomes low-latency present capability.

Status: local draft; theory/protocol paper; not an empirical validation of the broad thesis.

## Repository contents

- `paper/main.tex` — manuscript source
- `paper/references.bib` — source-checked working bibliography; incomplete author metadata is marked explicitly
- `claims/claims.yaml` — claim ledger with falsifiers and evidence boundaries
- `docs/RESEARCH-BOUNDARY.md` — scope and non-claims
- `scripts/validate.py` — deterministic manuscript/ledger checks
- `zenodo.json` — not-published metadata template
- `.github/workflows/ci.yml` — clean LaTeX and ledger build

## Build

```bash
python3 scripts/validate.py
cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated PDF is `paper/main.pdf` and is checked in as the current compiled projection. Auxiliary LaTeX build outputs are ignored by Git.

## Evidence boundary

The paper formalizes a proposed framework. Its equations are definitions, accounting identities, or bounded hypotheses unless explicitly labeled otherwise. The repository contains no claim of a universal law, no P/NP result, no energy measurement, and no empirical civilizational estimate. Future experiments should connect named claims to deterministic receipts before changing the manuscript's evidence status.

## Publication state

External publication is not authorized by this local scaffold. GitHub publication, DOI assignment, and any public claim promotion remain separate actions requiring explicit review and read-back.
