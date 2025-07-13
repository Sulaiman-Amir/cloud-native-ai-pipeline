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


---

# 📦 MODEL FLOW (Train → Deploy → Infra → Inference)

# 1️⃣ Train Model
cd sagemaker/
pip install -r requirements.txt
python train_model.py

# 2️⃣ Deploy SageMaker Model Endpoint
python deploy_model.py

# 3️⃣ Provision Infrastructure via Terraform
cd ../terraform/
terraform init
terraform apply

# 4️⃣ Trigger Inference via API Gateway
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

---


