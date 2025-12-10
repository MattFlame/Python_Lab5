from typing import List, Tuple

# Ukrainian alphabet order (lowercase) including ґ, є, ї, і
UKRAINIAN_ALPHABET = [
    "а",
    "б",
    "в",
    "г",
    "ґ",
    "д",
    "е",
    "є",
    "ж",
    "з",
    "и",
    "і",
    "ї",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ь",
    "ю",
    "я",
]

UKRAINIAN_ORDER = {letter: index for index, letter in enumerate(UKRAINIAN_ALPHABET)}


def is_ukrainian_word(word: str) -> bool:
    """Return True if the word starts with a Ukrainian letter (case-insensitive)."""
    if not word:
        return False
    first = word[0].lower()
    return first in UKRAINIAN_ORDER


def ukrainian_sort_key(text: str) -> Tuple[int, List[int]]:
    
    lower_text = text.lower()
    uk_word = is_ukrainian_word(lower_text)

    def char_weight(ch: str) -> int:
        # Ukrainian letters use defined order; others fall back to Unicode.
        return UKRAINIAN_ORDER.get(ch, 1000 + ord(ch))

    weights = [char_weight(ch) for ch in lower_text]
    return (0 if uk_word else 1, weights)


def sort_words(words: List[str]) -> List[str]:
    return sorted(words, key=ukrainian_sort_key)


def main() -> None:
    words = [
        "English",
        "інформація",
        "android",
        "Windows",
        "Добрий день",
        "матриця",
        "актова зала",
        "біоресурси",
        "єдиний",
        "кава",
        "Їжак у саду",
        "Єнот",
        "iphone",
        "Інженерія",
    ]

    print("Заданий список:")
    print(words)

    sorted_words = sort_words(words)

    print("\nВідсортований список:")
    print(sorted_words)


if __name__ == "__main__":
    main()

