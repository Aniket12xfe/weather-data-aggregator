CREATE DATABASE weather_data;

USE weather_data;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL
);

select * from weather;