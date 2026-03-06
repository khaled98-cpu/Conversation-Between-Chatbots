import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)
anthropic_client = Anthropic(api_key=anthropic_api_key)

gpt_model = "gpt-4.1-mini"
claude_model = "claude-haiku-4-5"

gpt_system = "You are a chatbot who is very argumentative; you disagree with anything in the conversation and you challenge everything."

claude_system = "You are a very polite, courteous chatbot. You try to agree with everything the other person says."

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]


def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]

    for gpt, cloud in zip(gpt_messages, claude_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": cloud})

    response = openai_client.chat.completions.create(
        model=gpt_model,
        messages=messages
    )

    return response.choices[0].message.content


def call_claude():
    messages = []

    for gpt, claude_message in zip(gpt_messages, claude_messages):
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": claude_message})

    messages.append({"role": "user", "content": gpt_messages[-1]})

    response = anthropic_client.messages.create(
        model=claude_model,
        system=claude_system,
        messages=messages,
        max_tokens=200 # max tokens for the response
    )

    return response.content[0].text


for i in range(5):
    gpt_reply = call_gpt()
    gpt_messages.append(gpt_reply)
    print("GPT:", gpt_reply)

    claude_reply = call_claude()
    claude_messages.append(claude_reply)
    print("Claude:", claude_reply)