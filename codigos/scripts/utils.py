from __future__ import generators
from os import path, devnull, listdir
from os.path import isfile, join
from pyhive import hive
import pandas as pd
import numpy as np
import csv

def ResultIter(cursor, arraysize=1000, bucket=False):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            cursor.close()
            break
        if bucket:
            yield results
        else:
            for result in results:
                yield result


class Connection(object):

    def __init__(self):
        print("Class Connection - init...")
        self.read_conn = None

    def openHiveConnection(self, database):
        print("class Connection - openHiveConnection...")
        try:
            self.config_db = {'host':'10.21.0.70', 'port':'10500', 'username':'trilhasgsi', 'password':'UFMGtrilhas2020', 'auth':'CUSTOM'}
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

    def __call__(self, query, size=1000, bucket=False):
        read_cur = self.read_conn.cursor()
        #read_cur.open()
        read_cur.execute(query)
        return ResultIter(read_cur, arraysize=size, bucket=bucket) 

    def showTablesQuery(self):
        return 'SHOW TABLES'



def main():
    conn = Connection()
    conn.openHiveConnection("mdm_v2")
    
    getTables = f'''show tables in mdm_v2'''
    tables = conn.executeQueryDB(getTables)

    print("Show Tables:\n")
    print(tables)
    #get_sample = f''' SELECT * FROM  mdm_v2.mdm_pessoa_dataset_carga_confiavel TABLESAMPLE (5 ROWS) '''    
    get_sample = f''' SELECT * FROM mdm_pessoa_dataset_carga_confiavel_blocagem LIMIT 10000'''
    #sample = conn.executeQueryDB(get_sample)
    for i, t in enumerate(conn(get_sample)):
        print( i, t)
        break
    for i,t in enumerate(conn(get_sample, bucket=True)):
        print(i, len(t), len(t[0]))
    #print("count", sample)
if __name__ == '__main__':
    main()
