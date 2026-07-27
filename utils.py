import math


def word_count(text: str) -> int:
    """
    Returns the total number of words.
    """
    return len(text.split())


def character_count(text: str) -> int:
    """
    Returns total characters including spaces.
    """
    return len(text)


def reading_time(text: str) -> int:
    """
    Estimates reading time in minutes.
    Average reading speed = 200 words/minute.
    """
    words = word_count(text)

    if words == 0:
        return 0

    return math.ceil(words / 200)


def article_stats(text: str) -> dict:
    """
    Returns article statistics.
    """
    return {
        "Words": word_count(text),
        "Characters": character_count(text),
        "Reading Time": f"{reading_time(text)} min"
    }