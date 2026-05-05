# MSIT 3404 DevOps Project

## Team Members

- _Member 1 (placeholder)_
- _Member 2 (placeholder)_
- _Member 3 (placeholder)_

---

## Description

This project implements a full DevOps pipeline that packages a web application into Docker containers and deploys it on a local Kubernetes cluster using Minikube.

The **frontend** is a static HTML/CSS/JS site served by an **Nginx** container. The **backend** is a Python **Flask** application that serves a static image. Both services are built into Docker images, published to Docker Hub, and then deployed as Kubernetes Deployments. A **NodePort Service** exposes the frontend pod to the host machine.

---

## Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Frontend     | HTML, CSS, JavaScript   |
| Web Server   | Nginx (Alpine)          |
| Backend      | Python 3.10, Flask      |
| Containers   | Docker                  |
| Orchestration| Kubernetes (Minikube)   |
| Registry     | Docker Hub              |
| Version Control | Git + GitHub         |

---

## Project Structure

```
project/
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── static/          ← place image.jpg here
│   └── Dockerfile
├── deploy-backend.yaml
├── deploy-frontend.yaml
├── node.yaml
├── commands.md
└── README.md
```

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- A [Docker Hub](https://hub.docker.com/) account

---

## How to Run

> See **`commands.md`** for the full step-by-step command cheat sheet.

### 1. Add the backend image

Place your image file at `backend/static/image.jpg` before building.

### 2. Build and push Docker images

```bash
docker login

cd frontend
docker build -t DOCKERHUB_USER/frontend-app:latest .
docker push DOCKERHUB_USER/frontend-app:latest

cd ../backend
docker build -t DOCKERHUB_USER/backend-app:latest .
docker push DOCKERHUB_USER/backend-app:latest
```

### 3. Test locally with Docker

```bash
docker run -d -p 8080:80 --name frontend DOCKERHUB_USER/frontend-app:latest
docker run -d -p 5000:5000 --name backend DOCKERHUB_USER/backend-app:latest
```

Open http://localhost:8080 (frontend) and http://localhost:5000 (backend).

### 4. Deploy to Kubernetes

```bash
minikube start
kubectl apply -f deploy-backend.yaml
kubectl apply -f deploy-frontend.yaml

# Label a frontend pod so the Service can reach it
kubectl get pods --show-labels
kubectl label pod <FRONTEND_POD_NAME> run=testp

kubectl apply -f node.yaml
minikube service myapp-service --url
```

---

## License

For academic use — MSIT 3404.
