"""This file will contain the function `pattern_offset` which
will find the offset in the pattern generated by the `pattern_create`
in the `pattern_create` file.

Name: pattern_offset.py

Raises:
    PatternOffsetError
"""


class PatternOffsetError(Exception):
    """Will handle any exceptions raised while attempting to
    find offset value
    """
    def __init__(self, error_msg):
        super().__init__(error_msg)


def pattern_offset(eip_value, pattern):
    """This function will generate a specific pattern of characters
    to help find offset for buffer overflow

    Args:
        eip_value (str): The specific characters that need to be searched within the `pattern`
                    argument in order to find the offset.
        pattern (str): The pattern generated by the `pattern_create` function defined in
                    `pattern_create.py` file.

    Raises:
        PatternOffsetError: 
    """
    offset = None

    return offset