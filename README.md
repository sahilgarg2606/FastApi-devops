# FastAPI DevOps Assignment

## Overview

This project demonstrates the deployment and productionization of a FastAPI-based backend application using Docker, Docker Compose, NGINX reverse proxy, PostgreSQL, Redis, and a complete CI/CD pipeline using GitHub Actions.

The objective of this project is to showcase real-world DevOps practices including containerization, automated deployment, security scanning, infrastructure organization, monitoring readiness, and production deployment workflows.

---

## Tech Stack

### Application

* FastAPI
* Python 3.12

### Database

* PostgreSQL 16

### Cache

* Redis 7

### Reverse Proxy

* NGINX

### Containerization

* Docker
* Docker Compose

### CI/CD

* GitHub Actions
* Docker Hub

### Infrastructure

* AWS EC2 (Ubuntu)

### Security

* GitHub Secret Scanning
* Dependency Scanning
* Docker Image Scanning
* SSL/TLS Encryption

---

## Architecture

```text
                    Internet
                        |
                Domain + SSL/TLS
                        |
                    NGINX
                        |
                 FastAPI Service
                    /      \
                   /        \
                Redis    PostgreSQL
```

---

## Features

* FastAPI REST API
* Redis connectivity
* PostgreSQL integration
* Dockerized application
* Docker Compose orchestration
* NGINX reverse proxy
* Custom domain configuration
* HTTPS enabled
* Health check endpoint
* CI/CD pipeline with GitHub Actions
* Automated Docker image deployment
* Security scanning pipeline

---

## Health Check Endpoint

Endpoint:

```bash
GET /health
```

Sample Response:

```json
{
  "status": "healthy",
  "redis": "connected"
}
```

Purpose:

* Container health verification
* Deployment validation
* Monitoring integration readiness

---

## Docker Deployment

Build and Start:

```bash
docker compose up -d
```

View Running Containers:

```bash
docker ps
```

Stop Services:

```bash
docker compose down
```

---

## CI/CD Pipeline

The GitHub Actions pipeline performs:

### Code Validation

* Secret Scanning
* Dependency Scanning
* Dockerfile Validation

### Build Stage

* Docker Image Build
* Docker Image Tagging

### Publish Stage

* Push Docker Image to Docker Hub

### Deploy Stage

* Automatic Deployment to AWS EC2
* Container Recreation
* Application Availability Verification

Pipeline Flow:

```text
Developer Push
      |
      v
GitHub Actions
      |
      +---- Secret Scan
      |
      +---- Dependency Scan
      |
      +---- Docker Validation
      |
      +---- Docker Build
      |
      +---- Docker Hub Push
      |
      +---- EC2 Deployment
      |
      v
Production Environment
```

---

## SSL Configuration

HTTPS is enabled using SSL certificates.

Benefits:

* Encrypted communication
* Secure API access
* Production-ready deployment
* Improved security posture

---

## Logging Strategy

Application logs are generated using Python logging.

Example:

```python
logger.info("Health endpoint called")
```

Logs can be redirected to:

* Local log files
* Docker logs
* Centralized log management systems

View Logs:

```bash
docker logs fastapi-app
```

---

## Backup Strategy

PostgreSQL backups can be created using:

```bash
docker exec postgres \
pg_dump -U admin appdb \
> backup_$(date +%F).sql
```

Recommended:

* Daily scheduled backups
* Offsite backup storage
* Retention policy implementation

---

## Security Measures

Implemented:

* Docker container isolation
* Environment variable management
* GitHub Secrets
* SSL/TLS encryption
* Reverse proxy architecture
* Dependency vulnerability scanning
* Secret scanning
* Docker image validation

Additional Recommendations:

* UFW Firewall
* Fail2Ban
* Cloudflare Protection
* Automated Security Updates

---

## Project Structure

```text
.
├── app/
├── nginx/
│   └── default.conf
├── backups/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .github/
│   └── workflows/
└── README.md
```

---

## Future Enhancements

* Prometheus Monitoring
* Grafana Dashboards
* Automated Database Backups
* Zero Downtime Deployments
* Kubernetes Migration
* Cloudflare Integration
* Centralized Logging

---

## Deployment Verification

Application URL:

https://fastapi.devopssify.fun

Swagger Documentation:

https://fastapi.devopssify.fun/docs

Health Endpoint:

https://fastapi.devopssify.fun/health

---

## Author

Sahil Garg

DevOps Engineer Assignment Submission
