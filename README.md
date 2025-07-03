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











### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### 🐍 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

#### ✅ Activate the virtual environment:

* On **Windows**:

```bash
venv\Scripts\activate
```

* On **macOS/Linux**:

```bash
source venv/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🛠️ 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔑 5. (Optional) Create a Superuser

```bash
python manage.py createsuperuser
```

Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### ▶️ 6. Run the Development Server

```bash
python manage.py runserver
```

Now the application will be running at:
🌐 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 How to Check API in Postman

Use the following steps to test your API using Postman or any REST client.

---

### 1️⃣ Register a New User

* **Method**: `POST`
* **URL**: `http://127.0.0.1:8000/api/register/`
* **Headers**:

  * `Content-Type: application/json`
* **Body** (raw JSON):

```json
{
  "username": "vinay",
  "email": "vinay@example.com",
  "password": "testpass123",
  "dob": "2000-01-01"
}
```

---

### 2️⃣ Login to Get Auth Token

* **Method**: `POST`
* **URL**: `http://127.0.0.1:8000/api/login/`
* **Headers**:

  * `Content-Type: application/json`
* **Body**:

```json
{
  "username": "vinay",
  "password": "testpass123"
}
```

✅ **Response**:

```json
{
  "token": "your_auth_token",
  "user_id": "..."
}
```

📌 **Copy this token** and use it for all future requests.

---

### 3️⃣ Submit Paragraphs

* **Method**: `POST`
* **URL**: `http://127.0.0.1:8000/api/submit/`
* **Headers**:

  * `Content-Type: application/json`
  * `Authorization: Token your_auth_token`
* **Body**:

```json
{
  "text": "This is the first paragraph.\n\nThis is the second paragraph with lorem ipsum."
}
```

✅ **Response**:

```json
{
  "message": "2 paragraphs indexed."
}
```

---

### 4️⃣ Search Paragraphs by Word

* **Method**: `GET`
* **URL**: `http://127.0.0.1:8000/api/search/?word=lorem`
* **Headers**:

  * `Authorization: Token your_auth_token`

✅ **Response**:

```json
[
  {
    "id": "uuid-of-paragraph",
    "text": "This is the second paragraph with lorem ipsum."
  }
]
```

---

## 📘 API Summary

| Method | Endpoint               | Description               | Auth Required |
| ------ | ---------------------- | ------------------------- | ------------- |
| POST   | `/api/register/`       | Register a new user       | ❌ No          |
| POST   | `/api/login/`          | Get auth token            | ❌ No          |
| POST   | `/api/submit/`         | Submit paragraphs         | ✅ Yes         |
| GET    | `/api/search/?word=..` | Search paragraphs by word | ✅ Yes         |

---

## 📝 Notes

* Paragraphs must be separated using **two newlines**: `\n\n`
* All words are tokenized and stored in **lowercase**
* Only top 10 matched paragraphs are returned per word

```

---

```
