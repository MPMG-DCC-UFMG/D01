from os import path, devnull, listdir
from os.path import isfile, join
from pyhive import hive
import pandas as pd
import numpy as np
import csv

class Connection(object):

    def __init__(self):
        print("Class Connection - init...")
        self.read_conn = None

    def openHiveConnection(self, database):
        print("class Connection - openHiveConnection...")
        try:
            self.config_db = {'host':'*****', 'port':'*****', 'username':'******', 'password':'******', 'auth':'****'}
            self.config_db.update({'database': database})
            #print("self.config_db", self.config_db)
            self.read_conn = hive.connect(**self.config_db)
            if self.read_conn is None:
                    print("Hive connection failed!")
                    exit(2)
            else:
                    print ("Hive connection is working. DB = ", database)
        except:
            print("Hive connection failed!")
            exit(2)

    def closeHiveConnectin(self):
        print("class Connection - closeHiveConnectin...")
        try:
            self.read_conn.close()
        except:
            print("Hive connection coould not close correctly...")
            exit(2)

    def executeQueryDB(self, query):
        print("class Connection - executeQueryDB...")
        with self.read_conn.cursor() as read_cur:
            read_cur.execute(query)
            result_query = read_cur.fetchall()
        return result_query

    def showTablesQuery(self):
        return 'SHOW TABLES'



def main():
    conn = Connection()
    conn.openHiveConnection()
    
    getTables = f'''show tables in mdm_v2'''
    tables = conn.executeQueryDB(getTables)

    print("Show Tables:\n")
    print(getTables)

if __name__ == '__main__':
    main()