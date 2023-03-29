import config
import openai

openai.api_key = config.OPENAI_TOKEN

#lst = [{"role": "system", "content": "You are a helpful translator between Russian and Serbian. I will give you phrases on one of two languages, and you will translate it to the opposite language. Your Serbian spelling must be in latin."},]
lst = [{"role": "system", "content": "You are a helpful assistant."},]

while True:
    question = input('Q: ')
    lst.append({"role": "user", "content": question})
    answer = openai.ChatCompletion.create(
        model="gpt-4",
        messages=lst,
    ).choices[0].message.content
    lst.append({"role": "assistant", "content": answer})
    print(f'A: {answer}')
