# CONTEXT FACT REGISTER — Vietnam ETS premises
Version: 0.2
Created: 2026-10-02 · Updated: 2026-10-03 (Gate 1A premise verification, task G1A-01)
Maintainer: Claude (`claude-opus-5-5`); human verification pending

## Rules
- A premise may be cited in project documents only with the status shown here and its `Source_ID` (see `SOURCE_MANIFEST.csv`).
- **Status vocabulary (G1A-01 §13):**
  - `VERIFIED`: established from a primary/authoritative source, read directly.
  - `PARTIALLY VERIFIED`: official metadata, an official secondary report, or a reproduction of an official text; or verified in part.
  - `CONTRADICTED`: an authoritative source contradicts the premise.
  - `NOT FOUND`: searched, not found. **This does not mean the thing does not exist.**
  - `NOT PUBLICLY ACCESSIBLE`: a legal reporting duty exists, but no public access route was found.
  - `UNKNOWN`: not determinable from what was examined.
- `DERIVED` in the locator column means the fact was computed by Claude from a stored source; the computation is described in `G1A_PREMISE_VERIFICATION_REPORT.md`.
- Retrieval date for all entries: **2026-10-03**, unless stated otherwise.
- Legal text was read from the official signed scan of Decree 119/2025 (no OCR; pages read visually). Decree 83/2026 was read from the text layer of the Official Gazette PDF.

---

## P1 — Legal architecture
| Fact_ID | Exact claim | Status | Source_ID (source date; effective date) | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P1.1 | The domestic ETS rests on the Law on Environmental Protection No. 72/2020/QH14 (as amended, latest cited amendment Law 146/2025/QH15). | PARTIALLY VERIFIED | SRC-DEC-083-2026 (2026-03-23) | Preamble (citation of the law) | The specific LEP article on the carbon market was not read | Background only |
| P1.2 | The operative ETS rules are Decree 06/2022/NĐ-CP as amended by Decree 119/2025/NĐ-CP (issued 2025-06-09; effective 2025-08-01): allocation (Art. 12), market actors (Art. 16), roadmap (Art. 17), registry (Art. 18), trading/borrowing/surrender/carry-over/offsets (Art. 19). | VERIFIED | SRC-DEC-119-2025 (2025-06-09; 2025-08-01) | Art. 1 cl. 8, 13–16 (scan pp. 8–14) | — | Core legal corpus for RQ1 and the construct |
| P1.3 | Decree 83/2026/NĐ-CP (2026-03-23, effective on signing) amends only Art. 24, 26 and Annex VI forms (ozone-depleting/controlled substances). It does **not** change the ETS provisions. | VERIFIED | SRC-DEC-083-2026 (2026-03-23; 2026-03-23) | Art. 1–5 (Công báo 183, pp. 62–65) | — | No ETS change since 119/2025 found |
| P1.4 | Roadmap: until end-2028, registry + pilot domestic carbon trading platform + domestic crediting; from 2029, allowance auctioning and full market rules. | VERIFIED | SRC-DEC-119-2025 | Art. 17 as amended (scan p. 10) | — | Prices before 2029 come from a thin pilot market only |
| P1.5 | Scheme for carbon market establishment (Decision 232/QĐ-TTg, 2025-01-24): pilot 2025–end-2028; official operation from 2029; HNX provides the trading platform. | PARTIALLY VERIFIED | SRC-DEC-232-2025 (metadata) + official press | baochinhphu.vn 24/01/2025 | Text not read | Consistent with P1.4 |
| P1.6 | Competent authority: Ministry of Agriculture and Environment (MAE) allocates, runs the registry and the MRV system; MOIT and MOC propose facility quotas for their sectors. | VERIFIED | SRC-DEC-119-2025 | Art. 9.2, 12.1.b, 12.2, 18.1 (scan pp. 3, 8, 11) | — | Data owner for emissions is MAE (+ MOIT/MOC) |
| P1.7 | Decree 29/2026/NĐ-CP (2026-01-19, effective same day) governs the domestic carbon trading platform. | PARTIALLY VERIFIED | SRC-DEC-029-2026 (metadata) + official press | baochinhphu.vn 20/01/2026 | Text not read | Market-microstructure details unverified |
| P1.8 | Circular 11/2026/TT-BNNMT (2026-02-13; effective 2026-03-30) governs the national registry. | PARTIALLY VERIFIED | SRC-CIRC-011-2026 (metadata, Công báo 147) | Gazette metadata | Registry disclosure rules not read | Check whether registry holdings or surrenders are public (Gate 1B/T04) |

