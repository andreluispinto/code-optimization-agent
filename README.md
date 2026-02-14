# Code Optimization Agent

## Overview

This project implements a new agent for the Advisors Platform
responsible for analyzing Python code snippets and providing
optimization suggestions based on Python best practices.

The solution was built using FastAPI, PostgreSQL, and a simulated CrewAI
orchestration layer, following microservice architecture principles.

------------------------------------------------------------------------

## Architecture

-   FastAPI (REST API Layer)
-   PostgreSQL (Persistence Layer)
-   CrewAI Integration (Simulated Workflow)
-   Docker-ready structure
-   Kubernetes manifests available in /k8s
-   Modular project organization

Project structure:

app/ k8s/ scripts/ tests/ .env.example Dockerfile.worker
CREWAI_INTEGRATION.md

------------------------------------------------------------------------

## API Endpoints

### POST /analyze-code

Analyzes a Python code snippet and returns optimization suggestions.

Example Request:

{ "code": "for i in range(len(items)): print(items\[i\])" }

Example Response:

{ "suggestions": \[ "Use direct iteration instead of indexing.",
"Consider using enumerate() if index is needed." \] }

All analysis results are persisted in the database.

------------------------------------------------------------------------

### GET /health

Returns service health status.

{ "status": "ok" }

------------------------------------------------------------------------

## Database

PostgreSQL table: analysis_history

CREATE TABLE analysis_history ( id SERIAL PRIMARY KEY, code_snippet TEXT
NOT NULL, suggestions TEXT NOT NULL, created_at TIMESTAMP DEFAULT
CURRENT_TIMESTAMP );

------------------------------------------------------------------------

## Running Locally

1.  Clone repository

git clone <https://github.com/andreluispinto/code-optimization-agent.git>
cd code-optimization-agent

2.  Create virtual environment

python -m venv venv venv`\Scripts`{=tex}`\activate  `{=tex}(Windows)

3.  Install dependencies

pip install -r requirements.txt

4.  Configure environment variables

Copy .env.example to .env and configure PostgreSQL credentials.

5.  Run application

uvicorn app.main:app --reload

Access Swagger UI at:

http://localhost:8000/docs

------------------------------------------------------------------------

## CrewAI Integration (Simulation)

The agent simulates integration with CrewAI through a workflow
abstraction.

In a production scenario:

-   The agent would be registered as a CrewAI tool.
-   /analyze-code would be triggered inside a multi-agent workflow.
-   Orchestration would coordinate multiple advisors.

Details available in CREWAI_INTEGRATION.md

------------------------------------------------------------------------

## Scalability Strategy

Horizontal Scaling: - Docker containerization - Kubernetes deployment -
Stateless service design

Performance Enhancements: - Redis caching for repeated analysis - Async
processing with Celery + message broker - PostgreSQL connection pooling

Observability: - Structured logging - Metrics collection - Health check
endpoint for probes

------------------------------------------------------------------------

## Testing

Run tests:

pytest

Tests are located in the /tests directory.

------------------------------------------------------------------------

## Technical Decisions

FastAPI: - High performance (ASGI) - Automatic OpenAPI documentation -
Strong typing with Pydantic

PostgreSQL: - ACID compliance - Production reliability - Scalability
support

------------------------------------------------------------------------

## Future Improvements

-   LLM-based semantic analysis
-   Static analysis tool integration (flake8, pylint)
-   CI/CD pipeline
-   Cloud-native deployment (AWS, Azure, GCP)

------------------------------------------------------------------------

Author: Andre Luis Monteiro Pinto
