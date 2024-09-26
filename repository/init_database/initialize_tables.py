import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI

def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def init_countries_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            insert into Countries (country_name)
            select distinct target_country
            FROM mission
            where target_country is not NULL
            on conflict (country_name) do nothing;
        ''')
    connection.commit()

def init_cities_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            insert into Cities (city_name, country_id, latitude, longitude)
            select distinct
                m.target_city,
                c.country_id,
                m.target_latitude::decimal,
                m.target_longitude::decimal
            from mission m
            join Countries c on m.country = c.country_name
            where m.target_city is not null
            on conflict (city_name) do nothing;
        ''')
    connection.commit()

def init_target_types_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            insert into TargetTypes (target_type_name)
            select distinct target_type
            from mission
            where target_type is not null
            on conflict (target_type_name) do nothing;
        ''')
    connection.commit()

def init_targets_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            insert into Targets (target_industry, target_priority, city_id, target_type_id)
            select distinct
                m.target_industry,
	            m.target_priority::integer,
                ci.city_id,
                tt.target_type_id
            from mission m
            inner join Cities ci on m.target_city = ci.city_name
            inner join TargetTypes tt on m.target_type = tt.target_type_name
            where m.target_id is not NULL and m.target_industry is not null
            on conflict (target_id) do nothing;
    ''')
    connection.commit()

def init_all_tables():
    init_countries_table()
    init_cities_table()
    init_target_types_table()
    init_targets_table()
