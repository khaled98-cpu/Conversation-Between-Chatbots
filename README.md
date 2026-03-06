# Conversation Between Chatbots

This project demonstrates a simple conversation between two AI chatbots using two different APIs:

- **OpenAI GPT**
- **Anthropic Claude**

One chatbot is configured to be **argumentative**, while the other is **polite and agreeable**.  
The bots respond to each other using the conversation history.

---

# How it works

The script stores the conversation history in two lists:

- `gpt_messages`
- `claude_messages`

Each chatbot receives the full conversation history and generates the next response.

### GPT bot
- argumentative
- challenges everything
- disagrees with the other bot

### Claude bot
- polite
- tries to agree
- keeps the conversation calm

The program runs several conversation rounds where each bot responds to the other.

---


