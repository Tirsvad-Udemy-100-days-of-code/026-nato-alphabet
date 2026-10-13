from pathlib import Path

from nato_alphabet.adapters.csv_alphabet import CsvAlphabetSource, load_nato_dict

EXPECTED_ENTRIES = 26


def test_load_nato_dict_reads_temporary_csv(tmp_path: Path) -> None:
    data_file = tmp_path / "alphabet.csv"
    data_file.write_text("letter,code\na,Alfa\nB,Bravo\n", encoding="utf-8")

    assert load_nato_dict(data_file) == {"A": "Alfa", "B": "Bravo"}


def test_load_nato_dict_builds_all_entries_from_packaged_file() -> None:
    alphabet = load_nato_dict()

    assert len(alphabet) == EXPECTED_ENTRIES
    assert alphabet["Z"] == "Zulu"


def test_csv_alphabet_source_loads_given_file(tmp_path: Path) -> None:
    data_file = tmp_path / "alphabet.csv"
    data_file.write_text("letter,code\nA,Alfa\n", encoding="utf-8")

    assert CsvAlphabetSource(data_file).load() == {"A": "Alfa"}
