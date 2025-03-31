from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter
import warnings

# Optional: suppress legacy warnings in dev
warnings.filterwarnings("ignore")

def create_chain(pdf_file, question, model_name="llama3", base_url="http://localhost:11434"):
    try:
        # Initialize model and embeddings
        model = OllamaLLM(model=model_name, base_url=base_url)
        embeddings = OllamaEmbeddings(model=model_name, base_url=base_url)

        # Load and split PDF
        loader = PyPDFLoader(pdf_file)
        pages = loader.load_and_split()

        # Define prompt
        template = """
        Answer the question based on the context below. If you can't answer
        the question, reply "I don't know". Additionally, reply to conversational 
        messages like greetings.

        Context: {context}

        Question: {question}
        """
        prompt = PromptTemplate.from_template(template)

        # Build vector store and retriever
        vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
        retriever = vectorstore.as_retriever()

        # Create the LangChain chain
        chain = (
            {
                "context": itemgetter("question") | retriever,
                "question": itemgetter("question")
            }
            | prompt
            | model
            | StrOutputParser()
        )

        return chain.invoke({"question": question})

    except Exception as e:
        return f"[ERROR] {str(e)}"

if __name__ == "__main__":
    # Example usage
    pdf_file = "mlSchool.pdf"
    question = "Summarize the course in 2-3 sentences."
    response = create_chain(pdf_file, question)
    print(response)