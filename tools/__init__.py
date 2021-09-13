# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import json

from unidecode import unidecode

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TYPE IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Optional


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOAD JSON
# └─────────────────────────────────────────────────────────────────────────────────────


def load_json(path: str) -> Optional[dict]:
    """ Loads a JSON file from a file path and returns a dictionary or None """

    # Initialize try-except block
    try:

        # Open file
        with open(path) as f:

            # Load data
            data = json.load(f)

        # Return data
        return data

    # Handle FileNotFoundError
    except FileNotFoundError:

        # Return None
        return None


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SLUGIFY
# └─────────────────────────────────────────────────────────────────────────────────────


def slugify(string: str, decode: bool = False, space: str = None) -> str:
    """ Returns a slugified version of a string input """

    # Check if string is null
    if not string:

        # Return an empty string
        return ""

    # Check if sould decode
    if decode:

        # Decode special characters
        string = unidecode(string)

    # Lowercase and strip slug
    string = string.lower().strip()

    # Check if space is a string
    if type(space) is str:

        # Replace spaces with the specified character
        string = string.replace(" ", space)

    # Return slugified string
    return string
