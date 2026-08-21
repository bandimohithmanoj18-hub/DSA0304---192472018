from openai import OpenAI

client = OpenAI()

prompt = "Write a short paragraph about artificial intelligence."

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print(response.output_text)
