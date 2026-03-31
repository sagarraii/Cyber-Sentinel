# 🔐 Network Security ML Pipeline — Phishing Website Detection

An end-to-end, production-grade Machine Learning pipeline designed to classify whether a website is **legitimate or phishing (malicious)**. This project follows industry best practices including modular architecture, pipeline orchestration, experiment tracking, cloud integration, and CI/CD.

---

## 🚀 Overview

This system ingests raw website data, validates and transforms it, trains a classification model, and serves predictions through a scalable pipeline.

> Designed to handle large-scale data and production deployment with clear separation of concerns across pipeline stages.

The entire workflow is designed to be:

* **Modular**
* **Scalable**
* **Reproducible**
* **Cloud-ready**

---

## 🧠 Problem Statement

Detect whether a given website is **phishing (malicious)** or **legitimate** based on structured features.

---

## 🏗️ Architecture

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Evaluation → Deployment
```

---

## 📁 Project Structure

```
.
├── .github/workflows/main.yml        # CI/CD pipeline
├── data_schema/schema.yaml           # Data schema definition
├── final_model/                      # Saved model artifacts
│   ├── model.pkl
│   └── preprocessor.pkl
├── Network_Data/phishingData.csv     # Raw dataset

├── networksecurity/
│   ├── cloud/                        # AWS S3 sync utilities
│   ├── components/                   # Core pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── constant/                     # Centralized constants
│   ├── entity/                       # Config & artifact schemas
│   ├── exception/                    # Custom exception handling
│   ├── logging/                      # Logging utilities
│   ├── pipeline/                     # Training pipeline orchestration
│   └── utils/                        # Utility functions & ML helpers

├── prediction_output/output.csv      # Prediction results
├── templates/table.html             # HTML output template
├── valid_data/test.csv              # Validation dataset

├── app.py                           # Application entry point
├── main.py                          # Pipeline trigger
├── push_data.py                     # Data push to storage
├── test_mongodb.py                  # MongoDB connectivity test

├── Dockerfile                       # Containerization
├── requirements.txt                 # Dependencies
├── setup.py                         # Packaging
└── README.md
```

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **ML Framework:** Scikit-learn
* **Experiment Tracking:** MLflow, Dagshub
* **Database:** MongoDB Atlas
* **Cloud Services:** AWS S3, EC2, ECR
* **Containerization:** Docker
* **Version Control:** Git
* **CI/CD:** GitHub Actions

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/sagarraii/Cyber-Sentinel.git]
cd Cyber-Sentinel
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables

* Create a `.env` file in the root directory:

```bash
MONGO_DB_URL="your_mongodb_atlas_url"
AWS_ACCESS_KEY_ID="your_aws_access_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
MLFLOW_TRACKING_URI="your_dagshub_mlflow_uri"
MLFLOW_TRACKING_USERNAME="your_dagshub_username"
MLFLOW_TRACKING_PASSWORD="your_dagshub_token"
```

### 4. Data Ingestion

* To push your local .csv data to MongoDB Atlas, run:

```bash
python push_data.py
```

---

## 🔄 Pipeline Workflow

### 1. Data Ingestion

* Reads raw CSV data
* Stores data in MongoDB Atlas or local storage

### 2. Data Validation

* Schema validation
* Null/missing checks
* Data consistency checks

### 3. Data Transformation

* Feature engineering
* Encoding & scaling
* Preprocessing pipeline creation

### 4. Model Training

* Classification model training
* Hyperparameter tuning
* Model evaluation using metrics

### 5. Model Storage

* Saves trained model and preprocessor
* Versioned using MLflow and stored in S3

---

## 📊 Model Evaluation

Custom metrics implemented:

* Accuracy
* Precision
* Recall
* F1 Score

Located in:

```
networksecurity/utils/ml_utils/metric/classification_metric.py
```

---

## ☁️ Cloud Integration

* **AWS S3:** Model and artifact storage
* **AWS ECR:** Docker image registry
* **AWS EC2:** Deployment environment

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t networksecurity-app .
```

### Run Container

```bash
docker run -p 8080:8080 networksecurity-app
```

---

## 🔁 CI/CD Pipeline

GitHub Actions automates:

* Code validation
* Docker build
* Deployment pipeline triggers

File:

```
.github/workflows/main.yml
```

---

## ▶️ Run the Pipeline

```bash
python main.py
```

---

## 🌐 Run the Application

```bash
python app.py
```

---

## 📌 Key Features

* Modular pipeline design
* End-to-end ML lifecycle
* Cloud-native architecture
* Experiment tracking with MLflow & Dagshub
* MongoDB integration for scalable data storage
* Dockerized deployment
* CI/CD automation

---

## 🧪 Testing

```bash
python test_mongodb.py
```

---

## 📈 Future Improvements

* Real-time streaming using Kafka
* Advanced model tuning (Optuna / Bayesian Optimization)
* Feature store integration
* Monitoring & alerting system

---

## 👨‍💻 Author

**Name: Sagar Rai**

**Email: sagarrai9547@gmail.com**

---

## ⭐ Final Note

This is not a toy notebook. It’s a **production-style ML system** — designed the way real pipelines are built in industry: clean, traceable, and scalable.

If it breaks, debug it. If it works, scale it.
