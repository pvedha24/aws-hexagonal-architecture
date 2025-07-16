# AWS Hexagonal Architecture Implementation Guide

This project demonstrates how to implement the **Hexagonal Architecture (Ports and Adapters)** using AWS services such as API Gateway, Amazon SQS, AWS Lambda, and DynamoDB.

It is ideal for cloud-native applications that require clear separation of concerns, scalability, and modular testing.

---

## 📄 Project Guide

👉 [Download the full PDF guide](https://docs.google.com/document/d/1BLa7lUCtU4V42ZRjUWOM61sHsUVnfa_B/edit?usp=sharing&ouid=103417016424255552492&rtpof=true&sd=true)

---

## 🧩 Architecture Overview

- **Primary Adapters**: API Gateway (HTTP), Amazon SQS (Queue-based input)
- **Domain Logic**: Central business logic using AWS Lambda functions
- **Secondary Adapters**: DynamoDB for data persistence
- **Port Communication**: Lambda functions serve as input/output ports

---

## 🔧 Setup Steps

1. **Create DynamoDB Table**
   - Table name: `UserData`
   - Partition key: `userId` (String)

2. **Create Lambda Functions**
   - `api-handler`: Handles REST API requests (POST/GET)
   - `sqs-handler`: Handles messages from SQS queue

3. **Configure IAM Policies**
   - Allow `dynamodb:PutItem`, `GetItem`, etc. for both Lambdas

4. **Create Amazon SQS Queue**
   - Queue name: `user-data-queue`
   - Connect to `sqs-handler` Lambda via trigger

5. **Set Up API Gateway**
   - Resource path: `/users`
   - Methods: POST & GET → linked to `api-handler` Lambda

6. **Deploy & Test**
   - Use `curl` or Postman to send requests
   - Trigger SQS with test messages

---

## ✅ Features

- Clean Hexagonal structure using AWS-native tools
- RESTful API + Queue processing
- Fully serverless architecture
- Easily testable and maintainable

---

## 📊 Free Tier Friendly

- **Lambda**: 1M free requests/month
- **API Gateway**: 1M API calls/month
- **DynamoDB**: 25GB storage + 25 RCU/WCU
- **SQS**: 1M requests/month

---

## 📈 Monitoring Tools

- **CloudWatch Logs** for Lambda
- **CloudWatch Metrics** for API Gateway, DynamoDB
- **AWS X-Ray** for request tracing


