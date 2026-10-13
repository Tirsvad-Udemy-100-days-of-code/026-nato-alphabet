"""@brief Use case: ask for a word until it can be spelled, then show it."""

from nato_alphabet.application.ports import (
    AlphabetSource,
    InputClosedError,
    WordConsole,
)
from nato_alphabet.domain.spelling import InvalidWordError, generate_phonetic


class SpellWordSession:
    """@brief One session of the tool: one word is spelled per session."""

    def __init__(self, source: AlphabetSource, console: WordConsole) -> None:
        """@brief Create a session.

        @param source Supplies the NATO alphabet.
        @param console Talks to the user.
        """
        ## @brief Supplier of the alphabet.
        self._source = source
        ## @brief Conversation with the user.
        self._console = console

    def run(self) -> None:
        """@brief Ask for words until one is valid, then show its code words.

        Ends without a result when the user can give no more input.
        """
        alphabet = self._source.load()
        while True:
            try:
                word = self._console.ask_word()
            except InputClosedError:
                return
            try:
                code_words = generate_phonetic(word, alphabet)
            except InvalidWordError:
                self._console.show_invalid()
                continue
            self._console.show_code_words(code_words)
            return
