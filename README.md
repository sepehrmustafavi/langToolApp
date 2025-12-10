# 🛠️ LangTool App

**LangTool App** is a practical Natural Language Processing (NLP) toolkit designed to perform essential text processing tasks.
This project represents the first phase of my journey toward becoming a **Practical AI Engineer**, focusing on leveraging state-of-the-art open-source models from Hugging Face.

## ✨ Features (Current Version)

Currently, the application includes two core command-line tools:

* **🇫🇷 English to French Translator:**
    * Utilizes the `Helsinki-NLP/opus-mt-en-fr` model.
    * Converts English input text into fluent French.
* **📝 Text Summarizer:**
    * Utilizes the `facebook/bart-large-cnn` model.
    * Condenses long paragraphs into concise summaries while preserving key information.

## 🚀 Roadmap & Development Plan

I am following an iterative development approach to build this project:

- [x] **Phase 1: MVP**
    - Implementation of basic scripts using Hugging Face `pipeline` (High-level API).
    - Setting up the Git repository and project structure.
- [ ] **Phase 2: Web Application**
    - Building a user-friendly interface using **Streamlit**.
    - Deploying the application as a web app.
- [ ] **Phase 3: Engineering Deep Dive**
    - Refactoring code to use `AutoTokenizer` and `AutoModel` directly (Low-level implementation).
    - Adding custom parameters for text generation.
- [ ] **Phase 4: Advanced AI Features**
    - Implementing **RAG (Retrieval-Augmented Generation)** to allow chatting with documents.
    - Adding an SQL Agent using Local LLMs.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** Transformers (Hugging Face), PyTorch
- **Version Control:** Git & GitHub

## 📦 Installation & Usage

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sepehrmustafavi/langToolApp.git](https://github.com/sepehrmustafavi/langToolApp.git)
    cd langToolApp
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the tools:**
    * To run the **Translator**:
        ```bash
        python translator.py
        ```
    * To run the **Summarizer**:
        ```bash
        python summarizer.py
        ```

