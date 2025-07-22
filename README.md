# langgraph-mcp-agent
Here's the **full `README.md` content** ready to copy-paste:

---

```markdown
# 🧠 LangGraph MCP Agent Chatbot (Groq Integration)

This project demonstrates how to build an **agentic chatbot** using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain MCP Tools](https://github.com/langchain-ai/langchain/tree/main/libs/langchain-mcp), and the **Groq API** for ultra-fast LLM inference. It supports structured tool usage via LangChain's MCP adapter interface.

---

## 🚀 Features

- 🤖 LangGraph-powered agent execution
- 🧰 Structured tool calling using MCP interface
- ⚡ Groq API support with LLaMA 3 and Mixtral
- 🌐 FastAPI server to host callable tools

---

## 📁 Project Structure



---

## 🧩 Prerequisites

- Python 3.10 or 3.11
- Groq account with API Key → [https://console.groq.com](https://console.groq.com)

---

## 🔧 Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/jashia333/langgraph-mcp-agent.git
   cd langgraph-mcp-agent
````

2. **Create and activate virtual environment**

   ```bash
   python -m venv agnt_cht
   agnt_cht\Scripts\activate  # On Windows
   # source agnt_cht/bin/activate  # On Unix/Mac
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_MODEL=llama3-8b-8192  # or mixtral-8x7b-32768
   ```

---

## ▶️ Running the Application

### 1. Start the tool server

```bash
python server.py
```

This will start a FastAPI service on:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

You should see:

```
StreamableHTTP session manager started
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 2. Start the agent client (in new terminal)

```bash
python client.py
```

You should see:

```
Available tools: [add, multiply, get_weather]
```

---

## 🧪 Example Interaction

When prompted by the agent, you can ask:

```
What is the weather like in New Jersey tomorrow?
```

It will call the `get_weather` tool using structured arguments:

```json
{ "a": "New Jersey" }
```

You can also try:

```
What is 7 + 3?
Multiply 8 and 9.
```

---

## ❓ Troubleshooting

* **`404 Not Found` errors on tool route**
  ➤ Ensure `server.py` is running before `client.py`.

* **`model_not_found` or `model_decommissioned`**
  ➤ Update `.env` to use a current Groq model:
  `llama3-8b-8192` or `mixtral-8x7b-32768`

* **Port already in use?**
  ➤ Kill any other process on port `8000` or change the port in `server.py`.

---

## 📚 Useful Links

* [LangGraph](https://docs.langgraph.ai)
* [LangChain MCP Docs](https://github.com/langchain-ai/langchain/tree/main/libs/langchain-mcp)
* [Groq Console](https://console.groq.com/docs)



