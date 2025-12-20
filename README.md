QR Code Generator – Python Flask App

This is a simple Python Flask web application that generates QR codes for multiple URLs.
The application is containerized using Docker and deployed on AWS EKS (Kubernetes) using Helm, Ingress, and GitOps CI/CD with GitHub Actions and Argo CD.

Features

Generate QR codes from multiple URLs

Download individual QR codes

Download all QR codes together as a single image

Lightweight and fast Flask application

Fully containerized and cloud-native

Tech Stack

Python (Flask)

Docker

Kubernetes (AWS EKS)

Helm

NGINX Ingress Controller

GitHub Actions (CI)

Argo CD (CD / GitOps)

Run Locally : 
pip install -r requirements.txt
python app.py
Application will be available at: 
http://localhost:8881
Project Description

This project demonstrates an end-to-end DevOps workflow by deploying a simple Python Flask web application using modern cloud-native tools and practices.

The application is containerized with Docker and deployed on an AWS EKS (Kubernetes) cluster. Helm is used to manage Kubernetes resources in a reusable and configurable way, while NGINX Ingress Controller exposes the application externally.

A complete CI/CD and GitOps pipeline is implemented using GitHub Actions and Argo CD. GitHub Actions automatically builds and pushes Docker images on every code change, and Argo CD continuously syncs the Kubernetes cluster with the Git repository, ensuring that the cluster state always matches the desired configuration stored in Git.

This project focuses on DevOps concepts rather than application complexity, covering:

Containerization

Kubernetes deployments

Helm-based configuration

Ingress-based traffic routing

Automated CI/CD pipelines

GitOps-driven continuous delivery

The goal of this project is to provide a real-world DevOps implementation that reflects how applications are built, deployed, and managed in production environments.

<img width="2880" height="1800" alt="Screenshot 2025-12-19 181609" src="https://github.com/user-attachments/assets/cadedba7-020a-4c13-b513-279c585164eb" />
<img width="2880" height="1800" alt="Screenshot 2025-12-19 174023" src="https://github.com/user-attachments/assets/ab5c0d4a-363f-434c-b20c-7dc3a6d8a76a" />

