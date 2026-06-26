from app.model import tokenizer, model


def translate(text, source_language, target_language):
    tokenizer.src_lang = source_language

    encoded = tokenizer(
        text,
        return_tensors="pt"
    )

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_language)
    )

    translated_text = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]

    return translated_text