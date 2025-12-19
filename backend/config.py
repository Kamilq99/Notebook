from db_connect.elasticsearch_connect import elasticsearch_connect, create_index

def init_app_config(app):
    es = elasticsearch_connect()
    create_index(es, 'notes')

    app.config['ES'] = es
    app.config['NOTES_INDEX'] = 'notes'
