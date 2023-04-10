"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-cgprf25269v5rj8b6ndg-a.oregon-postgres.render.com",
    database="tasks_k037",
    user="tasks_k037_user",
    password="y5q4yzJPAdsV3J4GfZzudQEvWwFBzz7b")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
