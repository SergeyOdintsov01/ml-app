# **Практическое задание №1**

Перед выполнением задания была создана папка с репозиторием на GitHab. Прежде чем выполнить git clone нашей папки на локальный компьютер(Ubuntu 22.043 LTS на VirtualBox), нужно передать public key, сгенерированный командой: ``ssh-keygen -t ed25519 -C 'vasha_pochta@gmail.com'``

Реализация задачи перевода текста с русского на английский, а также определение тональности текста решалась при помощи библиотеки [Hugging Face](https://huggingface.co/).

1. Задача перевода текста:
    + Решалась при помощи готовой модели  ["Helsinki-NLP/opus-mt-ru-en"](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en).
    + Содержимое файла translate.py :
    ```python
    from transformers import pipeline
    translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
    print(translator("Этот текст должна превести на английский язык модель машинного обучения"))

    ```
2. Задача определения тональности текста :
    + Решалась при помощи готовой модели ["blanchefort/rubert-base-cased-sentiment"](https://huggingface.co/blanchefort/rubert-base-cased-sentiment)
    + Содержимое файла santiment.py :
    ```python
    from transformers import pipeline
    classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
    output = classifier("Я изучаю модели манного обучения и программную инженерию")
    print(output)
    ```

# **Практическое задание №2**
 
