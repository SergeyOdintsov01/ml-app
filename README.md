# **Практическое задание №1**

Перед выполнением задания была создана папка с репозиторием на GitHab. Прежде чем выполнить git clone нашей папки на локальный компьютер(Ubuntu 22.043 LTS на VirtualBox), нужно передать public key, сгенерированный командой: ``ssh-keygen -t ed25519 -C 'vasha_pochta@gmail.com'``

Реализация задачи перевода текста с русского на английский, а также определение тональности текста решалась при помощи библиотеки [Hugging Face](https://huggingface.co/).

>Установка transformers (версия 4.35.0):
>```python
>   pip install transformers
>```


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
  1. Начнем с установки Streamlit. [Streamlit](https://docs.streamlit.io/) — это библиотека Python с открытым исходным кодом, которая позволяет легко создавать и публиковать  пользовательские веб-приложения для машинного обучения и анализа данных. ``pip install streamlit`` (установится версия 1.12.2)
 2. Код в файле mystreamlit.py : 
 ```python
import io
import streamlit as st
from transformers import pipeline


st.title('RU/ENG translation')
text_from_st = st.text_input('Text from streamlit') #текст который ввел пользователь на страничке в браузере

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")

def translate_model(ruText):
    st.write('Переведенный текст :',translator(ruText)[0]['translation_text'])

translate_model(text_from_st)
 ```
 
3. Запускаем приложение mystreamlit.py:
    ``streamlit run mystreamlit.py``
    ![Переходим по адрессу](![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/dbd1d777-29a0-4f7c-ad5d-a004b2196c61)
)
4. Вводим текст и получаем результат:
    ![Скрин работающего веб приложения на хосте](![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/63238cfa-02cc-41b1-a323-4ee2e753fa11)
)
    ![Скрин результата работы приложения](![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/b5ba3a8f-1bca-455d-b629-cb4d04b993b6)
)

5. Далее киммитим изменения и смотрим git status:
    ![Alt text](![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/f4d0bc53-eb93-4865-a067-59d4c82b8b4d)
)
