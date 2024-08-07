# Weather Data Aggregator and Analyzer

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [API Reference](#api-reference)

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
        timestamp DATETIME NOT NULL,
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        wind_speed FLOAT NOT NULL
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
```
weather-data-aggregator/
│
├── app.py
├── config.py
├── fetch_weather.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── overview.png
│   │   ├── home_page.png
│   │   ├── fetch_data.png
│   │   ├── visualize_data.png
│   │   └── analyze_data.png
│   └── js/
│       └── scripts.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── visualize.html
│   ├── analyze.html
│   └── pie.html
└── README.md
```

## API Reference

![UML_Diagram](https://github.com/user-attachments/assets/8cfa22b5-4919-4477-9233-0b122b7b4343)

## Authors

- [Aniket Chaudhari](https://github.com/Aniket12xfe)
