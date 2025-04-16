# 🛠️ Secure CI/CD Pipeline – Java App with SonarQube, Docker, & GitHub Actions

This lab demonstrates a secure CI/CD pipeline built for a simple Java Todo application. It integrates **Docker**, **SonarQube Cloud**, and **GitHub Actions** to automate builds, tests, and security analysis across multiple Java environments (Java 8, 11, and 17).

---

## 📁 Project Structure

| File / Folder             | Purpose                                           |
|--------------------------|---------------------------------------------------|
| `.github/workflows/`     | GitHub Actions workflow configs                   |
| `TodoList.java`          | Java source code (Todo app logic)                 |
| `todolist17Test.java`    | Unit test for Java 17 environment                 |
| `sonar-project.properties` | SonarQube config                                |
| `lib/`                   | Dependencies                                      |
| `Dockerfile` (in forked repo) | Docker setup per Java version              |
| `README.md`              | You’re reading it                                 |

---

## 🚀 CI/CD + Docker Overview

### ✅ GitHub Actions Workflow:
1. **Checkout Code**
2. **Set Up Java 17**
3. **Spin up Docker containers:**
   - `java8-app`
   - `java11-tests`
   - `java17-todo`
4. **Build and Test inside Docker**
5. **Run SonarQube Static Analysis**
6. **Publish to SonarCloud Dashboard**

---

## 🐳 Dockerized DevSecOps

Each Java version runs in its own Docker container:
- Ensures isolated, reproducible build/test environments
- Reduces “it works on my machine” bugs
- Paves the way for microservices-style deployment

**Docker Desktop** used locally to build/test and then scaled using GitHub Actions.

---

## 🔒 Security-Focused Practices

- SonarCloud scans for:
  - Bugs 🐞
  - Vulnerabilities 🚨
  - Code Smells 👃
- Quality Gates enforced before deployment
- CI/CD pipelines block insecure builds automatically
- Secure Dockerfiles minimize base image attack surface

---

## 💡 Learning Outcomes

- Orchestrated secure builds using **multi-version Docker containers**
- Integrated **SonarQube** with GitHub Actions for code quality
- Automated tests in **Java 17** container
- Learned real-world CI/CD design with DevSecOps principles

---


