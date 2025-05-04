def format_text(
    text: str,
    prefix: str = "",
    suffix: str = "",
    capitalize: bool = False,
    max_length: int = None
) -> str:
    """
    Format the given text by adding a prefix, suffix, applying capitalization, 
    and enforcing a maximum length.

    Parameters:
    - text (str): The main text to format (required).
    - prefix (str): A string to add before the text (default: "").
    - suffix (str): A string to add after the text (default: "").
    - capitalize (bool): If True, capitalize the first character of the text (default: False).
    - max_length (int or None): If specified, truncate the final result to this length (default: None).

    Returns:
    - str: The formatted text.

    Raises:
    - TypeError: If input types are incorrect.
    - ValueError: If max_length is negative.

    Examples:
    >>> format_text("hello world")
    'hello world'

    >>> format_text("hello", prefix=">>", suffix="<<", capitalize=True)
    '>>Hello<<'

    >>> format_text("sample", max_length=4)
    'samp'
    """
    # Input validations
    if not isinstance(text, str):
        raise TypeError("The 'text' parameter must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' parameter must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' parameter must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' parameter must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' parameter must be an integer or None.")
        if max_length < 0:
            raise ValueError("The 'max_length' parameter must be non-negative.")

    # Apply transformations
    if capitalize:
        text = text.capitalize()

    formatted = f"{prefix}{text}{suffix}"

    if max_length is not None:
        formatted = formatted[:max_length]

    return formatted

# Example usage
if __name__ == "__main__":
    print(format_text("josephine", prefix=">>", suffix="<<", capitalize=True, max_length=12))