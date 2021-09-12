# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from unidecode import unidecode


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SLUGIFY
# └─────────────────────────────────────────────────────────────────────────────────────


def slugify(string, decode=False, space=None):
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
