from app.languages import LANGUAGES


def display_languages():

    print()

    languages = list(LANGUAGES.keys())

    for index, language in enumerate(languages, start=1):
        print(f"{index}. {language}")

    return languages