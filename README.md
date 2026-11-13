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

**Status:** Completed



## Phase 3: AWS Infrastructure & Production Deployment

**Objective:** Deploy the application to AWS and establish a baseline infrastructure configuration.

Planned activities:
- Provision AWS EC2 infrastructure.
- Containerize the application using Docker.
- Deploy the FastAPI inference service.
- Configure networking, security groups and application access.
- Establish application and infrastructure monitoring using CloudWatch.

**Status:** Completed


## Phase 4: Concurrency & Performance Experiments

**Objective:** Evaluate application performance under varying levels of concurrent traffic.

Planned activities:
- Configure load testing using Grafana k6.
- Simulate concurrent API requests.
- Measure throughput, response latency and error rates.
- Monitor CPU and memory utilization.
- Identify application and infrastructure bottlenecks.

**Status:**  In Progress


## Phase 5: Performance Analysis & Cost Optimization

**Objective:** Analyze experimental results and evaluate infrastructure efficiency.

Planned activities:
- Compare performance across deployment configurations.
- Analyze throughput, latency and infrastructure utilization.
- Identify performance bottlenecks and scalability limitations.
- Evaluate AWS infrastructure costs.
- Document findings and present experimental results.

**Status:** Planned




# Trade-offs and Design Decisions

### 1. Streamlit vs. React vs. HTML/CSS

The primary objective of this project is to evaluate backend performance and identify infrastructure limitations. With this in mind, React was not selected because it introduces an additional frontend framework, build tooling, and dependencies that are unnecessary for a simple, single-input prediction interface.

Similarly, Streamlit was not chosen because its application runtime introduces additional resource overhead, potentially increasing CPU and memory consumption and impacting overall application performance.

Instead, **HTML/CSS was chosen as a lightweight alternative** to minimize frontend complexity and resource consumption. This allows the study to focus primarily on backend performance and infrastructure constraints without introducing unnecessary frontend overhead.

### 2. EC2 vs. ECR for Deployment

For deployment, I opted for a simpler approach:

**GitHub → EC2 → Docker Build → Docker Run**

Rather than building a Docker image locally and pushing it to Amazon Elastic Container Registry (ECR), the application code will be pulled directly from GitHub onto the EC2 instance, where the Docker image will be built and executed.

Although ECR provides benefits such as centralized image storage, versioning, and easier image distribution across multiple environments, it introduces an additional service and deployment step.

Given the scope of this project, deploying directly on EC2 offers a simpler workflow with fewer dependencies and less infrastructure overhead, while remaining sufficient for evaluating application performance and infrastructure limitations.