## P2 — Covered facilities
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P2.1 | Facilities eligible for quota in 2025–2026: thermal power plants (coal, oil, gas), crude-steel producers, clinker producers that are on the PM's GHG-inventory list. | VERIFIED | SRC-DEC-119-2025 | Art. 12.1.a; Annex I Method 01 (scan pp. 8, 35) | — | Sector scope fixed for the pilot |
| P2.2 | 110 facilities receive 2025–2026 quotas: 34 thermal power, 25 iron & steel, 51 cement. | VERIFIED | SRC-ALLOC-699-2026; SRC-MEDIA-002 | Annex row count (DERIVED); official press | — | Quota universe = 110 rows |
| P2.3 | An authoritative facility list with quotas exists as the annex of Decision 699/QĐ-BNNMT (2026-02-27). | PARTIALLY VERIFIED | SRC-ALLOC-699-2026 | Legal-database reproduction; official MAE copy **NOT FOUND** | Provenance of the copy | Primary-source copy must still be obtained |
| P2.4 | The 2026 GHG-inventory universe is 2,441 facilities in 6 sectors (Decision 42/2026/QĐ-TTg, effective 2026-09-25). | PARTIALLY VERIFIED | SRC-DEC-042-2026 | Media incl. baochinhphu.vn 11/08/2026 | Official text not read | Relevant for 2027+ expansion, not for the pilot sample |
| P2.5 | Allocation rows are not uniform physical facilities: 110 rows → 103 distinct tax codes → 91 distinct legal-entity roots. 5 tax codes carry more than one row (e.g. Phú Mỹ 1, 2.1, 4 share one code). One legal entity (3000437821, Formosa Hà Tĩnh) appears in both the power and steel sectors. | VERIFIED (DERIVED) | SRC-ALLOC-699-2026 | DERIVED from annex | What a "facility" is differs across rows (plant, company, plant group) | Unit of analysis must be defined explicitly (ISS-011) |

## P3 — Facility-level allowances
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P3.1 | Facility-level allocated quotas for 2025 and for 2026 (tCO2e, integer) are publicly readable, together with facility name, address, tax code and legal representative. Structure: one HTML table, three sector blocks, 7 columns. | PARTIALLY VERIFIED (access verified; copy not the official original) | SRC-ALLOC-699-2026 | Annex table | Reproduction vs signed original | Allowance link of the chain is available |
| P3.2 | Totals: 243,082,392 tCO2e (2025) and 268,391,454 tCO2e (2026). Sector shares 2025: power 57.0%, steel 12.8%, cement 30.2%. | VERIFIED | SRC-ALLOC-699-2026; SRC-DEC-263-2026; SRC-MEDIA-002; SRC-HNX-CARBON-2026 | Annex sums equal the 263/QĐ-TTg totals and the HNX total exactly (DERIVED) | — | Independent reconciliation of three sources |
| P3.3 | HNX lists one allowance instrument, VN2025, for compliance period 2025–2026, total 511,473,846 (= 2025 + 2026). | VERIFIED | SRC-HNX-CARBON-2026 | Allowance list page | — | Two annual quotas are traded as one period instrument |
| P3.4 | Allocation for 2027–2028 is due by 2027-10-31 and for 2029–2030 by 2029-10-31. | VERIFIED | SRC-DEC-119-2025 | Art. 12.2.c (scan p. 8) | — | Next allocation data arrive late 2027 |

