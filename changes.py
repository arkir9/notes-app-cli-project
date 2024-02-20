import sqlite3

# def add_user_id_column():
  
#     conn = sqlite3.connect('notes.db')
#     cursor = conn.cursor()

  
#     alter_query = """
#     ALTER TABLE notes
#     ADD COLUMN user_id INTEGER;
#     """
#     cursor.execute(alter_query)

  
#     conn.commit()
#     conn.close()

# def add_category_id_column():
  
#     conn = sqlite3.connect('notes.db')
#     cursor = conn.cursor()


#     alter_query = """
#     ALTER TABLE notes
#     ADD COLUMN category_id INTEGER;
#     """
#     cursor.execute(alter_query)

  
#     conn.commit()
#     conn.close()

def delete_table():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()


    alter_query = """
    DROP TABLE note_category_association
    """
    cursor.execute(alter_query)

  
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # add_user_id_column()
    # add_category_id_column()
    delete_table()
