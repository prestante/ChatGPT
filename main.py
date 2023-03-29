import config
import openai

openai.api_key = config.OPENAI_TOKEN

lst = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]


answer = openai.ChatCompletion.create(
    model="gpt-4",
    messages=lst,
)

print(answer.choices[0].message.content)
