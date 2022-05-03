#!/usr/bin/python3

import pymysql
import os

def make_umls_mrconso_term(mysql_info,save_path="umls_lui_nodes.csv",save_folder=""):
    if save_folder!="":
        save_path=os.path.join(save_folder,save_path)
    if os.path.exists(save_path):
        print(f"{save_path} exists!")
        return
    # open db connection
    db = pymysql.connect(host=mysql_info["hostname"], user=mysql_info["username"], password=mysql_info["password"], database=mysql_info["database"])

    cursor = db.cursor()

    sql = "SELECT distinct LUI FROM mrconso"
    sql_count = "SELECT count(distinct LUI) FROM mrconso"

    # write file
    header = ":ID,:LABEL,LUI\n"

    fo = open(save_path, 'w', encoding='utf-8')

    cursor.execute(sql_count)
    count = cursor.fetchone()[0]
    batch_size = 10 * 10000  # whatever

    print("total record count: " + str(count))

    counter = 0
    fo.write(header)
    for offset in range(0, count, batch_size):
        cursor.execute(sql + " LIMIT %s OFFSET %s", (batch_size, offset))

        # obtain a list of column names
        cols = cursor.description
        list_cols = []
        for i in range(len(cols)):
            list_cols.append(cols[i][0])
        print(list_cols)

        for row in cursor:
            # ID
            LUI = row[list_cols.index('LUI')]
            # Label
            label = "Term"

            # Properties

            # LAT = row[list_cols.index('LAT')]
            # TS = row[list_cols.index('TS')]

            # print results
            line = LUI + "," + label + "," + LUI
            # print(line)
            fo.write(line + "\n")
            counter = counter + 1
        print('counter = ' + str(counter))

    fo.close()

    # close connection
    db.close()

