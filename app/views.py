from flask import request, jsonify
import pandas as pd
import psycopg2
import configparser
from app import app
from scipy import stats


config = configparser.ConfigParser()
config.read('config/dev_configurations.ini')


@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'})

    # Read the CSV file using Pandas
    df = pd.read_csv(file)

    # Perform outlier detection
    outlier_indices = detect_outliers(df['value'])

    # Remove outliers from the DataFrame
    df_cleaned = df.drop(outlier_indices)

    # Create a table with inferred data types in SQL
    table_name = 'my_table'
    create_table_sql = generate_create_table_sql(df_cleaned, table_name)
    insert_data_sql = generate_insert_data_sql(df_cleaned, table_name)

    # Connect to the SQL database
    conn = psycopg2.connect(
        host=config['database']['host'],
        port=config.getint('database', 'port'),
        dbname=config['database']['dbname'],
        user=config['database']['user'],
        password=config['database']['password']
    )
    cur = conn.cursor()

    # Create the table
    cur.execute(create_table_sql)

    # Insert the data into the table
    cur.execute(insert_data_sql)

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Data uploaded successfully'})


def detect_outliers(data):
    z_scores = stats.zscore(data)
    threshold = 3
    outlier_indices = (z_scores > threshold).nonzero()[0]
    return outlier_indices


def generate_create_table_sql(df, table_name):
    columns = []
    for column, dtype in df.dtypes.iteritems():
        if dtype == 'object':
            columns.append(f"{column} TEXT")
        elif dtype == 'int64':
            columns.append(f"{column} INTEGER")
        elif dtype == 'float64':
            columns.append(f"{column} FLOAT")
        elif dtype == 'datetime64[ns]':
            columns.append(f"{column} TIMESTAMP")
        else:
            columns.append(f"{column} TEXT")

    create_table_sql = f"CREATE TABLE {table_name} ({', '.join(columns)});"
    return create_table_sql


def generate_insert_data_sql(df, table_name):
    insert_data_sql = f"COPY {table_name} FROM STDIN DELIMITER ',' CSV HEADER;"
    return insert_data_sql
