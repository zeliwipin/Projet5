#! /usr/bin/env python3
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode
from constantes import *


class Create_tables :

    # Initialiser

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",
                                            user="newuser", password="monmdp", database = "OpenFood")

        self.mycursor = self.mydb.cursor()


    def create_tables(self):
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}".format(table_name), end='')
                self.mycursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        self.mycursor.close()
















#mycursor.execute("CREATE TABLE category(category_id int unsigned AUTO_INCREMENT, "
              #   "category_name varchar(40), PRIMARY KEY (category_id)) ENGINE = InnoDB")


