from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

def elasticsearch_connect():
    es_usename = os.getenv('ELASTIC_USER')
    es_password = os.getenv('ELASTIC_PASSWORD')
    
    es = Elasticsearch(
        "http://localhost:9200",
        http_auth=(es_usename, es_password)
    )

    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Could not connect to Elasticsearch")
    
    return es

def create_index(es, index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Index '{index_name}' created")
    else:
        print(f"Index '{index_name}' already exists. Ready to insert data.")
