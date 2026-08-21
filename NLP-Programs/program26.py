from transformers import pipeline

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "I love learning artificial intelligence."

result = translator(text)

print(result[0]["translation_text"])
