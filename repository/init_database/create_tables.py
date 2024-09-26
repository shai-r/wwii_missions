import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI

def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_countries_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            create table if not exists Countries (
                country_id serial primary key,
                country_name varchar(100) unique not null
            );
        ''')
    connection.commit()

def create_cities_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            create table if not exists Cities (
                city_id serial primary key,
                city_name varchar(100) unique not null,
                country_id int not null,
                latitude decimal,
                longitude decimal,
                foreign key (country_id) references Countries(country_id)
            );
        ''')
    connection.commit()

def create_target_types_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            create table if not exists TargetTypes (
                target_type_id serial primary key,
                target_type_name varchar(255) unique not null
            );
        ''')
    connection.commit()

def create_targets_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            create table if not exists Targets (
                target_id serial primary key,
                target_industry varchar(255) not null,
                city_id int not null,
                target_type_id int,
	            target_priority int,
                foreign key (city_id) references Cities(city_id),
                foreign key (target_type_id) references TargetTypes (target_type_id)
            );
    ''')
    connection.commit()

def create_all_tables():
    create_countries_table()
    create_cities_table()
    create_target_types_table()
    create_targets_table()
