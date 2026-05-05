# MSIT 3404 DevOps Project — Step-by-Step Command Cheat Sheet

> **NOTE: Replace `DOCKERHUB_USER` with your Docker Hub username everywhere before running these commands.**

---

## Step 1 — Log in to Docker Hub

```bash
docker login
```

---

## Step 2 — Build the Frontend Image

```bash
cd frontend
docker build -t DOCKERHUB_USER/frontend-app:latest .
```

---

## Step 3 — Push the Frontend Image

```bash
docker push DOCKERHUB_USER/frontend-app:latest
```

---

## Step 4 — Build the Backend Image

```bash
cd ../backend
docker build -t DOCKERHUB_USER/backend-app:latest .
```

---

## Step 5 — Push the Backend Image

```bash
docker push DOCKERHUB_USER/backend-app:latest
```

---

## Step 6 — Return to Project Root

```bash
cd ..
```

---

## Step 7 — Run Frontend Container Locally

```bash
docker run -d -p 8080:80 --name frontend DOCKERHUB_USER/frontend-app:latest
```

---

## Step 8 — Run Backend Container Locally

```bash
docker run -d -p 5000:5000 --name backend DOCKERHUB_USER/backend-app:latest
```

---

## Step 9 — Verify Both Containers in Browser

- Frontend → http://localhost:8080
- Backend  → http://localhost:5000

---

## Step 10 — Stop and Remove Local Containers

```bash
docker stop frontend backend
docker rm frontend backend
```

---

## Step 11 — Start Minikube

```bash
minikube start
```

---

## Step 12 — Deploy the Backend to Kubernetes

```bash
kubectl apply -f deploy-backend.yaml
```

---

## Step 13 — Check Backend Pods and Labels

```bash
kubectl get pods --show-labels
```

---

## Step 14 — Deploy the Frontend to Kubernetes

```bash
kubectl apply -f deploy-frontend.yaml
```

---

## Step 15 — Check All Pods and Labels

```bash
kubectl get pods --show-labels
```

---

## Step 16 — Label a Frontend Pod with run=testp

Copy a frontend pod name from the output of Step 15, then run:

```bash
kubectl label pod <FRONTEND_POD_NAME> run=testp
```

Example:
```bash
kubectl label pod frontend-7d9f6b-xk2pq run=testp
```

---

## Step 17 — Apply the NodePort Service

```bash
kubectl apply -f node.yaml
```

---

## Step 18 — List Services

```bash
kubectl get svc
```

---

## Step 19 — List Services with Wide Output

```bash
kubectl get svc -o wide
```

---

## Step 20 — Describe the Service

```bash
kubectl describe svc myapp-service
```

---

## Step 21 — Get the Minikube Service URL

```bash
minikube service myapp-service --url
```

This prints the URL (e.g. `http://192.168.49.2:30002`). Copy it for the next step.

---

## Step 22 — Test with curl

```bash
curl http://192.168.49.2:30002
```

Replace `192.168.49.2` with the IP printed in Step 21.

---

## Step 23 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: MSIT 3404 DevOps project"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
```

Replace `<YOUR_GITHUB_USERNAME>` and `<YOUR_REPO_NAME>` with your actual GitHub details.
Create the repository on GitHub first at https://github.com/new (set it to Public).

---

## Quick Reference

```bash
# Watch pods in real time
kubectl get pods -w

# View logs for a specific pod
kubectl logs <pod-name>

# Delete all deployments and service
kubectl delete -f deploy-frontend.yaml
kubectl delete -f deploy-backend.yaml
kubectl delete -f node.yaml

# Stop minikube
minikube stop
```
