from psycopg2.extensions import AsIs
import psycopg2
from parserdzk import datacadnum
#import csv

#whith open('')

conn = psycopg2.connect("dbname='gis12' user='gis12' host='localhost' password='workfree'")
cur = conn.cursor()

song = datacadnum.cnum('6810100000:11:003:0101')
insert_nums = 'insert into kadastr_fromdzk (%s) values %s'

def cadnum(song):
    columns = song.keys()
    values = [song[column] for column in columns]

    cur.execute(insert_nums, (AsIs(','.join(columns)), tuple(values)))


    conn.commit()
    cur.close()
    conn.close()



if __name__ == '__main__':
    cadnum(song)
