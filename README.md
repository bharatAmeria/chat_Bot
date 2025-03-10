# LangChain Chatbot API

## Overview
This project is a chatbot API that leverages **LangChain** to extract course data from the Brainlox website, create vector embeddings, store them in a vector database, and serve responses via a **Flask RESTful API**. The chatbot enables users to retrieve course-related information through natural language queries.

## Features
- **Web Scraping**: Extracts course data from [Brainlox](https://brainlox.com/courses/category/technical) using LangChain's `WebBaseLoader`.
- **Vector Embeddings**: Uses OpenAI embeddings to encode text data.
- **Vector Database**: Stores embeddings in a **Chroma** vector store for efficient retrieval.
- **Flask REST API**: Provides an endpoint to interact with the chatbot.
- **LangChain Integration**: Uses LangChain’s **RetrievalQA** to generate responses from stored course data.

---

## Project Structure
```
📂 chatbot
├── 📄 dataLoader.py       # Extracts course data from the website
├── 📄 vectorStore.py      # Generates embeddings and stores them in Chroma DB
├── 📄 app.py           # Flask RESTful API for chatbot
├── 📄 requirements.txt     # Required dependencies
└── 📄 README.md            # Project documentation
```

---

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key (for embeddings and LLM-based responses)

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-username/chat_Bot.git
cd chat_Bot
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file and add your **OpenAI API Key**:
```sh
OPENAI_API_KEY=your-openai-api-key
```

---

## Usage

### 1. Extract Data from Brainlox
Run the following script to scrape and extract course data:
```sh
python dataLoader.py
```

### 2. Generate Embeddings & Store in Vector Database
```sh
python vectorstore.py
```

### 3. Start the Flask API
```sh
python chatbot.py
```

### 4. Query the Chatbot
Send a POST request to the API:
```sh
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"query": "What courses are available?"}'
```
Example Response:
```json
{
    "response": "Brainlox offers courses on Python, Machine Learning, and Web Development."
}
```

---

## API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST   | `/chat`  | Accepts a JSON payload `{ "query": "your question" }` and returns a response |

---

## Future Enhancements
- **Use FAISS**: Improve retrieval efficiency with **FAISS** instead of ChromaDB.
- **Authentication**: Secure API endpoints with JWT authentication.
- **Logging & Monitoring**: Add structured logging and monitoring tools.
- **Containerization**: Deploy the API with Docker & Kubernetes.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For any questions or issues, feel free to reach out!

📧 Email: bharataameriya@gmail.com
🖥 GitHub: [bharatAmeria](https://github.com/bharatAmeria)

