# Knowledge-graph audit — 2026-09-11

## Verdict

The project has a public artifact corpus and one claim-specific synthetic evidence chain plus one source-derived calibration chain. It does not yet have a complete evidence graph or field validation.

The current state is best described as:

```text
public source catalogue
+ validated formal slices
+ bounded experiment archive
+ one claim-specific synthetic support/test chain
+ one source-derived trace calibration chain
- deployment or external operational evidence
- profile-held causal-compression commitments
- resolved source-hash lineage for AxiomReason readbacks
```

The graph snapshot is structurally valid. Its epistemic edges remain sparse by design.

## Inventory

| Class | Count | Current state |
|---|---:|---|
| Paper manuscript source | 1 | Public GitHub source, commit `00e360b` |
| Compiled paper PDF | 1 | Public GitHub artifact; 11 pages |
| Paper claims/hypotheses | 8 | Four framework claims, four hypotheses in the claims ledger |
| Descriptive definitions | 6 | In `Workspace/CausalCompression.lean`; server-validated, unpublished |
| Descriptive Statements | 12 | In the same package; not theorem declarations |
| Proved theorem declarations | 11 | Three public AxiomReason source packages |
| Bounded experiment result documents | 37 | In the public experiment archive; queue migration v3 and v4 are claim-linked |
| AxiomReason theorem receipts | 3 | Search/fetch readback recorded |
| Experiment manifest receipt | 1 | 384-entry archive manifest |
| Causal-compression profile holdings | 0 | Not represented in the profile commitment projection |

## Formal artifacts

### `hmhhcnw7` — headroom arithmetic

Source: `Workspace/CausalCompressionTheorems.lean`

Declarations:

- `headroom_nonnegative`
- `headroom_zero_of_burden_ge_capacity`
- `headroom_positive_iff_capacity_exceeds_burden`
- `safe_retirement_gain_of_burden_release`

Scope: arithmetic consequences of an explicit `Nat` model.

Status:

```text
local validation: passed
server validation: passed
public source: confirmed by search and fetch
profile-held: no
empirical support edge: none
```

### `j1b75r6z` — forward accounting

Source: `Workspace/CausalCompressionForwardTheorems.lean`

Declarations:

- `headroom_transition_accounting`
- `backlog_grows_when_arrivals_exceed_service`
- `zero_gain_preserves_structure`
- `compressed_policy_equal_on_equal_representation`

Scope: explicit `Int` accounting and representation model. The backlog result is one-step recurrence arithmetic, not a general queueing theorem. The representation result is conditional action equality, not proof of real-world sufficiency.

Status:

```text
local validation: passed
server validation: passed
public source: confirmed by search and fetch
profile-held: no
empirical support edge: none
```

### `dn8bd2yh` — discrete dynamics

Source: `Workspace/CausalCompressionDynamicalTheorems.lean`

Declarations:

- `bounded_update_stays_between_state_and_target`
- `zero_adaptation_rate_preserves_state`
- `sufficient_representation_preserves_continuation`

Scope: a discrete `Int` update rule and an explicit continuation-factorization premise. It does not establish thrashing, rigidity, or sufficiency of a selected real representation.

Status:

```text
local validation: passed
server validation: passed
public source: confirmed by search and fetch
profile-held: no
empirical support edge: none
```

## Important dependency finding

`CausalCompression.lean` is the descriptive conceptual package. The three theorem packages are conceptually motivated by the paper and related definitions, but their source files do not formally import `CausalCompression.lean`.

Therefore the graph records:

```text
paper / descriptive package ──conceptually_depends_on──> theorem package
```

It does not record:

```text
CausalCompression.lean ──depends_on──> theorem package
```

That formal dependency would be false under the current Lean sources. If we later want a mechanically linked theorem layer, the imports and build dependency must be changed and revalidated.

## Publication and hash audit

