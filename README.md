# Auraa ERP - Getting Started

This project is built using Django 5, Celery, and a modular architecture. It is designed to be run in a containerized environment.

## Prerequisites
- Docker & Docker Compose
- Git

## 1. Environment Setup
The project is configured to use **Docker-containerized services** for the database, cache, and search. 
- **DB Name**: `auraacrackers` (Containerized)
- **User/Pass**: `auraauser` / `auraapass`

This ensures a consistent development environment across different machines.

## 2. Build and Start
Run the following command to build the images and start all services (Postgres, Redis, Celery, Web, etc.):

```bash
docker-compose up --build
```

## 3. Database Initialization
Once the containers are running, execute the migrations and create a superuser:

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser (Admin)
docker-compose exec web python manage.py createsuperuser
```

## 4. Accessing Services
- **Web Application**: [http://localhost:8000](http://localhost:8000)
- **API Documentation (Swagger)**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- **Celery Flower (Monitoring)**: [http://localhost:5566](http://localhost:5566) (Note: Add flower to docker-compose if needed)
- **Mailhog (Email Catcher)**: [http://localhost:8025](http://localhost:8025)
- **MinIO (Object Storage)**: [http://localhost:9001](http://localhost:9001) (Console)
- **Meilisearch**: [http://localhost:7700](http://localhost:7700)

## 5. Development Commands
- **Run Tests**: `docker-compose exec web pytest`
- **Linting**: `docker-compose exec web ruff check .`
- **Enter Web Container**: `docker-compose exec web bash`
