from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from vectorstore import create_vector_store
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
api = Api(app)



# Load Vector Store
url = "https://brainlox.com/courses/category/technical"
vector_store = create_vector_store(url)
retriever = vector_store.as_retriever()

class ChatbotAPI(Resource):
    def post(self):
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        # Create a LangChain QA chain
        llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
        qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever, chain_type="stuff")

        # Get response
        response = qa_chain.run(query)
        return jsonify({"response": response})

api.add_resource(ChatbotAPI, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
