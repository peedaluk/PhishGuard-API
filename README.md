PhishGuard API 🛡️

A full-stack Machine Learning microservice that detects phishing URLs in real-time.
Built with FastAPI for high-performance networking and Scikit-Learn for the intelligence engine, backed by SQLite for audit logging.

🏗️ Architecture

The project follows a modular Controller-Service-Repository pattern:

API Layer (FastAPI): Handles HTTP requests and validates data using Pydantic schemas.

ML Engine (Scikit-Learn): A Random Forest Classifier trained to analyze URL feature vectors.

Persistence (SQLAlchemy): Logs every scan transaction to a SQLite database.

🚀 Tech Stack

Language: Python 3.9+

Framework: FastAPI + Uvicorn (ASGI)

Database: SQLite + SQLAlchemy ORM

Machine Learning: Scikit-Learn (Random Forest), NumPy, Pandas

Serialization: Joblib (Model persistence)

🛠️ Installation & Setup

1. Clone & Environment

It is recommended to use a virtual environment to manage dependencies.

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


2. Install Dependencies

pip install -r requirements.txt


3. Train the "Brain"

Before running the API, you must generate the ML model artifact (phish_model.pkl).
Run the training script:

python train_model.py


Output: [+] Saving model to 'phish_model.pkl'... Done!

⚡ Usage

1. Start the Server

Launch the API using Uvicorn (The ASGI server).

uvicorn main:app --reload


The API is now live at http://127.0.0.1:8000.

2. API Documentation (Swagger UI)

FastAPI provides interactive documentation automatically.

Open your browser to: http://127.0.0.1:8000/docs

3. Scan a URL

Send a POST request to the /scan endpoint.

Endpoint: POST /scan

Request Body:

{
  "url": "[http://192.168.1.1/login-secure-update](http://192.168.1.1/login-secure-update)"
}


Response:

{
  "id": 1,
  "url": "[http://192.168.1.1/login-secure-update](http://192.168.1.1/login-secure-update)",
  "prediction": "Phishing",
  "confidence": 0.92,
  "timestamp": "2023-10-27T14:30:00.123456"
}


4. Check Database Logs

You can inspect the scan history using the provided utility script:

python check_db.py


📂 Project Structure

phishguard/
├── main.py           # The API Controller (Entry Point)
├── models.py         # SQLAlchemy Database Tables
├── schemas.py        # Pydantic API Data Models
├── database.py       # Database Connection Factory
├── train_model.py    # Script to Train & Save ML Model
├── check_db.py       # Utility to view SQLite logs
├── phish_model.pkl   # The serialized ML Model (Generated)
├── phishguard.db     # The SQLite Database (Generated)
└── requirements.txt  # Project Dependencies


🧠 ML Logic (Feature Extraction)

The model does not read text; it analyzes mathematical vectors extracted from the URL:

Length: Phishing URLs are statistically longer.

Special Chars: High counts of dots (.) and hyphens (-).

IP Address Detection: Checks for raw IP usage (e.g., 192.168.x.x).

Digit Density: Suspiciously high number of digits in the domain.
