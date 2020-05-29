# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
sys.path[0] = str(Path(__file__).resolve().parents[2]) # Set path for custom modules
import click
import logging
from dotenv import find_dotenv, load_dotenv
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'; turn off SettingWithCopyWarning
import psycopg2
from src.toolkits.sql import connect_db, add_columns, update_table_values, fetch_data, compare_column_order # Import custom sql functions
from src.toolkits.eda import save_csv # Import custom eda functions

# Get project root directory
project_dir = str(Path(__file__).resolve().parents[2])


def main():
    
    # Fetch data
    csv_path = project_dir + '/data/interim/permits_geocoded.csv'
    print("Reading csv...")
    data = pd.read_csv(csv_path)
    print(data.head().iloc[:,-3:])

    conn = connect_db()

    #add_columns(data, DB_TABLE, conn, run=True);

    compare_column_order(data, DB_TABLE, con=conn, match_inplace=True)

    print(data.head().iloc[:,-4:])
    print(fetch_data('SELECT * FROM {} LIMIT 500;'.format(DB_TABLE), conn).head().iloc[:,-4:])
    # # Resave with reordered columns
    # save_csv(data, data_path, match_db_order=True);

    # # Path for sql query
    # sql_path = project_dir + '/postgres/sql/update_table_values.sql'

    # Path to mounted data volume inside Docker container
    #container_path = '/var/local/data/interim/permits_geocoded.csv' # Path within container for COPY command

    # update_table_values(DB_TABLE, con=conn, data_path=container_path, sql_path=sql_path, run=True);

    return



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    # only works in Python 3.6.1 and above

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    # Set environment variables
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")
    DATA_URL = os.getenv("DATA_URL")
    DB_TABLE = "permits_raw"

    main()

    ### Check success
    # Connect to db
    # conn = connect_db()

    # # Extract partial dataset
    # sql = 'SELECT * FROM {} LIMIT 500;'.format(DB_TABLE)

    # # Fetch data
    # data = fetch_data(sql, conn)

    # # Display
    # print(data.head())