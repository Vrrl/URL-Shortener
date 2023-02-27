# Url Shortener
This project is a URL shortener implemented using Python 3.9+ and the FastAPI web framework. The purpose of the project is to serve as an example for implementing continuous integration and deployment (CI/CD) practices, such as automated testing and automated production deployment.

The project follows some principles of Clean Architecture and Domain-Driven Design (DDD) to ensure a separation of concerns and maintainability of the codebase. It also includes code linters such as flake8 and Black to ensure consistency and readability of the code, and pre-commit hooks to run the linters and tests before committing to the Git branch.

# Installation
To install the project dependencies, simply run:

```bash
pip install -r requirements.txt
```

# Usage
To run the application in development mode, use the following command:

```bash
uvicorn src.web.server:app --reload
```
This will start the server at `http://localhost:8000/`.

To save a new URL, make a POST request to the /save endpoint with a JSON payload containing the URL to be shortened:

```http
POST /save HTTP/1.1
Content-Type: application/json

{
"url": "https://www.example.com/very/long/url/that/needs/to/be/shortened"
}
```
This will return a JSON response with a unique key for the shortened URL:

```json
{
"key": "abc123"
}
```
To access the original URL, make a GET request to the /key endpoint, where key is the unique key returned from the /save endpoint:

```http
GET /abc123 HTTP/1.1
```
This will redirect you to the original URL.

# Testing
To run the tests, use the following command:

```bash
pytest -v -s .
```
This will run all tests and output the results to the console.

# API Documentation
The API documentation can be accessed by visiting the /docs endpoint, which will open the Swagger UI in your browser. This UI provides an interactive interface to explore and test the API endpoints.

# CI/CD
The CI/CD configuration for this project is located in the .gitlab-ci.yml file. This configuration specifies the steps for running the tests and deploying the application to a production environment. These steps are automatically executed when changes are pushed to the Git branch.