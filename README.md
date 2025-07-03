# 📚 Paragraph Indexing & Word Search API (Django REST Framework)

A RESTful API that allows users to register, login, and submit multi-paragraph text. The backend tokenizes each paragraph, indexes the words, and enables fast searching of paragraphs by word.

---

## 🚀 Features

- 🔐 User authentication using token-based login
- 📄 Accepts large text input and splits into paragraphs
- 🧠 Tokenizes each paragraph and maps words to their paragraph
- 🔍 Search API to find all paragraphs containing a specific word
- 🗄️ PostgreSQL or SQLite supported

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Token Authentication
- SQLite (or PostgreSQL)
- Postman (for API testing)

---

## ⚙️ Setup Instructions

### 1. 📦 Clone the repository


git clone <your-repo-url>
cd <project-folder>
## ⚙️ Setup Instructions

### 🐍 Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
