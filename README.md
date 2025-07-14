yourdata-batch-app/
├── yourdata/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── db.py
│   ├── tasks.py
│   ├── batch_runner.py
│   ├── main.py
│   └── lambda_function.py
├── config.yaml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md

# yourdata Batch Processing App

A modular Python application for batch jobs. Designed for local execution or serverless deployment via AWS Lambda.

---

## 🧩 Structure

- `yourdata/` — all core logic
- `config.yaml` — centralized configuration
- `lambda_function.py` — entry point for AWS Lambda
- `main.py` — CLI/local execution entry point

---

## 🚀 Usage

### Local

```bash
python yourdata/main.py
