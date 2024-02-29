from mysql.connector import connect, Error
from main import DB_HOST, DB, DB_USER, DB_PWD


def connect_db():
    try:
        cnx = connect(host=DB_HOST, database=DB, user=DB_USER, password=DB_PWD)
        return cnx
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


def some_func():
    cnx = connect_db()
    if cnx:
        cursor = cnx.cursor()
        query = ("SELECT DISTINCT Devicetype FROM sitemaster")
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            query = (f"SELECT smSitecode,smSiteID FROM sitemaster WHERE Devicetype={row[0]}")
            cursor.execute(query)
            dv_unique_ids = cursor.fetchall()
            print(dv_unique_ids)  # You may remove this if not needed
            # for row in dv_unique_ids:
            #     if row[0]:
            #         dv_id=row[0]
            #         print(dv_id)
            #         query = (f"SELECT * FROM trans_latestdata WHERE dvuniqueid={dv_id}")
            #         sm_site_data = cursor.fetchall()
            #         print(sm_site_data)
        cnx.close()


some_func()
