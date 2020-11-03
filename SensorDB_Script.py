import sqlite3

DB_Name = "Sensors.db"

TableSchema = """

    drop table if exists Sensors;

    create table Sensors(
        SensorID integer not null primary key autoincrement,
        SensorName nvarchar(50) null,
        LocationID integer not null,
        foreign key(LocationID) references Locations(LocationID)
        );

    drop table if exists Locations;

    create table Locations(
        LocationID integer not null primary key autoincrement,
        LocationName nvarchar(50) null
        );
    """

conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#curs.execute("insert into Locations(LocationName) values('Living room')")
#curs.execute("insert into Locations(LocationName) values('Kitchen')")
#curs.execute("insert into Locations(LocationName) values('Room 1')")
#curs.execute("select * from Locations")

#rows = curs.fetchall()

#for row in rows:
#    print(row)
            
curs.close()
conn.close()



