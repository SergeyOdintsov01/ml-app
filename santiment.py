from transformers import pipeline


classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

output = classifier("Я изучаю модели манного обучения и программную инженерию")
print(output)
