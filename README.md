# Student_AI

## Overview

Student_AI is a Python-based project designed to fetch, process, and analyze quiz data from various APIs. It includes functionalities for data cleaning, visualization, and generating student personas based on quiz performance. Additionally, it leverages AI models to provide insights and improvement suggestions for students based on their quiz results.

## Project Structure

The project consists of the following main components:

- **Study.py**: Contains utility functions for fetching, flattening, cleaning, and filtering JSON data from APIs. It also includes functions for processing specific APIs and generating cleaned data.
- **Persona.py**: Generates a student persona based on quiz performance data stored in a CSV file.
- **Data_viz.py**: Provides functions for loading quiz data and creating various visualizations to analyze student performance.
- **AI_Pattern.py**: Utilizes the Groq AI model to analyze student performance and suggest improvement strategies based on quiz results.
- **requirements.txt**: Lists the required Python packages for the project.
- **quiz_results_cleaned.csv**: A sample CSV file containing cleaned quiz results data.
- **api_1_cleaned.json**: A sample JSON file containing cleaned data from API 1.
- **api_2_cleaned.json**: A sample JSON file containing cleaned data from API 2.

## Installation

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Create a .env file:
    ```
    GROQ_API_KEY = "YOUR API KEY"
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Processing API Data

1. Run the `Study.py` script to fetch, process, and clean data from the APIs:
    ```bash
    python Study.py
    ```

   This will generate `api_1_cleaned.json`, `api_2_cleaned.json`, and `quiz_results_cleaned.csv` files.

### Generating Student Persona

1. Run the `Persona.py` script to generate a student persona based on the cleaned quiz results:
    ```bash
    python Persona.py
    ```

   This will print the generated student persona details to the console.

### Data Visualization

1. Run the `Data_viz.py` script to create visualizations of the quiz data:
    ```bash
    python Data_viz.py
    ```

   This will display various plots analyzing the student performance. In the visualizations folder, check for some sample graphs

### AI-Based Analysis and Suggestions

1. Ensure you have your Groq API key set up in the environment. If not, the script will prompt you to enter it.
2. Run the `AI_Pattern.py` script to analyze student performance and get improvement suggestions:
    ```bash
    python AI_Pattern.py
    ```

   This will print the AI-generated insights and improvement plan to the console.


### Documentation

The word Document file consists of thought process and design.