## P4 — Allocation methodology
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P4.1 | A(a,y) = P̄(a; y−1, y−2, y−3) × B × T: facility average output over the three prior years × sector average intensity × adjustment coefficient. | VERIFIED | SRC-DEC-119-2025 | Annex I, Method 01 (scan p. 35) | — | **Benchmark × output** allocation (RQ2 decomposition) |
| P4.2 | B = Σ Ē(y−1..y−3) / Σ P̄(y−1..y−3) over allocated facilities "of the sector" (facility 1 … n). Product units: kWh (power), t crude steel, t clinker. | VERIFIED | SRC-DEC-119-2025 | Annex I, Method 01 (scan p. 35) | Whether thermal power is one pooled sector or split by fuel/technology: **UNKNOWN**. The same question applies to BF-BOF vs EAF steel. | Determines whether coal/BF-BOF facilities are systematically short |
| P4.3 | T = (1 + g)(1 − r). g = sector growth target for the allocation period. r = sector reduction target, taking into account the facility's reduction roadmap, technology level, financial capacity and reductions already implemented. Line ministries determine T for each facility. | VERIFIED (text) | SRC-DEC-119-2025 | Annex I, Method 01 (scan p. 36) | Whether T actually varies across facilities: **UNKNOWN** | Facility-specific T would break pure benchmark logic |
| P4.4 | Within each sector the 2026/2025 quota ratio is (near-)uniform: cement 1.09425 for all 51; power 1.0956 for 33 of 34 (one at 1.0899); steel 1.165–1.170. | VERIFIED (DERIVED) | SRC-ALLOC-699-2026 | DERIVED | Consistent with a sector-common year factor and a fixed facility base; does not reveal the base T | INFERENCE: facility heterogeneity sits in P̄ (and possibly T_2025), not in year-on-year adjustment |
| P4.5 | Quotas are allocated by the State with no auctioning before 2029. | VERIFIED | SRC-DEC-119-2025 | Art. 12, Art. 17.2.a (scan pp. 8–10) | "Free of charge" is stated by secondary sources only | No allowance purchase cost at allocation |
| P4.6 | Ex-post adjustment of quotas to actual output. | NOT FOUND | SRC-DEC-119-2025 | Art. 12 and Method 01 contain no such clause | May exist elsewhere (guidance, registry circular) | If absent, output growth above P̄ increases shortfall |
| P4.7 | At proposal stage, MAE stated that sector totals were below projected emissions by 1.6–2.0% (power), 3.8–4.4% (steel) and 4.0–4.5% (cement). Projections used 2022–2023 activity data and the 2024 inventory. | PARTIALLY VERIFIED | SRC-MEDIA-001 (2025-12-25) | Media quote of Vice Minister Lê Công Thành | Proposal stage; final margins not confirmed | Aggregate stringency is mild (R-5, ISS-012) |

## P5 — Facility-level emissions
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P5.1 | Quota facilities must prepare biennial facility inventory reports from 2026 (Form 06, Annex II). Their inventories must be verified by an accredited verifier. Verified results are submitted to MAE by 1 December each year from 2027. | VERIFIED (legally required) | SRC-DEC-119-2025 | Art. 11.4.c, 11.6a; Art. 14 (scan pp. 7, 9) | — | First verified compliance-grade data for 2025–2026: due by 2027-12-01 |
| P5.2 | Surrender is measured against verified inventory results for **direct** emission sources in the allocation period. | VERIFIED | SRC-DEC-119-2025 | Art. 19.5.a (scan p. 13) | Treatment of process vs combustion emissions not read in Annex II | Compliance boundary = direct emissions only (EAF electricity excluded) |
| P5.3 | Public disclosure of facility-level inventory or verified emissions. | NOT PUBLICLY ACCESSIBLE (duty to report exists; no publication clause or public dataset found) | SRC-DEC-119-2025 | Amended Art. 11 clauses read; MAE updates results into the national database (Art. 11.2.e), with no public-access clause | Registry circular and MAE portal not fully examined | **Binding constraint for RQ2/RQ3 (ISS-010)** |
| P5.4 | Listed companies must report total direct and indirect GHG emissions in annual reports (Circular 96/2020/TT-BTC, Annex IV s. 6.1). | PARTIALLY VERIFIED | SRC-MEDIA-010 | Secondary | Firm level, not facility level; scopes mixed; assurance not required | At best a Tier 2 firm-level proxy for listed parents |
| P5.5 | Facility emissions cannot be recovered from published quotas. Form 01 publishes only A, and A = P̄ × B × T contains no facility emissions. | VERIFIED (by formula) | SRC-DEC-119-2025; SRC-ALLOC-699-2026 | Form 01 (scan p. 33); Method 01 | — | E must come from another source |

