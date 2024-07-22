Weather Data Aggregator and Analyzer
Table of Contents
Introduction
Features
Setup
Running the Application
Usage
Code Structure
Comments and Docstrings
Introduction
The Weather Data Aggregator and Analyzer is a Python web application that allows users to fetch, visualize, and analyze weather data in real-time. The application fetches data from the OpenWeatherMap API, stores it in a MySQL database, and provides various visualizations and analyses through a Flask web interface.

Features
Fetch Weather Data: Retrieve the latest weather data from the OpenWeatherMap API.
Visualize Data: Display weather trends over time using line charts.
Analyze Data: Perform statistical analysis on the collected weather data.
Setup
Prerequisites
Python 3.6 or higher
MySQL Server
A virtual environment tool (optional but recommended)
Installation Steps
Clone the Repository

sh
Copy code
git clone https://github.com/yourusername/weather-data-aggregator.git
cd weather-data-aggregator
Create a Virtual Environment

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

sh
Copy code
pip install -r requirements.txt
Setup MySQL Database

Create a MySQL database named weather_data.
Update the config.py file with your MySQL credentials:
python
Copy code
DB_CONFIG = {
    'user': 'root',
    'password': 'yourpassword',
    'host': 'localhost',
    'database': 'weather_data',
    'port': 3306,
    'raise_on_warnings': True
}
Create Required Tables

Run the following SQL command to create the necessary table:
sql
Copy code
CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT
);
Update API Key

Update the fetch_weather.py file with your OpenWeatherMap API key:
python
Copy code
API_KEY = 'your_openweathermap_api_key'
Running the Application
Start the Flask Application
sh
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/.
Usage
Home Page: Provides an overview and navigation to different functionalities.
Fetch Data: Click on "Fetch Data" to retrieve the latest weather data.
Visualize Data: Click on "Visualize Data" to see weather trends in graphical format.
Analyze Data: Click on "Analyze Data" to perform statistical analysis and view histograms of temperature and humidity.
Code Structure
app.py: Main Flask application file.
fetch_weather.py: Contains the function to fetch weather data from the API.
config.py: Contains database configuration details.
templates/: Directory containing HTML templates.
base.html: Base template.
index.html: Home page template.
visualize.html: Template for visualizing data.
analyze.html: Template for analyzing data.
static/: Directory containing static files like CSS, JavaScript, and images.
css/: Custom CSS files.
js/: Custom JavaScript files.
images/: Images used in the project.
