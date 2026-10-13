# 🚀 NATO alphabet

A console tool that spells a word with the NATO phonetic alphabet, the Day 26 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It is written for fellow course participants and GitHub visitors who want a readable, tested, runnable solution that uses list and dictionary comprehensions and has no runtime dependencies.

![The tool spelling the word Hello][screenshot-spell]

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [Continuous integration](#-continuous-integration)
- [Build the source documentation](#-build-the-source-documentation)
- [Project layout](#-project-layout)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

You type a word, the program prints the NATO code word of each letter. A character that is not a letter makes it ask again.

```text
Enter a word: Hello
Phonetic code words:
Hotel
Echo
Lima
Lima
Oscar
```

How it works, in the course's terms:

- `load_nato_dict` reads the supplied CSV file and builds the letter-to-code-word dictionary with a **dictionary comprehension**.
- `generate_phonetic` turns a word into its code words with a **list comprehension**.
- The standard library `csv` module replaces Pandas, so the project has no runtime dependencies (see the architecture decision record [ADR-0001][ADR-0001]).

The wiki explains installation, usage and development in English, Danish and Bahasa Malaysia: [wiki][wiki].

## 📋 Requirements

- Python 3.13 or newer, with the `venv` module.
- Git, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

The program itself needs no packages. The development tools (pytest, ruff, mypy, import-linter) are installed by the `dev` extra.

## 🛠️ Setup

Clone the repository, then create a local virtual environment named `.venv` in its root, upgrade pip and install the project in editable mode with its development tools.

### Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet.git
cd 026-nato-alphabet
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow it for this window only with `Set-ExecutionPolicy -Scope Process RemoteSigned`.

### Linux Debian

```bash
sudo apt install git python3 python3-venv
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet.git
cd 026-nato-alphabet
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Debian 13 (trixie) ships Python 3.13. On an older release install Python 3.13 first (for example with `pyenv`).

### MacOS

```bash
brew install python@3.13 git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet.git
cd 026-nato-alphabet
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

With the virtual environment active:

```bash
python -m nato_alphabet
```

or, as the installed command:

```bash
nato-alphabet
```

An invalid character asks for the word again:

![A word with a digit is rejected, then a valid word is spelled][screenshot-retry]

## 🧪 Tests

Run the tests with the virtual environment active:

```bash
python -m pytest
```

The same checks that CI runs:

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## 🔄 Continuous integration

The workflow [`.gitea/workflows/ci.yml`](.gitea/workflows/ci.yml) runs on every push to `main` or a `mil-*` branch and on every pull request that touches source, tests or configuration. It sets up Python 3.13, creates a virtual environment, installs the project with the `dev` extra, and runs ruff, mypy and pytest.

## 📖 Build the source documentation

The source is documented with Doxygen comments. From the repository root:

```bash
doxygen Doxyfile
```

Open `build/html/index.html` in a browser. The `build/` folder is ignored by git.

## 🗂️ Project layout

```text
src/nato_alphabet/
  constants.py        every literal of the program
  main.py             composition root and entry point
  __main__.py         python -m nato_alphabet
  domain/             the spelling rule (no input or output)
  application/        the use case and its ports
  adapters/           CSV reader and console
  data/               nato_phonetic_alphabet.csv
tests/                pytest tests, mirroring src/
docs/                 project documents (see the appendix)
wiki/                 wiki pages in en, da and ms
.gitea/workflows/     CI workflow
pyproject.toml        project configuration
Doxyfile              Doxygen configuration
```

## 📄 License

GNU Affero General Public License v3.0 or later. See [LICENSE](LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Architecture decisions][adr] | Why the data is read with the standard library and which analysis documents were skipped |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/wiki
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/026-nato-alphabet/issues
[screenshot-spell]: ./docs/images/spell-word.png
[screenshot-retry]: ./docs/images/retry-invalid.png
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[adr]: ./docs/adr/
[ADR-0001]: ./docs/adr/adr-0001-read-nato-data-with-csv-module.md
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
