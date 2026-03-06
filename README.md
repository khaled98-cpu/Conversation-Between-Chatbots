# Conversation-Between-Chatbots

This project demonstrates a simple conversation between two chatbots using two different APIs:

- **OpenAI GPT**
- **Anthropic Claude**

One chatbot is configured to be argumentative, while the other is configured to be polite and agreeable.

## How it works

The script stores the conversation history in two lists:

- `gpt_messages`
- `claude_messages`

Each function rebuilds the dialogue from the perspective of one chatbot:

- `call_gpt()` sends the conversation to the OpenAI model
- `call_claude()` sends the conversation to the Anthropic model

A loop runs the conversation for several turns, and both bots respond one after another.

## Chatbot personalities

### GPT bot
The GPT bot is instructed to:
- disagree with the conversation
- challenge everything
- behave in an argumentative way

### Claude bot
The Claude bot is instructed to:
- be polite and courteous
- agree where possible
- respond in a calm way

## Requirements

Install the required packages:

```bash
pip install openai anthropic python-dotenv
