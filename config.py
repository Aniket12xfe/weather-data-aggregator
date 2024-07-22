# config.py
DB_CONFIG = {
    'user': 'root',                # Replace with your MySQL username
    'password': 'Aniket@123',      # Replace with your MySQL password
    'host': 'localhost',
    'database': 'weather_data',
    'port': 3306,                  # Default MySQL port
    'raise_on_warnings': True
}


# Create a connection URI from the configuration dictionary
def get_database_uri():
    config = DB_CONFIG
    return f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
