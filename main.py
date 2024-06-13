from display_menu import show_app_menu
from db_handlers import create_db,create_table, seed_db
from db.data_import import records

if __name__ == "__main__":
    # creates db, returns connection obj.
    db_conn = create_db()
    create_table(db_connector=db_conn, sql_="boxes")
    create_table(db_connector=db_conn, sql_="freights")
    create_table(db_connector=db_conn, sql_="containers")
    seed_db(records, db_conn)
    db_conn.close()
