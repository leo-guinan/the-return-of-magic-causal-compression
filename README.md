# The Return of Magic: Causal Compression in Adaptive Systems

A LaTeX research paper developing causal compression as a theory of how historical work becomes low-latency present capability.

Status: theory/protocol paper with bounded instrument-level experimental validation; no empirical validation of the broad causal-compression thesis.

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

## Reproduce the bounded experiment

The paper's current empirical surface is the synthetic v3 instrument validation and one 1,190-record trace replay. The synthetic reproduction is:

```bash
cd /path/to/pnp-research-base/experiment
PYTHONPATH=src python3 -m unittest tests.test_queue_migration_v3_bursty -v
PYTHONPATH=src python3 scripts/run_queue_migration_v3_bursty.py \\
  --output artifacts/queue_migration_v3.json \\
  --summary artifacts/queue_migration_v3.md
```

The trace-derived receipt, source hash, and protocol are in `experiment/docs/queue-migration-v4-results.md`, `experiment/docs/queue-migration-v4-protocol.md`, and `experiment/artifacts/queue_migration_v4.json`. Later Borg and second-trace artifacts remain archived calibration work, not part of the current paper claim surface.

## Evidence boundary

The paper formalizes a proposed framework. Its equations are definitions, accounting identities, or bounded hypotheses unless explicitly labeled otherwise. The repository contains no claim of a universal law, no P/NP result, no energy measurement, and no empirical civilizational estimate. Future experiments should connect named claims to deterministic receipts before changing the manuscript's evidence status.

## Publication state

External publication is not authorized by this local scaffold. GitHub publication, DOI assignment, and any public claim promotion remain separate actions requiring explicit review and read-back.
