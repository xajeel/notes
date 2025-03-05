# Docker Compose Tutorial: A Comprehensive Guide

This tutorial provides a detailed walkthrough of **Docker Compose**, covering essential concepts such as **services**, **volumes**, and **environment variables**. Additionally, it includes practical examples for deploying both **Flask/FastAPI** (Python-based web frameworks) and **Next.js** (React-based framework) applications using Docker Compose. We'll also set up a **reverse proxy** (e.g., Nginx) and handle SQLite databases for the Next.js app.

---

## Table of Contents
1. [Introduction to Docker Compose](#introduction-to-docker-compose)
2. [Key Concepts](#key-concepts)
   - [Services](#services)
   - [Volumes](#volumes)
   - [Environment Variables](#environment-variables)
3. [Setting Up Docker Compose](#setting-up-docker-compose)
4. [Building a Flask/FastAPI Application with Docker Compose](#building-a-flaskfastapi-application-with-docker-compose)
   - [Step 1: Create a Flask/FastAPI App](#step-1-create-a-flaskfastapi-app)
   - [Step 2: Write `docker-compose.yml`](#step-2-write-docker-composeyml)
   - [Step 3: Run the Application](#step-3-run-the-application)
5. [Building a Next.js Application with Docker Compose](#building-a-nextjs-application-with-docker-compose)
   - [Step 1: Create a Next.js App](#step-1-create-a-nextjs-app)
   - [Step 2: Write `docker-compose.yml`](#step-2-write-docker-composeyml-1)
   - [Step 3: Run the Application](#step-3-run-the-application-1)
6. [Adding a Reverse Proxy with Nginx](#adding-a-reverse-proxy-with-nginx)
7. [Conclusion](#conclusion)

---

## Introduction to Docker Compose
**Docker Compose** is a tool for defining and running multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to configure the application's services, networks, and volumes. With a single command, you can create and start all the services from your configuration.

---

## Key Concepts

### Services
A **service** in Docker Compose represents a containerized application or component. For example, a Flask API, a database, or a reverse proxy can each be defined as a service.

### Volumes
**Volumes** are used to persist data between container restarts or share files between the host machine and containers. They are particularly useful for databases and development workflows.

### Environment Variables
**Environment variables** allow you to manage configuration settings outside of your codebase. Docker Compose supports `.env` files and inline environment variable definitions in the `docker-compose.yml` file.

---

## Setting Up Docker Compose
Ensure Docker and Docker Compose are installed:
1. Verify Docker installation:
   ```bash
   docker --version
   ```
2. Verify Docker Compose installation:
   ```bash
   docker compose version
   ```

---

## Building a Flask/FastAPI Application with Docker Compose

### Step 1: Create a Flask/FastAPI App
1. Create a project directory:
   ```bash
   mkdir flask-fastapi-compose
   cd flask-fastapi-compose
   ```
2. Initialize a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn
   ```
3. Create a file named `main.py`:
   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Hello, Docker Compose!"}
   ```

### Step 2: Write `docker-compose.yml`
Create a `docker-compose.yml` file:
```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - ENV_VAR_EXAMPLE=example_value
```

Create a `Dockerfile`:
```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create a `requirements.txt` file:
```
fastapi
uvicorn
```

### Step 3: Run the Application
1. Start the application:
   ```bash
   docker compose up --build
   ```
2. Access the app at `http://localhost:8000`.

---

## Building a Next.js Application with Docker Compose

### Step 1: Create a Next.js App
1. Create a project directory:
   ```bash
   mkdir nextjs-compose
   cd nextjs-compose
   ```
2. Initialize a Next.js app:
   ```bash
   npx create-next-app@latest .
   ```
3. Add a SQLite database:
   - Install dependencies:
     ```bash
     npm install sqlite3
     ```
   - Create a `db` folder and initialize a SQLite database:
     ```bash
     mkdir db
     touch db/database.sqlite
     ```

### Step 2: Write `docker-compose.yml`
Create a `docker-compose.yml` file:
```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - ./db:/app/db
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:3000
    depends_on:
      - db

  db:
    image: nouchka/sqlite3
    volumes:
      - ./db:/var/lib/sqlite
```

Create a `Dockerfile`:
```Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

### Step 3: Run the Application
1. Start the application:
   ```bash
   docker compose up --build
   ```
2. Access the app at `http://localhost:3000`.

---

## Adding a Reverse Proxy with Nginx

### Step 1: Update `docker-compose.yml`
Add an Nginx service to route traffic to the Flask/FastAPI or Next.js app:
```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    expose:
      - "3000"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app
```

### Step 2: Create `nginx.conf`
Create an `nginx.conf` file:
```nginx
events {}

http {
  server {
    listen 80;

    location / {
      proxy_pass http://app:3000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
```

### Step 3: Run the Application
1. Start the application:
   ```bash
   docker compose up --build
   ```
2. Access the app at `http://localhost`.

---

## Conclusion
In this tutorial, you learned how to use Docker Compose to manage multi-container applications. You explored key concepts such as services, volumes, and environment variables, and applied them to real-world scenarios involving **Flask/FastAPI** and **Next.js** applications. You also learned how to add a reverse proxy using Nginx and handle SQLite databases.

For further learning, consider exploring advanced topics like scaling services, custom networks, and integrating Docker Compose with CI/CD pipelines.