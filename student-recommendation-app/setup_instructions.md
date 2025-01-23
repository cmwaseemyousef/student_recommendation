# Setup Instructions for Student Recommendation App

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**
   Open your terminal and run the following command to clone the repository:
   ```
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the URL of the repository.

2. **Navigate to the Project Directory**
   Change your directory to the project folder:
   ```
   cd student-recommendation-app
   ```

3. **Create a Virtual Environment (Optional but Recommended)**
   It is recommended to create a virtual environment to manage dependencies:
   ```
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Required Packages**
   Install the necessary dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Application**
   Run the main application script:
   ```
   python src/main.py
   ```

2. **Follow the Prompts**
   The application will guide you through the process of analyzing quiz performance and generating recommendations.

## Usage Guidelines
- Ensure that you have access to the quiz data endpoints as specified in the project documentation.
- Review the README.md for additional information on the project structure and functionalities.

## Troubleshooting
If you encounter any issues, please check the following:
- Ensure all dependencies are installed correctly.
- Verify that you are using the correct version of Python.
- Consult the README.md for further guidance on project usage.

# Setup Instructions

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the main script:
    ```bash
    python src/main.py
    ```