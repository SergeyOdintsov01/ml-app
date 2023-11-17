from transformers import pipeline


translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
print(translator("Этот текст должна превести на английский язык модель машинного обучения"))
