from app.languages import LANGUAGES
from app.utils import display_languages
from app.language_detector import detect_language
from app.translator import translate
from app.history import save_translation


def choose_language(message):

    print(f"\n{message}")

    languages = display_languages()

    while True:

        try:

            choice = int(input("\nChoose a language: "))

            if 1 <= choice <= len(languages):
                return LANGUAGES[languages[choice - 1]]

            print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


def main():

    print("=" * 50)
    print("Multilingual Translator")
    print("=" * 50)

    auto_detect = input(
        "\nAutomatically detect source language? (y/n): "
    ).lower()

    if auto_detect == "y":
        source = None
    else:
        source = choose_language("Select Source Language")

    target = choose_language("Select Target Language")

    while True:

        text = input("\nEnter text ('exit' to quit): ").strip()

        if text.lower() == "exit":
            break

        if not text:
            continue

        detected_source = source

        if source is None:
            detected_source = detect_language(text)

            if detected_source is None:
                print("Unsupported language detected.")
                continue

            print(f"\nDetected Language Code: {detected_source}")

        translated = translate(
            text,
            detected_source,
            target
        )

        save_translation(
            detected_source,
            target,
            text,
            translated
        )

        print("\nTranslation:")
        print(translated)


if __name__ == "__main__":
    main()