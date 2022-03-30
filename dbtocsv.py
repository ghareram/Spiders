import pymysql
import csv
import sys

db_opts = {
    'user': 'hare',
    'password': 'Ram@1234',
    'host': 'localhost',
    'database': 'dbussecurity'
}

db = pymysql.connect(**db_opts)
cur = db.cursor()

sql = 'SELECT * from ussecurity'
csv_file_path = '/home/hareram/ussecurity/ussecurity/spiders/dbtocsv.csv'

try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    db.close()

if rows:
    result = list()

    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))
