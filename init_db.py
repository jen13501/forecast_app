import database as database

def main():
   conn = database.get_connection()

   with open('schema.sql') as f:
      conn.executescript(f.read())

   conn.commit()
   conn.close()

if __name__=="__main__":
    main()