## P6 — Compliance rules
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P6.1 | One allowance = right to emit 1 tCO2 or 1 tCO2e. | VERIFIED | SRC-DEC-119-2025 | Art. 19.1.a (scan p. 12) | — | Unit |
| P6.2 | Surrender ≥ verified direct emissions for the period minus credits used for offset, before 31 December of the year after the allocation period. For 2025–2026 this is 2027-12-31. | VERIFIED (date DERIVED) | SRC-DEC-119-2025; SRC-HNX-CARBON-2026 | Art. 19.5.a–b (scan p. 13); HNX last trading day 2027-12-24 | — | Compliance timing for scenarios |
| P6.3 | Shortfall: administrative sanction under environmental sanction law, and the missing quantity is deducted from the next period's allocation. | VERIFIED | SRC-DEC-119-2025 | Art. 19.5.e (scan p. 13) | Fine amount: claim of 300–400 million VND (Decree 45/2022) is **UNKNOWN** (secondary only) | Non-compliance cost is partly deferred, not priced |
| P6.4 | Borrowing until end-2030 from the facility's own next-period allocation, ≤15% of the period's allocation, not tradable. | VERIFIED | SRC-DEC-119-2025 | Art. 19.6 (scan p. 13) | — | Softens near-term shortfall |
| P6.5 | Carry-over (banking) until end-2030 of unused quota after surrender; carried quota is tradable. Unsurrendered, untransferred quota is cancelled 30 days after the deadline. | VERIFIED | SRC-DEC-119-2025 | Art. 19.7 (scan pp. 13–14) | — | Surplus retains option value |
| P6.6 | Offsets: carbon credits from the domestic mechanism and Article 6.2/6.4 mechanisms (credited reductions from 2021-01-01) may cover up to 30% of the facility's allocated quota. | VERIFIED | SRC-DEC-119-2025 | Art. 19.1.b, 19.8.a (scan pp. 12, 14) | Credit supply/price unknown | Large flexibility relative to 1.6–4.5% aggregate gap |
| P6.7 | Allocation/compliance period: 2025–2026, with annual quota amounts. | VERIFIED | SRC-DEC-119-2025; SRC-HNX-CARBON-2026 | Art. 12.1; Form 01 note | — | Period unit = 2 years |

## P7 — Trading and market maturity
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P7.1 | The HNX domestic carbon trading platform is operating. VN2025 status: Trading/Normal; first trading day 2026-06-29; last trading day 2027-12-24. | VERIFIED | SRC-HNX-CARBON-2026 | Allowance list page | — | Infrastructure exists |
| P7.2 | Trades to 2026-08-14: one session with trades, 1,210 tCO2e, 161.66 million VND, 130,000–136,000 VND/t. | PARTIALLY VERIFIED | SRC-MEDIA-003, SRC-MEDIA-004; HNX snapshot (52-week high/low 136/130 thousand VND) | Media citing HNX; HNX page consistent | Trades after 2026-08-14 not checked day by day | **No usable price history** |
| P7.3 | No price/volume history exists that could support forecasting or a market-event study. | VERIFIED (by P7.1–P7.2) | — | — | — | Supports DEC-003 |
| P7.4 | Trading fees are waived until 2028-12-31; trading uses securities accounts at carbon trading members. | PARTIALLY VERIFIED | SRC-DEC-029-2026 | Official press summary | — | — |

## P8 — Organizational identity (very small reconnaissance only)
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P8.1 | Every allocation row carries a tax code: 79 enterprise-level codes (10 digits) and 31 dependent-unit codes (10+3). The dependent-unit prefix identifies the owning legal entity. Power has 22 of 34 rows as dependent units. | VERIFIED (DERIVED) | SRC-ALLOC-699-2026 | DERIVED | — | Facility → legal entity link is code-based for all rows |
| P8.2 | Reconnaissance cases (5): (a) Quảng Ninh TPP JSC: own enterprise code, facility = firm. (b) Phú Mỹ 1/2.1/4: one dependent-unit code under the EVNGENCO3 root. (c) Kiên Lương and Bình Phước cement plants: dependent units of Vicem Hà Tiên 1. (d) AES Mông Dương II: own code, foreign-owned BOT LLC. (e) Hòa Phát: at least three separate legal entities with allocation rows. | PARTIALLY VERIFIED | SRC-ALLOC-699-2026; SRC-MEDIA-005 … 009 | Row names/codes; media for ownership | Ownership shares and consolidation status not verified from filings | Linking is plausible; the ultimate parent and consolidation require filings (ISS-008) |
| P8.3 | Some entity names in the annex appear outdated (e.g. row 14 names GENCO3 as a single-member LLC branch). | VERIFIED (observation) | SRC-ALLOC-699-2026 | Row text | Name ≠ current legal form | Use tax code, not name, as the key |

