import os

import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
from flask import Flask, render_template, request

from config import DB_CONFIG
from fetch_weather import fetch_weather_data

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/fetch')
def fetch():
    fetch_weather_data()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature, humidity FROM weather")
    data = cursor.fetchall()
    conn.close()

    if not data:
        return "No data available for visualization."

    dates = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    humidities = [row[2] for row in data]

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=dates, y=temperatures, label='Temperature')
    sns.lineplot(x=dates, y=humidities, label='Humidity')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Weather Trends')

    if not os.path.exists('static'):
        os.makedirs('static')

    image_path = 'static/weather_trends.png'
    plt.savefig(image_path)
    plt.close()

    return render_template('visualize.html', image='weather_trends.png')


@app.route('/visualize', methods=['GET', 'POST'])
def visualize():
    conn = get_db_connection()
    cursor = conn.cursor()

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        cursor.execute(
            "SELECT timestamp, temperature, wind_speed FROM weather WHERE timestamp BETWEEN %s AND %s",
            (start_date, end_date)
        )
    else:
        cursor.execute("SELECT timestamp, temperature, wind_speed FROM weather")

    data = cursor.fetchall()
    conn.close()

    if not data:
        return "No data available for visualization."

    dates = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    wind_speed = [row[2] for row in data]

    # Example of aggregating data for a specific date (e.g., first date in the list)
    specific_date = dates[0]  # Replace with the date you're interested in
    specific_temp = temperatures[dates.index(specific_date)]
    specific_wind = wind_speed[dates.index(specific_date)]

    # Data for the pie chart
    labels = ['Temperature', 'Wind Speed']
    sizes = [specific_temp, specific_wind]
    colors = ['skyblue', 'orange']
    explode = (0.1, 0)  # explode the first slice

    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f'Weather Distribution on {specific_date}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save and show the pie chart
    pie_chart_path = 'static/weather_pie_chart.png'
    plt.savefig(pie_chart_path)
    plt.close()
    # plt.show()

    return render_template('pie.html', image_pie='weather_pie_chart.png')


@app.route('/analyze')
def analyze():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature, humidity FROM weather")
    data = cursor.fetchall()
    conn.close()

    if not data:
        return "No data available for analysis."

    temperatures = [row[1] for row in data]
    humidities = [row[2] for row in data]
    #
    avg_temp = sum(temperatures) / len(temperatures)
    avg_humidity = sum(humidities) / len(humidities)

    avg_temp_formatted = "{:.2f}".format(avg_temp)
    avg_humidity_formatted = "{:.2f}".format(avg_humidity)

    # Plot histogram of temperatures
    plt.figure(figsize=(10, 5))
    sns.histplot(temperatures, kde=True, bins=30, color='blue')
    plt.xlabel('Temperature')
    plt.title('Temperature Distribution')
    temp_hist_path = 'static/temp_histogram.png'
    plt.savefig(temp_hist_path)
    plt.close()
    # dates = [row[0] for row in data]
    # temperatures = [row[1] for row in data]
    #
    # # Plot bar graph
    # plt.figure(figsize=(10, 5))
    # plt.barh(dates, temperatures, color='blue', alpha=0.7)
    # plt.xlabel('Temperature')
    # plt.ylabel('Date')
    # plt.title('Temperature Distribution Over Dates')
    #
    # # Save and show the bar graph
    # temp_bar_path = 'static/temp_bar_graph.png'
    # plt.savefig(temp_bar_path)
    # plt.close()

    # Plot histogram of humidity
    plt.figure(figsize=(10, 5))
    sns.histplot(humidities, kde=True, bins=30, color='green')
    plt.xlabel('Humidity')
    plt.title('Humidity Distribution')
    humidity_hist_path = 'static/humidity_histogram.png'
    plt.savefig(humidity_hist_path)
    plt.close()

    return render_template('analyze.html', avg_temp=avg_temp_formatted, avg_humidity=avg_humidity_formatted,
                           temp_hist='temp_histogram.png', humidity_hist='humidity_histogram.png')


if __name__ == '__main__':
    app.run(debug=True)
