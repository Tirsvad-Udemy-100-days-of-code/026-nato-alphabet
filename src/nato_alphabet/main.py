"""@brief Composition root: wires the adapters into the use case."""

from nato_alphabet import constants
from nato_alphabet.adapters.console import TerminalConsole
from nato_alphabet.adapters.csv_alphabet import CsvAlphabetSource, load_nato_dict
from nato_alphabet.application.spell_word_session import SpellWordSession
from nato_alphabet.domain.spelling import InvalidWordError, generate_phonetic

__all__ = ["InvalidWordError", "generate_phonetic", "load_nato_dict", "main"]


def main() -> int:
    """@brief Run the interactive tool.

    @return The exit status of the program.
    """
    SpellWordSession(CsvAlphabetSource(), TerminalConsole()).run()
    return constants.EXIT_OK
