# 🛒 Flipkart Recommender System

An **LLM-powered product recommendation system** inspired by Flipkart’s e-commerce platform.
It uses **LangChain, HuggingFace embeddings, AstraDB, and Groq** to provide contextual, personalized recommendations. The system also **remembers past queries** to improve recommendations, making it more conversational and user-friendly.

🔗 **GitHub Repo:** [Flipkart Recommender LLMOps](https://github.com/sushant097/Flipcart-recommender-llmops.git)

---

## 🚀 Features

* Personalized recommendations based on product reviews
* Query memory for conversational experience
* REST API with Flask + frontend (HTML + CSS)
* Monitoring with **Prometheus** & dashboards in **Grafana**
* Containerized with Docker & deployable on Kubernetes / GCP VM

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-%F0%9F%A4%96-orange)
![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)
![Groq](https://img.shields.io/badge/LLM-Groq-green)
![AstraDB](https://img.shields.io/badge/Database-AstraDB-lightgrey)
![Flask](https://img.shields.io/badge/Backend-Flask-red)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-blue)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5)

---

## 📂 Project Structure

```bash
flipkart-recommender-llmops/
│── data/
│   └── flipkart_product_review.csv     # Product reviews dataset
│
│── flipkart/
│   ├── config.py                       # Configuration
│   ├── data_converter.py               # Data preprocessing
│   ├── data_ingestion.py               # Dataset ingestion
│   └── rag_chain.py                    # RAG pipeline
│
│── utils/
│   ├── custom_exceptions.py            # Error handling
│   └── logger.py                       # Logging
│
│── templates/                          # HTML frontend
│── static/                             # CSS styling
│── grafana/                            # Grafana configs
│── prometheus/                         # Prometheus configs
│── app.py                              # Flask app entrypoint
│── Dockerfile                          # Containerization
│── flask-deployment.yaml               # Kubernetes deployment
│── requirements.txt                    # Dependencies
│── setup.py                            # Installable package
│── script.sh                           # Automation script
│── .env.example                        # Env template
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sushant097/Flipcart-recommender-llmops.git
cd Flipcart-recommender-llmops
```

### 2️⃣ Install Package

```bash
pip install -e .
```

### 3️⃣ Setup `.env`

Create `.env` in the root:

```ini
GROQ_API_KEY=""
HF_TOKEN=""
HUGGINGFACEHUB_API_TOKEN=""
ASTRA_DB_API_ENDPOINT=""
ASTRA_DB_APPLICATION_TOKEN=""
ASTRA_DB_KEYSPACE=""
```

---

## ▶️ Run Locally

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## ☁️ VM & Kubernetes Setup (Google Cloud)

### Step 1: Create VM

* Go to **Google Cloud Console > VM Instances > Create Instance**
* Machine: **E2 Standard (16 GB RAM)**
* Boot Disk: **Ubuntu 24.04 LTS, 256 GB**
* Networking: Enable **HTTP & HTTPS traffic**
* Connect via **SSH** from console

---

### Step 2: Install Docker

```bash
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
docker run hello-world
```

Allow running without `sudo`:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

---

### Step 3: Install Minikube & kubectl

```bash
# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start cluster
minikube start

# kubectl
sudo snap install kubectl --classic
kubectl version --client
```

Check status:

```bash
minikube status
kubectl get nodes
kubectl cluster-info
```

---

### Step 4: Build & Deploy App

```bash
eval $(minikube docker-env)

docker build -t flask-app:latest .

kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="" \
  --from-literal=ASTRA_DB_APPLICATION_TOKEN="" \
  --from-literal=ASTRA_DB_KEYSPACE="default_keyspace" \
  --from-literal=ASTRA_DB_API_ENDPOINT="" \
  --from-literal=HF_TOKEN="" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN=""

kubectl apply -f flask-deployment.yaml
kubectl get pods
```

Forward service:

```bash
kubectl port-forward svc/flask-service 5000:80 --address 0.0.0.0
```

App available at: `http://<VM_IP>:5000`

---

### Step 5: Setup Prometheus & Grafana

```bash
kubectl create namespace monitoring

kubectl apply -f prometheus/prometheus-configmap.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml
kubectl apply -f grafana/grafana-deployment.yaml
```

Access:

```bash
# Prometheus
kubectl port-forward --address 0.0.0.0 svc/prometheus-service -n monitoring 9090:9090

# Grafana (default user/pass: admin/admin)
kubectl port-forward --address 0.0.0.0 svc/grafana-service -n monitoring 3000:3000
```

Configure Grafana:

* Add **Prometheus** data source
* URL: `http://prometheus-service.monitoring.svc.cluster.local:9090`
* Save & Test → ✅ Success

---

## 🎨 GUI Demo

👉 **\[Placeholder for uploading GUI screenshots / Streamlit/React UI]**

---

## 🧠 Memory Support

The system uses **LangChain memory** to recall past queries. Example:

```text
User: Recommend me budget laptops
System: Suggests Acer Aspire, Lenovo Ideapad

User: What about for gaming?
System: Refers to previous context & updates recommendations
```

---

## 📊 Monitoring

* Prometheus → `http://<VM_IP>:9090`
* Grafana → `http://<VM_IP>:3000`

---

## 📦 Requirements

See [requirements.txt](./requirements.txt)

---

## 📜 License

MIT License