import pytest

from nato_alphabet.adapters.csv_alphabet import load_nato_dict
from nato_alphabet.domain.spelling import InvalidWordError, generate_phonetic

ALPHABET = load_nato_dict()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@pytest.mark.parametrize("letter", list(LETTERS))
def test_generate_phonetic_maps_letter_to_its_code_word(letter: str) -> None:
    assert generate_phonetic(letter, ALPHABET) == [ALPHABET[letter]]


def test_generate_phonetic_uses_known_code_words() -> None:
    assert generate_phonetic("ADZ", ALPHABET) == ["Alfa", "Delta", "Zulu"]


def test_generate_phonetic_covers_all_26_letters() -> None:
    assert len(generate_phonetic(LETTERS, ALPHABET)) == len(LETTERS)


def test_generate_phonetic_is_case_insensitive_for_mixed_case() -> None:
    assert generate_phonetic("Hello", ALPHABET) == [
        "Hotel",
        "Echo",
        "Lima",
        "Lima",
        "Oscar",
    ]


@pytest.mark.parametrize("word", ["a1", "two words", "hi!", "", "ß", "æ"])
def test_generate_phonetic_raises_for_non_letter_or_empty(word: str) -> None:
    with pytest.raises(InvalidWordError):
        generate_phonetic(word, ALPHABET)


def test_generate_phonetic_keeps_cause_of_invalid_character() -> None:
    with pytest.raises(InvalidWordError) as info:
        generate_phonetic("a1", ALPHABET)

    assert isinstance(info.value.__cause__, KeyError)
