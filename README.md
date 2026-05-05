# CloudShield – Adaptive Threat Detection System

## Overview

CloudShield is a cloud-based intrusion detection system designed to identify malicious activities using machine learning. The system analyzes behavioral patterns from user and network data to classify activities as normal or potential threats.

This project focuses on improving security monitoring by automating threat detection and reducing manual analysis effort.

---

## Problem Statement

Modern cloud systems generate large volumes of activity data, making it difficult to:

- Detect security threats in real time  
- Identify abnormal behavior patterns  
- Reduce manual monitoring and response time  

---

## Solution

CloudShield provides an automated system that:

- Analyzes behavioral and network data  
- Detects anomalies using machine learning  
- Classifies activities as normal or attack  
- Provides a structured workflow for secure file handling  

---

## Key Features

- Machine learning-based intrusion detection  
- Behavioral analysis of system activity  
- Secure file upload and verification workflow  
- Blockchain-inspired data integrity mechanism  
- End-to-end user workflow (sender, server, receiver)  
- Web-based interface using Flask  

---

## Tech Stack

- Python  
- Flask  
- SQLite (database)  
- Scikit-learn  
- NumPy  
- Pandas  
- ECDSA (cryptography)  

---

## System Architecture

1. User activity or file data is collected  
2. Data is processed and structured  
3. Machine learning model analyzes patterns  
4. System classifies activity:
   - Normal  
   - Attack  
5. Results are stored and displayed via web interface  

---

## Project Structure


cloud-anomaly-detection/
├── app.py
├── database.py
├── eval.py
├── main.py
├── RSA.py
├── config.py
├── requirements.txt
├── templates/
├── static/
├── database_file/
├── testing_df.pkl
├── LSTMModel.sav


---

## Installation & Setup

### 1. Clone Repository


git clone https://github.com/your-username/cloud-anomaly-detection.git

cd cloud-anomaly-detection


### 2. Install Dependencies


pip install -r requirements.txt


### 3. Run Application


python app.py


### 4. Open in Browser


http://127.0.0.1:5000


---

## Live Demo

CloudShield is deployed and accessible online:

https://cloud-shield-threat-detection.onrender.com/

You can:
- Register users
- Upload files
- Generate secure signatures
- Detect activity as normal or attack

---

## Usage Workflow

1. Register sender and receiver  
2. Login as sender and upload file  
3. Generate secure signature  
4. Server processes and verifies data  
5. Receiver requests access  
6. System validates and classifies activity  
7. Output is displayed as:
   - Normal  
   - Attack  

---

## Machine Learning Model

- Model Type: Pre-trained classification model  
- Input: Behavioral/network features  
- Output: Attack category or normal activity  

---

## Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  

---

## Advantages

- Automated threat detection  
- Reduces manual monitoring effort  
- Structured and modular backend design  
- Demonstrates real-world security workflow  

---

## Limitations

- Depends on dataset quality  
- Limited real-time streaming capability  
- Can be improved with advanced models  

---

## Future Improvements

- Integration with cloud platforms (AWS, Azure)  
- Real-time log streaming (Kafka)  
- Advanced deep learning models (LSTM, CNN)  
- Interactive monitoring dashboard  

---

## Author

Sadurla Jayanth  
B.Tech CSE (Data Science)

---

## Note

This project is built for learning and applying machine learning in cybersecurity and system monitoring scenarios.
