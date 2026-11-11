# Machine Learning Model Deployment & Concurrency Testing on AWS

The objective of this project is to develop and deploy a Machine Learning 
inference application on AWS and evaluate its performance, scalability, 
and reliability under varying levels of concurrent traffic. Using a simple Linear Regression model, the project focuses primarily on 
production deployment, containerization, concurrency management, load testing, 
infrastructure monitoring, and horizontal scaling. 

Through controlled experiments, the goal is to identify performance 
bottlenecks, understand infrastructure limitations, 
evaluate scaling strategies, and analyze the associated AWS operational 
costs.

## Phase 1: Machine Learning Model Development

**Objective:** Develop and serialize a baseline Machine Learning model for inference deployment.

- **Algorithm:** Linear Regression (Scikit-learn)
- **Input Feature:** Area (house size)
- **Target Variable:** Price
- **Train-Test Split:** 80:20
- **Random State:** 42
- **Model Serialization:** Joblib (`.joblib`)

**Status:** Completed

## Phase 2: Frontend & Backend Development

**Objective:** Develop a functional prediction application with frontend-to-backend integration.

- **Frontend:** React, HTML and CSS
- **Backend:** FastAPI
- **Communication:** HTTP/REST API with JSON payloads
- **Integration:** Connected the React frontend to the FastAPI inference service.
- **Validation:** Successfully tested the end-to-end prediction workflow in the local development environment.

**Status:** Planned



## Phase 3: AWS Infrastructure & Production Deployment

**Objective:** Deploy the application to AWS and establish a baseline infrastructure configuration.

Planned activities:
- Provision AWS EC2 infrastructure.
- Containerize the application using Docker.
- Deploy the FastAPI inference service.
- Configure networking, security groups and application access.
- Establish application and infrastructure monitoring using CloudWatch.

**Status:** Planned

**Architecture**

![](plans/1_deployment_plan.jpeg)

## Phase 4: Concurrency & Performance Experiments

**Objective:** Evaluate application performance under varying levels of concurrent traffic.

Planned activities:
- Configure load testing using Grafana k6.
- Simulate concurrent API requests.
- Measure throughput, response latency and error rates.
- Monitor CPU and memory utilization.
- Identify application and infrastructure bottlenecks.

**Status:** Planned

## Phase 5: Horizontal Scaling & Load Distribution

**Objective:** Evaluate application scalability through distributed infrastructure.

Planned activities:
- Configure an AWS Application Load Balancer.
- Deploy multiple EC2 instances.
- Configure target groups and health checks.
- Implement Auto Scaling Groups.
- Compare performance across different scaling configurations.

**Status:** Planned

## Phase 6: Performance Analysis & Cost Optimization

**Objective:** Analyze experimental results and evaluate infrastructure efficiency.

Planned activities:
- Compare performance across deployment configurations.
- Analyze throughput, latency and infrastructure utilization.
- Identify performance bottlenecks and scalability limitations.
- Evaluate AWS infrastructure costs.
- Document findings and present experimental results.

**Status:** Planned
