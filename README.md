
# Agentic AI System Using LLMs

## Project Title
**Developing an Agentic AI System Using Large Language Models (LLMs)**

## Overview
This project demonstrates the development of an Agentic AI system powered by LLMs. It showcases the ability of AI to autonomously reason, plan, and act on user input to achieve specific goals. Built using Flask and LangChain with Ollama integration, it allows PDF uploads and dynamic interaction through a chatbot UI.

## Features
- Upload and analyze PDF documents
- Extract context and answer user questions using LLMs
- Web interface with chatbot-style interaction
- Integration with LangChain and Ollama
- Uses `DocArrayInMemorySearch` for vector-based document retrieval
- Speech-to-text support and user voice commands

## Tech Stack
- Python
- Flask
- LangChain
- Ollama (LLM Backend)
- HTML/CSS/JavaScript (Bootstrap, jQuery)

## Agentic Capabilities
- Interprets user natural language queries
- Extracts relevant information from uploaded documents
- Dynamically responds to queries using LLM output
- Basic planning and reactive adaptation via context retrieval

## Setup Instructions

1. **Install Ollama and pull a model**
   ```bash
   ollama serve
   ollama pull llama3
   ```

2. **Set up Python environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python chat.py
   ```

4. **Visit the app**
   Open your browser at `http://localhost:5000`.

## Usage
1. Upload a PDF document.
2. Type or speak your question.
3. The AI will respond with relevant information based on the PDF content.

## Deliverables
- PDF-to-chatbot web interface
- PDF analysis using LLM embeddings
- Clean and functional codebase
- GitHub-ready documentation and UI

## Future Improvements
- Add multi-PDF and history support
- Improve agent planning capabilities
- Integrate with additional tools or APIs
- Add authentication and user profile tracking

---

**Course Assignment**: Machine Learning & Data Mining  
**Assignment**: Agentic AI System with LLMs  
**Author**: Mostafa Abedi  
