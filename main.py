from app.translator import translate

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Spanish": "spa_Latn"
}


def choose_language(message):
    print(f"\n{message}")

    languages = list(LANGUAGES.keys())

    for index, language in enumerate(languages, start=1):
        print(f"{index}. {language}")

    while True:
        try:
            choice = int(input("\nChoose a language: "))
            if 1 <= choice <= len(languages):
                return LANGUAGES[languages[choice - 1]]
            print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")


def main():
    print("=" * 50)
    print("Multilingual Translator")
    print("=" * 50)

    source = choose_language("Select Source Language")
    target = choose_language("Select Target Language")

    while True:
        text = input("\nEnter text ('exit' to quit): ").strip()

        if text.lower() == "exit":
            print("Goodbye!")
            break

        if not text:
            print("Please enter some text.")
            continue

        translated = translate(text, source, target)

        print("\nTranslation:")
        print(translated)


if __name__ == "__main__":
    main()