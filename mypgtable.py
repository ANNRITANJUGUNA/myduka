import psycopg2

try:
    conn = psycopg2.connect("dbname=myduka user=postgres password=1234")
    cur = conn.cursor()
except Exception as edu:
   print(edu)

def fetch_data(tbln):
    try:
       q="SELECT * FROM " + tbln + ";"
       cur.execute(q)
       records=cur.fetchall()
       return records
    except Exception as e:
       return e
 
def insert_product(v):
   vs=str(v)
   q= "insert into sales(id,pid,stock_quantity,date created)"\
       "values"+vs 
   cur.execute(q)
   conn.commit()
   
   return "product successfully installed"