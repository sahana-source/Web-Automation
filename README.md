# Project Description:

This project demonstrates a modern, end-to-end automation testing framework that integrates Selenium WebDriver, Pytest, Docker, GitHub Actions, and Kubernetes to enable scalable, consistent, and continuous test execution.
The main goal was not to build a large suite of tests, but to showcase complete DevOps integration for test automation — from writing tests → building Docker images → executing in a Kubernetes cluster via CI/CD pipelines.

## Key Features & Components
### 1. Test Automation Framework
Built using Python (Pytest + Selenium) with the Page Object Model (POM) structure.
Covers:
Valid and invalid login test cases
Product selection and checkout validation
Generates self-contained HTML reports after each run.

### 2. Containerization (Docker)
Created a Dockerfile that packages the entire test environment (Python, dependencies, Chrome, ChromeDriver, Pytest).
Allows tests to run identically on any system without local setup issues.
The image is pushed to Docker Hub automatically.

### 3. CI/CD Integration (GitHub Actions)
Configured a CI pipeline that:
Builds the Docker image whenever code is pushed.
Pushes the image to Docker Hub.
Deploys and runs the automation tests on a Kubernetes cluster (Minikube).
Waits for test completion and collects the HTML report as an artifact.
Ensures continuous testing and zero manual intervention during execution.

### 4. Kubernetes (Minikube / Cluster)
Defines a Kubernetes Job manifest to run tests inside a pod.
Uses a Persistent Volume Claim (PVC) to store generated reports.
Automatically spins up test pods, runs tests, and shuts down after completion — ensuring clean, isolated runs.

### 5. Reporting
Produces detailed HTML test reports summarizing test execution results.
Reports are automatically copied from the container to the CI/CD artifacts or local system.

## Tech Stack
Category	Tools / Technologies
Language	Python 3.12
Framework	Pytest, Selenium WebDriver
CI/CD	GitHub Actions
Containerization	Docker
Orchestration	Kubernetes (Minikube)
Reporting	Pytest HTML plugin
Version Control	Git & GitHub
Registry	Docker Hub

## Workflow Overview
Developer pushes new test code → triggers GitHub Actions pipeline.
GitHub builds and pushes the Docker image to Docker Hub.
Pipeline deploys a Kubernetes Job using the latest image.
The pod executes tests, generates a report, and exits.
HTML test report is collected and published as an artifact.

## Outcome
Successfully automated the build, deployment, and test execution process.
Demonstrated CI/CD pipeline integration with containerized tests.
Showcased how Kubernetes can be used for scalable and isolated test environments.
All test cases executed successfully across environments (local, Docker, and Kubernetes).

## Future Enhancements
Add parallel test execution in Kubernetes (multiple pods).
Integrate Allure or ReportPortal for richer test analytics.
Deploy reports to a dashboard or cloud storage (e.g., S3).
Scale the framework for API and database validation tests.