All three theorem packages have independent AxiomReason search/fetch receipts. The `axm publish` command returned a successful publication message but exited with status 1; publication was therefore not accepted on exit status alone.

Each receipt also records a difference between the submitted local hash and the fetched public-source hash:

| File ID | Submitted hash | Fetched hash | State |
|---|---|---|---|
| `hmhhcnw7` | `6533592d…65f65` | `9c81f9fa…b8d99` | Mismatch unresolved |
| `j1b75r6z` | `8b4c58a9…52af7e` | `f1ce3480…58b19` | Mismatch unresolved |
| `dn8bd2yh` | `4701c046…7cab6` | `2e54badf…83688` | Mismatch unresolved |

This does not establish corruption. It establishes that AxiomReason's public fetched representation is not byte-identical to the submitted local file, or that the receipt hashes were computed over different representations. The graph must not call these byte-level identities verified until the normalization/transport rule is known.

## Experiment audit

The experiment archive contains 35 result documents and a 384-entry manifest. These are valuable evidence-bearing artifacts, but their current relationship to the paper is mostly documentary:

```text
experiment repository ──documents──> result document
```

The graph intentionally contains zero automatically generated `supports`, `tests`, or `falsifies` edges from those results to the eight paper claims/hypotheses.

To add such an edge, each candidate result needs:

1. an exact claim contract;
2. a named comparator or baseline;
3. a declared estimand;
4. scope and seed information;
5. an independent readback of the result artifact;
6. a calibrated conclusion that does not exceed the receipt.

The 35 documents should not be summarized as “evidence for causal compression” merely because their filenames contain morphology, capability, history, observation, or transition language. The market has enough semantic soup already.

## Missing graph elements

The current snapshot is missing or incomplete in these areas:

- no profile-held causal-compression proposition;
- descriptive package is not published;
- no formal import dependency between descriptive and theorem packages;
- no claim-specific experiment `tests` edges;
- no experiment-to-claim `supports` edges;
- no `falsifies` or contradiction edges;
- no explicit counterexample nodes;
- no paper-section/source-locator fields for every claim occurrence;
- no complete experiment protocol-to-result edge for all 35 results;
- no resolved explanation for submitted/fetched AxiomReason hash differences;
- no generated static navigator yet;
- no automated regeneration script for the graph snapshot;
- no supersession edges for earlier formulations;
- no DOI/Zenodo publication node.

## Recommended next gates

### Gate 1 — make the snapshot reproducible

Create a deterministic builder that reads the paper claims ledger, AxiomReason receipts, Lean sources, experiment manifest, and explicitly curated mapping file. It should regenerate `graph-v1.json`, validate endpoint integrity, and fail on missing provenance.

### Gate 2 — resolve AxiomReason source normalization

Fetch each public source, record the exact bytes used for the fetched hash, compare normalized text against local source, and document any server transformation. Until then, retain both hashes.

### Gate 3 — curate evidence edges claim by claim

Start with one hypothesis, probably queue migration or headroom erosion. Do not map all 35 experiment results at once. A single clean claim/result/baseline chain is more valuable than a large decorative graph.

### Gate 4 — decide what belongs in the Axiom profile

Only promote a narrow proposition into the profile commitment layer after explicit review. Profile visibility is not a valid reason to turn a descriptive or empirical hypothesis into an axiom.

### Gate 5 — build the public navigator

Once the source graph is reproducible, render a static profile projection with filters for claim type, epistemic status, formal status, publication status, and evidence state. The renderer should expose unresolved edges instead of hiding them.

## Bottom line

We currently have enough material for a credible public graph, but not enough evidence to claim that the graph explains the whole theory. The strongest existing nodes are the paper, three validated/published formal slices, and the bounded experiment archive. The weakest layer is the connective tissue: which artifact tests which claim, under which contract, with what result, and what would falsify it.

That connective tissue is the next research artifact. Not another theorem-shaped object. Another theorem-shaped object would be easier. That is precisely why it is suspicious.