## P9 — Financial data path (existence check only)
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P9.1 | Audited FY2025 financial statements exist for PGV (EVNGENCO3), HT1 (Vicem Hà Tiên), QTP (Quảng Ninh TPP) and HPG (Hòa Phát Group). | PARTIALLY VERIFIED | SRC-MEDIA-005, 006, 007, 009 | Media/aggregators; primary HOSE/HNX filings not retrieved | — | Listed parents have a financial path |
| P9.2 | Public local financial statements for AES Mông Dương (BOT, foreign-owned). | NOT FOUND | SRC-MEDIA-008 | Partial figures via AES Corp disclosures only | — | BOT/FDI rows likely lack a financial denominator |
| P9.3 | Dependent units (branches) have no separately published financial statements; exposure must be aggregated to the legal entity or group. | INFERENCE (not verified) | — | — | — | Unit-of-analysis decision (ISS-008, ISS-011) |

## P10 — CBAM boundary
| Fact_ID | Exact claim | Status | Source_ID | Evidence locator | Ambiguity | Implication |
|---|---|---|---|---|---|---|
| P10.1 | The EU CBAM definitive regime applies from 2026-01-01 to cement, iron and steel, aluminium, fertilisers, electricity and hydrogen. Importers above a 50-tonne threshold declare embedded emissions and surrender certificates. A carbon price paid in the country of production can be deducted. | VERIFIED | SRC-EU-CBAM-2026 | EU DG TAXUD page | How free allocation in Vietnam affects the deduction: **UNKNOWN** | CBAM is a separate EU instrument hitting exporters of two of the three pilot sectors; boundary channel per DEC-009 |

---

## Superseded entries from v0.1 (2026-10-02 background-knowledge leads)
| v0.1 ID | Lead | Result |
|---|---|---|
| F01 | LEP 72/2020 | → P1.1 (PARTIALLY VERIFIED) |
| F02 | Decree 06/2022; 119/2025 | → P1.2 (VERIFIED) |
| F03 | Decisions 01/2022, 13/2024 (inventory lists) | Not verified; superseded in practice by 42/2026/QĐ-TTg (P2.4) |
| F04 | Sectors: power, steel, cement | → P2.1 (VERIFIED) |
| F05 | Possibly free, intensity-based allocation | → P4.1–P4.5 (VERIFIED: benchmark × output with sector-average benchmark) |
| F06 | Publication of facility allocations | → P3.1 (PARTIALLY VERIFIED) |
| F07 | Publication of facility emissions | → P5.3 (NOT PUBLICLY ACCESSIBLE) |
| F08 | Compliance obligations | → P6.1–P6.7 (VERIFIED) |
| F09 | HNX platform | → P7.1 (VERIFIED) |
| F10 | MAE as authority | → P1.6 (VERIFIED) |
| F11 | 3,000 tCO2e inventory threshold | Not examined in Gate 1A (UNKNOWN) |
| F12 | Regulated electricity tariff / single buyer | Not examined in Gate 1A (UNKNOWN); needed for RQ3 pass-through |
| F13 | Decision 232/QĐ-TTg | → P1.5 (PARTIALLY VERIFIED) |
| F14 | EU CBAM from 2026 | → P10.1 (VERIFIED) |
| (onboarding R-5) | "Pilot allocation likely generous (surplus)" | **Not supported as stated.** MAE's proposal-stage statement implies a small aggregate *shortfall* (P4.7), offset by large flexibility (P6.4–P6.6). Near-term exposure is small in magnitude, but its sign is not "surplus". |
