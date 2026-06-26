from langdetect import detect
from app.languages import LANGUAGE_DETECT_MAP


def detect_language(text):
    """
    Detect the language of the input text and
    return the corresponding NLLB language code.
    """

    detected = detect(text)

    return LANGUAGE_DETECT_MAP.get(detected)