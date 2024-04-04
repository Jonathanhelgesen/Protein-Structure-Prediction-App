# Setup Guide

This guide will explain how to run the web application for predicting the secondary structure of proteins. The application consists of two main parts: the backend, built with Flask, and the frontend, developed with React.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.8 or newer)
- pip (Python package installer)
- Node.js (14.x or newer)
- npm (Node package manager)

## Setup Instructions

### Backend Setup (Flask Application)

1. **Navigate to the Backend Directory:**

   Given that you are already in the project directory, change to the backend directory through the terminal:

   ```bash
   cd backend
   ```

2. **Create a Virtual Environment:**

   If you already haven't, create a virtual environment for the Flask application:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   Before installing dependencies, activate the virtual environment:

   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   Install all required packages using pip by running the following command in your activated virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

5. **Start the Flask Application:**

   Run the Flask application by executing:

   ```bash
   python app.py
   ```

   By default, the Flask app will run on `http://localhost:5000`. You can access the API endpoints at this base URL.

### Frontend Setup (React Application)

1. **Navigate to the Frontend Directory:**

   Open a new terminal window or tab and change to the frontend directory where the React application is:

   ```bash
   cd path/to/frontend
   ```

2. **Install Dependencies:**

   Use npm to install the necessary dependencies for the React app if you already haven't done it before:

   ```bash
   npm install
   ```

3. **Start the React Application:**

   Once the dependencies are installed, you can start the React application by running:

   ```bash
   npm start
   ```

   This command starts the React development server, typically on `http://localhost:3000`. Your default web browser should automatically open and navigate to this URL.

## Accessing the Application

With both the backend and frontend running, you can interact with the application through your web browser at `http://localhost:3000`. The React frontend will communicate with the Flask backend to serve dynamic content.

## Troubleshooting

- Ensure both the backend and frontend directories are correctly navigated to when running their respective commands.
- Make sure the virtual environment for the Flask app is activated before installing dependencies or starting the app.
- Check that all dependencies are installed in both the frontend and backend before attempting to start the applications.
