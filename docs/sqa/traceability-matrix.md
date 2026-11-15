# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added rows for the MIL-002 use case artifacts and converter code (RC-010 to RC-014) | [1b7da4b] |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the package re-review row (RC-015) | [92b9543] |
| 2026-11-15 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline milestone, the wiki row, the new review records, the concern coverage and the domain education; removed the duplicated template Purpose paragraph; reviewed in autonomous mode, not independent | [671d7c7] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the re-review records of BC-001 and MIL-004 for task 6 and corrected the coverage note about source files; reviewed in autonomous mode, not independent | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the cross-artifact traceability can be checked. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-024] (Go, re-review after the scope wording change), [RC-016] (Go, re-review of the whole document), [RC-001] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-017] (Go, re-review of the whole document), [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-018] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone | en | education | [BC-001], [PP-001] | [MIL-002], [ADR-0001], [ADR-0002] | [RC-019] (Go, re-review after the metadata change), [RC-003] |
| [MIL-002] | Milestone | en | education | [BC-001], [MIL-001] | [MIL-003], [US-001], [UC-001], [PY-002] | [RC-020] (Go, re-review after the metadata change), [RC-004] |
| [MIL-003] | Milestone | en | education | [BC-001], [MIL-002] | [MIL-004] | [RC-021] (Go, re-review after the metadata change), [RC-005] |
| [MIL-004] | Milestone | en | education | [BC-001], [PP-001], [MIL-003] | - | [RC-025] (Go, re-review after task 6), [RC-022] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-004] | - | [RC-023] (Go-with-conditions) |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | [PY-001] | [RC-006] |
| [ADR-0002] | ADR | - | - | [BC-001] | - | [RC-007] |
| [WF-001] | CI workflow | - | - | [MIL-001] | - | [RC-008] |
| [UCD-001] | Use Case Diagram | en | education | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-010] |
| [US-001] | User Story | en | education | [UCD-001], [MIL-002] | [UC-001] | [RC-011] |
| [UC-001] | Use Case | en | education | [UCD-001], [US-001] | [SSD-001], [PY-002] | [RC-012] |
| [SSD-001] | System Sequence Diagram | en | education | [UC-001] | [PY-002] | [RC-013] |
| [PY-002] | Python source | - | - | [UC-001], [SSD-001], [ADR-0001] | [PY-003] | [RC-014] |
| [PY-003] | Python source | - | - | [PY-002], [MIL-003] | - | [RC-015] |
| [PY-001] | Python source | - | - | [ADR-0001], [MIL-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-002] | - | - | Covered |
| CN-003 | [MIL-002] | - | - | Covered |
| CN-004 | [MIL-003] | - | - | Covered |
| CN-005 | [MIL-001], [MIL-003] | - | - | Covered |
| CN-006 | [MIL-001] | [ADR-0001] | - | Covered |
| CN-007 | [MIL-004] | - | - | Covered |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no review record exists.
- PP-001 was accepted by the Product Owner's stand-in without a review record; [RC-018] is its first review, against QC-PP-001.
- WF-001 and PY-001 are labels for reviewed code instances (no artifact file).
- PY-002 is the label of the reviewed converter code.
- The domain of every artifact is `education` since [MIL-004]; the earlier review records state the former domain `it` as it was at the time.
- The source code and the workflow are reviewed in the records RC-008, RC-009, RC-014 and RC-015 and not again in [MIL-004]; its task 6 rewrites the imports of `csv_alphabet.py` without changing behaviour, and the tests, ruff, mypy, import-linter and OpenGrep check it.
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-repository-foundation.md
[MIL-002]: ../milestones/mil-002-nato-converter.md
[MIL-003]: ../milestones/mil-003-documentation-and-publication.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[SA-001]: ../stakeholder-analysis.md
[7212302]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/commit/7212302fb9d9fe411215d4702d56a7cfe8834f1a
[ADR-0001]: ../adr/adr-0001-read-nato-data-with-csv-module.md
[ADR-0002]: ../adr/adr-0002-skip-analysis-artifacts.md
[WF-001]: ../../.gitea/workflows/ci.yml
[PY-001]: ../../src/nato_alphabet/constants.py
[RC-006]: ./reviews/rc-006-adr-0001.md
[RC-007]: ./reviews/rc-007-adr-0002.md
[RC-008]: ./reviews/rc-008-ci-workflow.md
[RC-009]: ./reviews/rc-009-python-skeleton.md
[a381791]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/commit/a381791874907359dab9b8f40a3c2b73f95dc0c8
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[PY-002]: ../../src/nato_alphabet/main.py
[RC-010]: ./reviews/rc-010-ucd-001.md
[RC-011]: ./reviews/rc-011-us-001.md
[RC-012]: ./reviews/rc-012-uc-001.md
[RC-013]: ./reviews/rc-013-ssd-001.md
[RC-014]: ./reviews/rc-014-python-converter.md
[1b7da4b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/commit/1b7da4bcf95f69bf009b0a1f3d0ab740ae77e340
[PY-003]: ../../src/nato_alphabet/__init__.py
[RC-015]: ./reviews/rc-015-python-package-docs.md
[92b9543]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/commit/92b954331c2deb7f9f641eb6266007496b404356
[MIL-004]: ../milestones/mil-004-framework-baseline.md
[RC-016]: ./reviews/rc-016-business-case-baseline.md
[RC-017]: ./reviews/rc-017-stakeholder-analysis-baseline.md
[RC-018]: ./reviews/rc-018-project-plan-baseline.md
[RC-019]: ./reviews/rc-019-milestone-001-baseline.md
[RC-020]: ./reviews/rc-020-milestone-002-baseline.md
[RC-021]: ./reviews/rc-021-milestone-003-baseline.md
[RC-022]: ./reviews/rc-022-milestone-004.md
[RC-023]: ./reviews/rc-023-wiki.md
[671d7c7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/commit/671d7c70db04919d0f46ce8d17d8c0053265d3fe
[RC-024]: ./reviews/rc-024-business-case-task-6.md
[RC-025]: ./reviews/rc-025-milestone-004-task-6.md
