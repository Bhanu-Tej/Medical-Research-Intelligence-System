import re


def clean_text(text: str):

    # Remove excessive newlines
    text = re.sub(
        r"\n+",
        "\n",
        text
    )

    # Replace multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Remove weird spacing artifacts
    text = text.replace(
        "- ",
        ""
    )

    return text.strip()