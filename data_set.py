#!/usr/bin/env python
import MySQLdb

class Sample:
    "Represenation of one data smaple"

    def __init__(self, db_entry):
        self.good_day = db_entry[len(db_entry)-1]
        self.data_id = db_entry[0]
        self.belongs_to = db_entry[2]
        self.data = db_entry[3:len(db_entry)-1]

def get_field_names(cursor):
    field_names_sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME=\'data\'"
    cursor.execute(field_names_sql)
    field_names_unformated = cursor.fetchall()
    field_names = []
    for i in field_names_unformated:
        field_names.append(i[0])
    field_names = field_names[3:len(field_names)-1]
    return field_names

def get_data_set(cursor):
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    all_data = cursor.fetchall()
    data = []
    for entry in all_data:
        data.append(Sample(entry))
    return data

# Open database connection
db_temp = MySQLdb.connect("localhost","testuser","test123","GoodDay" )
# prepare a cursor object using cursor() method
cursor_temp = db_temp.cursor()

field_names = get_field_names(cursor_temp)
data_set = get_data_set(cursor_temp)
db_temp.close()
