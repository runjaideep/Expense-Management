# Expense Management System

This project implements an Expense Management System with a **Streamlit** frontend and a **FastAPI** backend. The system allows users to manage their expenses through a responsive web interface, supported by a powerful and scalable backend server.

## Project Structure

- **frontend/**: Contains the code for the Streamlit application that serves as the user interface.
- **backend/**: Contains the FastAPI backend server code, including API endpoints and business logic.
- **tests/**: Contains unit and integration test cases for both frontend and backend components.
- **requirements.txt**: Lists the Python packages required to run the application.
- **README.md**: Provides an overview of the project and setup instructions.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```

2. **Install dependencies**:
   Install required dependencies for both frontend and backend:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:
   Launch the FastAPI backend server:
   ```bash
   uvicorn backend.server:app --reload
   ```

4. **Run the Streamlit app**:
   Start the frontend Streamlit application:
   ```bash
   streamlit run frontend/app.py
   ```

## Testing

- **Unit tests**: Ensure unit tests are implemented and tested for individual modules.
- **Integration tests**: Run integration tests to verify the interactions between the frontend and backend.
- To run the tests:
   ```bash
   pytest tests/
   ```
