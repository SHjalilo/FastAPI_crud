import psycopg2
import json
#----------------------------------------------
#add this dictionary for configuration to connect with database so easy !
# change XXXXXX with your informatition don't forget that !?
config = {
    "host":"XXXXXX",
    "database":"XXXXXX",
    "user":"XXXXXX",
    "password":"XXXXXX"
}
#----------------------------------------------

#----------------------------------------------
# get Data From database .
def getData(query):
    try:
        con = psycopg2.connect(**config)
        print("Connection open successfully !")
        try:
            cur = con.cursor()
            cur.execute(query)
        except:
            print("Query failed !")
            # raise : for stopping proc ?
            raise
        else:
            rows = cur.fetchall()
            #return json.dumps(rows) 
            return rows
        finally:
            cur.close()
            con.close()
            print("Connection closed !")
    except Exception as e:
        print("Something went wrong",e)
#----------------------------------------------
# Set data to database 
def setData(query):
    try:
        con = psycopg2.connect(**config)
        print("Connection open successfully !")
        try:
            cur = con.cursor()
            cur.execute(query)
        except:
            print("Query failed !")
            # raise : for stopping proc ?
            raise
        else:
            con.commit()
        finally:
            cur.close()
            con.close()
            print("Connection closed !")
    except Exception as e:
        print("Something went wrong",e)

#----------------------------------------------