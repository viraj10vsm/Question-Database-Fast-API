# Question-Database-Fast-API
## Create Virtual Env--> download requirements--> connect MongoDB
## Start Server >$ uvicorn index:app --reload

# Interview Question API

This repository contains a FastAPI-based API that handles CRUD operations for managing interview questions. It also supports uploading a CSV file to insert multiple questions into the database in bulk.

## Table of Contents

- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
  - [Get All Questions](#1-get-all-questions)
  - [Create a New Question](#2-create-a-new-question)
  - [Update an Existing Question](#3-update-an-existing-question)
  - [Delete a Question](#4-delete-a-question)
  - [Upload Questions via CSV](#5-upload-questions-via-csv)
- [Models](#models)
- [Error Handling](#error-handling)
- [Conclusion](#conclusion)

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. Set up a virtual environment and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

3. Ensure that MongoDB is installed and running locally, or configure the connection to a remote MongoDB instance in your `config/db.py`.

4. Run the FastAPI server:
   ```bash
   uvicorn index:app --reload
   ```

5. Access the API documentation through the auto-generated Swagger UI at:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## API Endpoints

### 1. Get All Questions

- **Endpoint:** `GET /`
- **Description:** Retrieves all questions stored in the database.

- **Response:**
  ```json
  [
    {
      "_id": "60a6763f8d6e9c7c88d0fabe",
      "question": "What is a Python decorator?",
      "answer": "A Python decorator is...",
      "category": "Python",
      "difficulty": "Intermediate",
      "role": "Software Developer"
    },
    ...
  ]
  ```

### 2. Create a New Question

- **Endpoint:** `POST /`
- **Description:** Creates and inserts a new question into the database.

- **Request Body:**
  ```json
  {
    "question": "What is a Python lambda function?",
    "answer": "A lambda function is a small anonymous function...",
    "category": "Python",
    "difficulty": "Easy",
    "role": "Software Developer"
  }
  ```

- **Response:** Returns a list of all questions, including the newly created one.

### 3. Update an Existing Question

- **Endpoint:** `PUT /{id}`
- **Description:** Updates an existing question in the database based on the provided `id`.

- **Path Parameter:** `id` (The MongoDB ObjectId of the question to update)

- **Request Body:**
  ```json
  {
    "question": "What is the difference between a list and a tuple?",
    "answer": "A list is mutable, whereas a tuple is immutable...",
    "category": "Python",
    "difficulty": "Intermediate",
    "role": "Software Developer"
  }
  ```

- **Response:** Returns the updated question.

### 4. Delete a Question

- **Endpoint:** `DELETE /{id}`
- **Description:** Deletes an existing question from the database based on the provided `id`.

- **Path Parameter:** `id` (The MongoDB ObjectId of the question to delete)

- **Response:** Returns the deleted question.

### 5. Upload Questions via CSV

- **Endpoint:** `POST /upload_csv/`
- **Description:** Uploads a CSV file containing multiple questions and inserts them into the database in bulk.

- **Request:**
  - A CSV file uploaded via `multipart/form-data`. The CSV should contain the following columns:
    - `question`: The interview question.
    - `answer`: The answer to the question.
    - `category`: The question category (e.g., Python, JavaScript).
    - `difficulty`: Difficulty level (Easy, Intermediate, Hard).
    - `role`: Relevant role for the question (e.g., Software Developer, Data Scientist).

  - Example CSV format:
    ```csv
    question,answer,category,difficulty,role
    "What is a Python decorator?","A Python decorator is a function...", "Python", "Intermediate", "Software Developer"
    "What is polymorphism?","Polymorphism allows...", "OOP", "Intermediate", "Software Developer"
    ```

- **Response:**  
  - **Success:**
    ```json
    {
      "message": "Successfully inserted X questions into the database."
    }
    ```

  - **Error:**
    ```json
    {
      "error": "CSV file must contain the following columns: 'question', 'answer', 'category', 'difficulty', 'role'."
    }
    ```

---

## Models

### Question Model

The `Question` model defines the structure of the interview questions:
- `question`: String (The interview question text)
- `answer`: String (The corresponding answer or explanation)
- `category`: String (e.g., Python, JavaScript, etc.)
- `difficulty`: String (Easy, Intermediate, Hard)
- `role`: String (Relevant role, e.g., Software Developer, Data Scientist)

---

## Error Handling

Common errors that can occur during API usage:

1. **Invalid ID Format:**
   ```json
   {
     "error": "Invalid ObjectId format"
   }
   ```

2. **CSV Column Validation Error:**
   ```json
   {
     "error": "CSV file must contain the following columns: 'question', 'answer', 'category', 'difficulty', 'role'."
   }
   ```

---

## Conclusion

This API provides functionality to manage interview questions in a MongoDB database with CRUD operations and bulk CSV uploads. Follow the defined data structure to avoid errors. You can explore the available endpoints and test them using the interactive Swagger UI.
