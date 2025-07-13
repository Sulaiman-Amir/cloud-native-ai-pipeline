# 🌩️ Cloud-Native AI Inference Pipeline (SageMaker + Lambda + API Gateway)

This project demonstrates a **fully serverless, scalable, and production-ready AI inference system** built with AWS-native services. It features model training in **SageMaker**, deployment using **Lambda** behind an **API Gateway**, and infrastructure managed via **Terraform**. Ideal for real-time AI applications with minimal operational overhead.

---

## 🚀 Features

- 🔧 **End-to-end pipeline**: From training to real-time inference
- 🧠 **Model training and deployment** on Amazon SageMaker
- ⚙️ **Inference via Lambda** using a RESTful API Gateway endpoint
- 🏗️ **Infrastructure-as-Code (IaC)** using Terraform
- 🔐 Optional **S3 integration**, **CloudWatch monitoring**, and environment-based control
- 📦 Modular architecture suitable for continuous integration and rapid iteration

---

## 🛠️ Tech Stack

| Tool              | Purpose                            |
|------------------|------------------------------------|
| AWS SageMaker     | Model training + hosting            |
| AWS Lambda        | Stateless inference handler         |
| Amazon API Gateway| Public API for inference requests   |
| Terraform         | Infrastructure provisioning         |
| Python            | ML model and logic                  |
| boto3             | AWS SDK for model invocation        |

---

## 📁 Project Structure


---

## 🧠 Model Flow

1. **Training Phase**
   - You use `sagemaker/train_model.py` to train a simple ML model (e.g., classifier or regressor).
   - Model artifacts are saved in SageMaker's managed environment or S3.

2. **Deployment Phase**
   - `sagemaker/deploy_model.py` creates a SageMaker endpoint using the trained model.
   - The endpoint can be invoked in real-time.

3. **Inference Phase**
   - Incoming requests hit the **API Gateway** endpoint.
   - API triggers the **Lambda** function (`inference_handler.py`) which invokes the SageMaker model.
   - Predictions are returned as JSON.

---

## 📦 Deployment Guide

### 🔹 1. Train Model

cd sagemaker/
pip install -r requirements.txt
python train_model.py


🔹 2. Deploy Model Endpoint
python deploy_model.py


🔹 3. Deploy Infrastructure
cd terraform/
terraform init
terraform apply
Make sure to set:

SAGEMAKER_ENDPOINT in Lambda’s environment variables

🔹 4. Trigger Inference
Make a POST request:

bash
Copy
Edit
curl -X POST https://<api-gateway-url>/predict \
     -H "Content-Type: application/json" \
     -d '{"input": [1.5, 2.3, 3.1]}'


📊 Monitoring & Logging
Logs are automatically pushed to Amazon CloudWatch

You can enhance observability with:

Alarms on Lambda errors

Tracing with AWS X-Ray

S3 logging for audit

📌 Use Cases
Real-time predictions for financial, healthcare, or e-commerce apps

Cost-effective ML inference without maintaining servers

Integrating ML into mobile or frontend apps via REST API

🧠 Improvements (Future Work)
Add support for multiple models (via path params)

Add CI/CD with GitHub Actions to automate Terraform + Lambda deployment

Fine-tune API Gateway with throttling, caching, and authorization

Use EventBridge to retrain models on schedule

👨‍💻 Author
M. Sulaiman Amir

🌐 Website: sulaimanamir.com

🧠 Credly: My Certificates

💼 LinkedIn: linkedin.com/in/m-sulaiman-amir-ab043632b

📧 Email: sullemaan007@gmail.com

🧵 Discord: sulle_amir

⚠️ License
All Rights Reserved © 2025.
This code is for demonstration and educational purposes only.
You may not copy, modify, distribute, or use it in production without permission.


