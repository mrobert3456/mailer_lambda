# 🚀 robert-meszaros.com

## 💻 Technologies

| **Category**   | **Technology** |
| -------------- | -------------- |
| **Lambda**     | Python         |
|                | AWS SES        |
|                | BOTO3          |
|                | AWS Lambda     |
| **Dev server** | FastApi        |
|                | Poetry         |
| **CI/CD**      | Github actions |

## ⚡ CI/CD pipeline

This application is deployed using a CI/CD pipeline created with **Github Actions**.

Workflow steps:

1. **Scan** repository

   - **Detect Secrets** to avoid pushing sensitive information

2. **Build** project

   - **pip install -r requirements.txt -t ./package** to install dependencies
   - **Zip Lambda function** Zipping ./package

3. **Deploy** project to Amazon Lambda

## 🚀 Installation

1. Download this repository by running:

```
git clone https://github.com/mrobert3456/mailer_lambda.git
cd mailer_lambda
```

2. Install dependencies by running:

```
poetry install
```

3. Setup `AWS CLI`
   https://aws.amazon.com/cli/

4. Create `.env` file with the following:

```
RECAPTCHA_SECRET_KEY={$your recaptcha secret key}
```

5. Start development server by running:

```
poetry run fastapi dev app.py
```
