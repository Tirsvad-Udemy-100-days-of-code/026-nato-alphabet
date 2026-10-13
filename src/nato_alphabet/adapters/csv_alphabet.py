"""@brief Adapter that reads the NATO alphabet from a CSV file."""

import csv
from importlib import resources
from importlib.resources.abc import Traversable

from nato_alphabet import constants


def packaged_data_file() -> Traversable:
    """@brief Locate the data file shipped with the package.

    @return The packaged CSV file.
    """
    return (
        resources.files(constants.DATA_PACKAGE)
        / constants.DATA_DIRECTORY
        / constants.DATA_FILE_NAME
    )


def load_nato_dict(path: Traversable | None = None) -> dict[str, str]:
    """@brief Read the NATO alphabet from a CSV file.

    @param path The CSV file; the packaged file when omitted.
    @return Code word per upper-case letter.
    """
    source = path if path is not None else packaged_data_file()
    with source.open("r", encoding=constants.DATA_ENCODING) as stream:
        return {
            row[constants.LETTER_COLUMN].upper(): row[constants.CODE_COLUMN]
            for row in csv.DictReader(stream)
        }


class CsvAlphabetSource:
    """@brief AlphabetSource port implemented on a CSV file."""

    def __init__(self, path: Traversable | None = None) -> None:
        """@brief Create the source.

        @param path The CSV file; the packaged file when omitted.
        """
        ## @brief CSV file to read, or None for the packaged file.
        self._path = path

    def load(self) -> dict[str, str]:
        """@brief Read the alphabet.

        @return Code word per upper-case letter.
        """
        return load_nato_dict(self._path)
