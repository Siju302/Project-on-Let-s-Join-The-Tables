import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print("database connected successfully.")

import pandas as pd
tables = pd.read_sql('''
select * from sqlite_master where type = "table";
''', conn)
print(tables)

umpire = pd.read_sql('''
select * from umpire;
''', conn)

country = pd.read_sql('''
select * from country;
''', conn)
print(umpire)
print(country)

inner_join = pd.read_sql('''
select country_id, country_name from country
inner join umpire
ON umpire.umpire_country == country.country_id;
''', conn)
print(inner_join)