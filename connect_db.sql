def connect_db():
    sql=sqlite3.connect('F:\\IIIT Bhubaneswar\\ML\\FoodTracker\\food_log.db')
    sql.row_factory=sqlite3.Row  // converting tuples to dictionaries
    return sql

def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite3_db=connect_db
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()