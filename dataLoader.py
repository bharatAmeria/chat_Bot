from langchain.document_loaders import WebBaseLoader

def extract_data(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    url = "https://brainlox.com/courses/category/technical"
    docs = extract_data(url)
    print(docs[:2])  # Print a few extracted documents
