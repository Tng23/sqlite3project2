import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name1 = 'my_table_11'
table_name2 = 'my_table_22'
new_field = 'my_1st_column'
field_type = 'INTEGER'

#connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
    .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn}({nf}{ft} PRIMARY KEY)'\
    .format(tn=table_name2, nf=new_field, ft=field_type))

print("Table completed")
conn.commit()
conn.close()