# Weather Data Aggregator and Analyzer

Weather Data Aggregator![Weather Data Aggregator and Analyzer - Brave 22-07-2024 11_25_02](https://github.com/user-attachments/assets/73c17776-c465-4aec-8f47-bd85fff45c82)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Comments and Docstrings](#comments-and-docstrings)

## Introduction
The Weather Data Aggregator and Analyzer is a Python web application that allows users to fetch, visualize, and analyze weather data in real-time. The application fetches data from the OpenWeatherMap API, stores it in a MySQL database, and provides various visualizations and analyses through a Flask web interface.

## Features
- **Fetch Weather Data**: Retrieve the latest weather data from the OpenWeatherMap API.
- **Visualize Data**: Display weather trends over time using line charts.
- **Analyze Data**: Perform statistical analysis on the collected weather data.

## Setup

### Prerequisites
- Python 3.6 or higher
- MySQL Server
- A virtual environment tool (optional but recommended)

### Installation Steps

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/weather-data-aggregator.git
    cd weather-data-aggregator
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Setup MySQL Database**
    - Create a MySQL database named `weather_data`.
    - Update the `config.py` file with your MySQL credentials:
      ```python
      DB_CONFIG = {
          'user': 'root',
          'password': 'yourpassword',
          'host': 'localhost',
          'database': 'weather_data',
          'port': 3306,
          'raise_on_warnings': True
      }
      ```

5. **Create Required Tables**
    - Run the following SQL command to create the necessary table:
      ```sql
      CREATE TABLE weather (
          id INT AUTO_INCREMENT PRIMARY KEY,
          timestamp DATETIME,
          temperature FLOAT,
          humidity INT,
          wind_speed FLOAT
      );
      ```

6. **Update API Key**
    - Update the `fetch_weather.py` file with your OpenWeatherMap API key:
      ```python
      API_KEY = 'your_openweathermap_api_key'
      ```

## Running the Application

1. **Start the Flask Application**
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- **Home Page**: Provides an overview and navigation to different functionalities.
  ![Home Page](https://github.com/user-attachments/assets/ed75b5ce-813f-4cfe-86d0-016401439f98)
  
- **Fetch Data**: Click on "Fetch Data" to retrieve the latest weather data.
  ![Fetch Data](https://github.com/user-attachments/assets/6a094234-a92c-45be-a055-f174443b6907)
  
- **Visualize Data**: Click on "Visualize Data" to see weather trends in graphical format.
  ![Visualize Data](https://github.com/user-attachments/assets/0a8cd602-43ad-49d0-8006-6814dc88802f)
  
- **Analyze Data**: Click on "Analyze Data" to perform statistical analysis and view histograms of temperature and humidity.
  ![Analyze Data](https://github.com/user-attachments/assets/b50651d6-41ee-407d-983c-06aac1c73b4e)

## Code Structure

- `app.py`: Main Flask application file.
- `fetch_weather.py`: Contains the function to fetch weather data from the API.
- `config.py`: Contains database configuration details.
- `templates/`: Directory containing HTML templates.
  - `base.html`: Base template.
  - `index.html`: Home page template.
  - `visualize.html`: Template for visualizing data.
  - `analyze.html`: Template for analyzing data.
- `static/`: Directory containing static files like CSS, JavaScript, and images.
  - `css/`: Custom CSS files.
  - `js/`: Custom JavaScript files.
  - `images/`: Images used in the project.

## API Reference

![UML_Diagram](https://github.com/user-attachments/assets/8cfa22b5-4919-4477-9233-0b122b7b4343)

## Authors

- [Aniket Chaudhari](https://github.com/Aniket12xfe)
