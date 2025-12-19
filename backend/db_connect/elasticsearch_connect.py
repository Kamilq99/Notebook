from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

db_ussername = os.getenv("ELASTIC_USER")
db_password = os.getenv("ELASTIC_PASSWORD")

es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=(db_ussername, db_password)
)

def test_connection():
    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Could not connect to Elasticsearch")