from transformers import pipeline


translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")


def input_text():
    t = input("Введите текст на русском: ")
    return t


def translate_model(ruText):
    print(
        "Перевод текста на английский:{0} ".format(
            translator(ruText)[0]["translation_text"]
        )
    )


text = input_text()
translate_model(text)
