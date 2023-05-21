from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData, Date
from datetime import datetime
import csv
import sqlite3

engine = create_engine('sqlite:///my_database.db')

metadata = MetaData()

stations = Table('stations', metadata,
                 Column('station', String, primary_key=True),
                 Column('latitude', String),
                 Column('longitude', String),
                 Column('elevation', String),
                 Column('name', String),
                 Column('country', String),
                 Column("state", String))

measures = Table('measures', metadata,
                 Column('station', String, primary_key=True),
                 Column('date', Date, primary_key=True),
                 Column('precip', Float),
                 Column('tobs', Integer))

metadata.create_all(engine)

with open('clean_stations.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    with engine.connect() as conn:
        for row in csv_reader:
            conn.execute(stations.insert().prefix_with('OR IGNORE').values(
                station=row[0],
                latitude=row[1],
                longitude=row[2],
                elevation=row[3],
                name=row[4],
                country=row[5],
                state=row[6]
            ))

with open('clean_measure.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    with engine.connect() as conn:
        for row in csv_reader:
            if row[1] == 'date':
                continue
            conn.execute(measures.insert().prefix_with('OR IGNORE').values(
                station=row[0],
                date=datetime.strptime(row[1], "%Y-%m-%d").date(),
                precip=float(row[2]),
                tobs=int(row[3])
            ))

with engine.connect() as conn:
    result = conn.execute("SELECT * FROM stations JOIN measures ON stations.station = measures.station LIMIT 5").fetchall()
    for row in result:
        print(row)