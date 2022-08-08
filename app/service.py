import imp
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from db import db_config, db_queries
from flask import jsonify
import datetime

def create_db_connection():
    """
        return : database connection object
    """
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
        (db_config["host"], db_config["username"],
         db_config["password"], db_config["database"])

    db_conn = connect(conn_string)
    return db_conn

def check_request_params(origin,destination,date_from,date_to):
    if not (origin and destination):
        return False, "Incorrect input for origin or destination"
    try:
        datetime.datetime.strptime(str(date_from), '%Y-%m-%d')
        datetime.datetime.strptime(str(date_to), '%Y-%m-%d')
    except Exception as e:
        return False, "Incorrect date format, should be YYYY-MM-DD"
    return True, "valid input params"

def convert_row_to_rate(row):
    """params:
        row : database query respose

       returns : json object
    """
    return {
        "day": row["day"].strftime('%Y-%m-%d'),
        "average_price": round(float(row["price"]), 2) if row["price"] is not None else None
    }


db_conn = create_db_connection()


def get_rates(origin,destination,date_from,date_to):
    """
       returns : final rates response in json formate
    """
    params = {
                "date_from": date_from,
                "date_to": date_to,
                "origin": origin,
                "destination": destination
    }
    cursor = db_conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(db_queries.get('get_rates'), params)
    response = cursor.fetchall()
    rates = [convert_row_to_rate(row) for row in response]
    return jsonify({"rates": rates})