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






# **Практическое задание №3**

1. Начнем у становки FastApi ``pip install fastapi`` (установилась версия 0.104.1)
2. Установим веб-серевер, в котором будет работать приложение, использующее FastAPI. Например Uvicorn: 
``pip install uvicorn`` (установилась версия 0.24.0.post1)
3. Создаем файл main.py в котором будет хранится наше FastAPI приложение(перевод с русского на английский). Приложение будет принимать POST запрос от пользователя (пользователь будет отправлять его с помощью утилиты curl в терминале Ubuntu или используя Postman). Код файла:
```python
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text:str

app = FastAPI()
translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
@app.get('/')
def root():
    return {'message':'This model translation text'}

@app.post('/translate/')
def translate(item:Item):
    return translator(item.text)[0]
```
4. Отправим POST запрос на сервер и в качестве параметра укажем текст для перевода. Это делается при помощи утилиты curl и имеет следующий вид :
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/translate/' \
  -H 'Content-Type: application/json' \
  -d '{
        "text": "Этот текст будет переведен на английский моделью машинного обучения"
      }'

```

5. Результат запуска unicorn main:app :
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/8b069b84-f7ea-490a-9192-560b51c18bf2)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/5af56ce0-10e2-4c82-8e23-36c08ef4a5c4)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/3c9cda66-1ae6-46be-8271-ad1eba1461c7)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/db4c923e-71b7-4ba3-9883-1ec3e58404c9)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/f62370f5-2b1c-4f77-aaeb-1bb1a2ba93c9)
   
   ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/121e2042-17e2-4980-a115-382c61a97d4c)

6. Автоматически сгенерированная документация :
![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/5c1ec081-652d-407b-ae6b-7276dd0a3c54)
![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/60266f6b-5123-4b8d-96d3-c559d7ee273d)


 # **Практическое задание №4**
1. Переходим на страничку [Streamlit](https://streamlit.io/cloud)
    + Cloud
    + Регистрируемся
    + Подключаем репозиторий на GitHub

        + ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/941717ff-27f4-4947-ae6d-6b4451955cac)

        + ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/51fa7a34-048d-4eb3-9222-c0fcf7ae05f0)

        + ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/6dca161b-d5a4-4af8-9004-40d3f3a87776)

        + **Видим что репозиторий подключен:**
        + ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/e7739a37-febc-4cca-81bf-c053fd888d76)
        + Поключились к нужному репозиторию и готовы запускать
        + ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/2798187a-187d-4622-9505-8746f5bab703)

2. **Перед deploy, нужно изменить/дополнить файл** ``requirements.txt``:
```bash
tensorflow-cpu
sentencepiece
transformers
streamlit
uvicorn
fastapi
streamlit
```
3. Публикуем приложение ml-app (mystreamlit.py):
    ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/af70e36a-b4e3-4c05-84d3-0bbce02409b3)

    ![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/ae7d94e2-403f-4075-8f39-09b9a329eb42)

4. Ссылка на приложение: ``https://ml-app-674mkvg6jd5ybfatem9vxq.streamlit.app/``


# **Практическое задание №5**
1. Установка библиотеки PyTest (установилась версия 7.4.3): 
```bash
pip install pytest
```
2. Для корректной работы модулея тестирования, установи предварительно ```pip install httpx```
3. Добавляем функцию тестирования в файл test_main.py : 
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This model translation text"}
```
4. Запускаем тест командой ``pytest`` .Результат работы теста:
![image](https://github.com/SergeyOdintsov01/ml-app/assets/149817675/6a1165bc-114e-4185-9fe8-7b5a8513076e)

