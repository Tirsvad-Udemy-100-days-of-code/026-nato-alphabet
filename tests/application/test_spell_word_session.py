from collections.abc import Mapping

from nato_alphabet.application.ports import InputClosedError
from nato_alphabet.application.spell_word_session import SpellWordSession


class FakeSource:
    def load(self) -> Mapping[str, str]:
        return {"A": "Alfa", "B": "Bravo"}


class FakeConsole:
    def __init__(self, words: list[str]) -> None:
        self._words = words
        self.asked = 0
        self.invalid = 0
        self.shown: list[list[str]] = []

    def ask_word(self) -> str:
        self.asked += 1
        if not self._words:
            raise InputClosedError
        return self._words.pop(0)

    def show_invalid(self) -> None:
        self.invalid += 1

    def show_code_words(self, code_words: list[str]) -> None:
        self.shown.append(code_words)


def test_run_shows_code_words_for_valid_word() -> None:
    console = FakeConsole(["ab"])

    SpellWordSession(FakeSource(), console).run()

    assert console.shown == [["Alfa", "Bravo"]]
    assert console.asked == 1


def test_run_asks_again_after_invalid_word() -> None:
    console = FakeConsole(["a1", "", "b"])

    SpellWordSession(FakeSource(), console).run()

    assert console.invalid == 2
    assert console.asked == 3
    assert console.shown == [["Bravo"]]


def test_run_ends_cleanly_when_input_is_closed() -> None:
    console = FakeConsole([])

    SpellWordSession(FakeSource(), console).run()

    assert console.shown == []
