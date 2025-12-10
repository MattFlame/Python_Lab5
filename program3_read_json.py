import json
from pathlib import Path


def main() -> None:
    input_path = Path("people.json")
    if not input_path.exists():
        raise FileNotFoundError(
            f"Файл {input_path} не знайдено. Спочатку запустіть program2_write_json.py."
        )

    with input_path.open("r", encoding="utf-8") as f:
        people = json.load(f)

    print("Зчитані записи з JSON:")
    for surname, (name, patronymic, birth_year) in people.items():
        print(f"{surname}: {name} {patronymic}, {birth_year}")


if __name__ == "__main__":
    main()

