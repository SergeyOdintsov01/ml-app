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
      ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/221fec39-c900-437e-a469-ddc1fdd1cb73)

4. Вводим текст и получаем результат:
    ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/3f46e666-6006-4ba5-950b-2fd46df4ba23)
    ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/513cf7b4-6878-402f-aac7-4b1bf268271e)


5. Далее коммитим изменения и смотрим git status:
    ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/0ecf1f78-0058-41ac-afab-91012bfe5b55)









5. Результат запуска unicorn main:app :
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/8b069b84-f7ea-490a-9192-560b51c18bf2)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/5af56ce0-10e2-4c82-8e23-36c08ef4a5c4)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/3c9cda66-1ae6-46be-8271-ad1eba1461c7)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/db4c923e-71b7-4ba3-9883-1ec3e58404c9)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/f62370f5-2b1c-4f77-aaeb-1bb1a2ba93c9)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/121e2042-17e2-4980-a115-382c61a97d4c)
   


   



