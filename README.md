# 🤖 RAG-based Chatbot with FAISS and Web-Scraped Knowledge Base

[![🔗 Live Demo](https://img.shields.io/badge/🧪%20Try%20the%20Chatbot-Demo-blue?style=for-the-badge)](https://chabot-app-bsrraf2efxzxgimpsngbmd.streamlit.app/)

Welcome to the repository of a powerful chatbot that combines **Retrieval-Augmented Generation (RAG)** with **FAISS** for intelligent, domain-specific conversations.  
All knowledge was gathered through **web scraping using Selenium**, indexed using FAISS, and served through an interactive **Streamlit** interface.

---

## 🚀 Features

- 🧠 **Retrieval-Augmented Generation (RAG)** for contextual and grounded answers  
- ⚡ **FAISS** for lightning-fast semantic search over embeddings  
- 🌐 **Static knowledge base** extracted via **Selenium-based web scraping**  
- 💬 Smooth and responsive chatbot interface powered by **Streamlit**  
- 🔒 Fully self-contained and offline-compatible after scraping

---

## 📸 Live Demo

Click below to chat with the bot in real-time:

👉 [**Try the Chatbot**](https://chabot-app-bsrraf2efxzxgimpsngbmd.streamlit.app/)

> Ask questions about the domain-specific dataset gathered from the web and see how the RAG pipeline responds with precise, context-aware answers.

---

## 🛠️ Tech Stack

| Tool / Framework   | Purpose                                                |
|--------------------|--------------------------------------------------------|
| **RAG**            | Retrieval + Generation for factual response synthesis |
| **FAISS**          | Efficient vector search engine                         |
| **Selenium**       | Automates browser-based web scraping                   |
| **BeautifulSoup**  | Cleans and parses HTML content                         |
| **OpenAI / LLM**   | Generates final responses from retrieved context       |
| **Streamlit**      | Builds a clean and responsive UI for chatbot           |

---

## 🧱 Workflow

1. **Web Scraping:**  
   - Used **Selenium** to scrape static data from selected websites.  
   - Cleaned and processed text using **BeautifulSoup**.

2. **Embedding + Indexing:**  
   - Converted documents to vector embeddings.  
   - Stored them in a **FAISS** index for fast retrieval.

3. **Chatbot Flow:**  
   - User inputs query → FAISS retrieves top-k similar chunks → LLM generates a final answer using the context.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/chatbot-rag-faiss.git
cd chatbot-rag-faiss
pip install -r requirements.txt
