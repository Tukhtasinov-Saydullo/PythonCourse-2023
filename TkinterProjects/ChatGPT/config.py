import openai

openai.api_key = "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"

model_engine = "text-davinci-003"

max_tokens = 128


def answer_gpt(send_message):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=send_message,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text
