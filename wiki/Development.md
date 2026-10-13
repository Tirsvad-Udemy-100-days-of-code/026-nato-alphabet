# Development

🌐 **English** · [Dansk](Development-da) · [Bahasa Melayu](Development-ms)

Set up the project first ([Install](Install)). The `dev` extra installs pytest, ruff, mypy and import-linter.

## Run the tests

```bash
python -m pytest
```

## Run the checks that CI runs

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## Build the source documentation

```bash
doxygen Doxyfile
```

Open `build/html/index.html`. Install Doxygen from [doxygen.nl](https://www.doxygen.nl/) or your package manager.

## Code layout

| Folder | Content |
| --- | --- |
| `src/nato_alphabet/domain/` | The spelling rule, with no input or output |
| `src/nato_alphabet/application/` | The use case and its ports |
| `src/nato_alphabet/adapters/` | The CSV reader and the console |
| `src/nato_alphabet/constants.py` | Every literal of the program |
| `tests/` | pytest tests, mirroring `src/` |

Dependencies point inward: adapters know the application, the application knows the domain. import-linter enforces it.

## Pull requests

One branch and one pull request per milestone; CI must be green. The project follows the SQA and QC framework in `framework/`; see `docs/` for the plan and the review records.
