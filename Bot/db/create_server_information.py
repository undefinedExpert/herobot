#!/usr/bin/python

import psycopg2
from Bot.db.config import config


# FOREIGN KEY - Najprostsza definicja klucza obcego,
#               jaką można przytoczyć, specyfikuje dodatkową kolumnę
#               lub zbiór kolumn w danej tabeli z wartościami,
#               stanowiącymi klucz główny w innej.
# PRIMARY KEY - ID danego rekordu
# REFERENCES - sluzy do ustalenia relacji miedzy pomiedzy tabelami


def create_tables():
    # czym jest tabela?
    """ create tables in the PostgreSQL database"""
    commands = (
        """
            CREATE TABLE servers (
                server_id SERIAL PRIMARY KEY,
                server_address VARCHAR(255) NOT NULL
            )
        """,
        """
            CREATE TABLE apps (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                version VARCHAR(255) NOT NULL,
                size VARCHAR(255) NOT NULL,
                game_id VARCHAR(255) NOT NULL,
                installed BOOLEAN NOT NULL,
                my_own BOOLEAN NOT NULL,
                server_id INTEGER NOT NULL,
                FOREIGN KEY (server_id)
                REFERENCES servers(server_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            )
        """,
        """
            CREATE TABLE hardwares (
                hardware_id SERIAL PRIMARY KEY,
                space_all VARCHAR(255) NOT NULL,
                space_taken VARCHAR(255) NOT NULL,
                space_free VARCHAR(255) NOT NULL,
                network VARCHAR(255) NOT NULL,
                server_id INTEGER NOT NULL,
                FOREIGN KEY (server_id)
                REFERENCES servers(server_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            )
        """
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_server(server_address):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO servers(server_address)
             VALUES(%s) RETURNING server_id;"""

    check_existence = """
        SELECT exists(SELECT server_address FROM servers
        WHERE server_address = '%s')
      """ % server_address

    conn = None
    server_id = None

    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()

        # check if server already exists
        cur.execute(check_existence)

        if cur.fetchone()[0]:
            print('Server on %s already exist' % server_address)
            return False

        # execute the INSERT statement
        cur.execute(sql, (server_address,))
        # get the generated id back
        server_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return server_id


def insert_server_list(servers):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO servers(server_address) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, servers)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_server(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE servers
                SET server_address = %s
                WHERE server_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def add_app(app, server_address):
    # we should get id of server address we are looking for
    server_id = None
    # statement for inserting a new row into the parts table
    insert_app = """
        INSERT INTO apps(name,
                         type,
                         version,
                         size,
                         installed,
                         my_own,
                         game_id,
                         server_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
      """

    get_server_id = """
      SELECT server_id, server_address
      FROM servers
      WHERE server_address LIKE '%s';
    """ % server_address

    check_existence = """
        SELECT exists(
            SELECT name FROM apps
            WHERE
              game_id = '%s'
              AND
              apps.server_id = '%s'
          )
      """


    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # get id of server address
        cur.execute(get_server_id)
        server_id = cur.fetchone()[0]

        # check if software already exists
        cur.execute(check_existence % (app['game_id'], server_id))
        print('Adding %s on server %s into database' % (app['name'], server_address))

        # check if exist
        if cur.fetchone()[0]:
            print('App %s already exist on %s server address' % (app['name'], server_address))
            return False


        # insert our software into apps
        cur.execute(insert_app, (app['name'],
                                 app['type'],
                                 app['version'],
                                 app['size'],
                                 app['installed'],
                                 app['my_own'],
                                 app['game_id'],
                                 server_id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_apps(server_address):
    # we should get id of server address we are looking for
    server_id = None
    # statement for inserting a new row into the parts table
    get_apps = """
        SELECT * FROM apps
        WHERE apps.server_id = %s;
      """

    get_server_id = """
      SELECT server_id, server_address
      FROM servers
      WHERE server_address LIKE '%s';
    """ % server_address


    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # get id of server address
        cur.execute(get_server_id)
        server_id = cur.fetchone()[0]

        # check if software already exists
        cur.execute(get_apps % server_id)
        apps = cur.fetchone()

        return apps
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# def add_hardware(app_name, server_address):
#     # we should get id of server address we are looking for
#     server_id = None
#     # statement for inserting a new row into the parts table
#     insert_app = """
#         INSERT INTO apps(app_name, server_id) VALUES(%s, %s);
#       """
#
#     get_server_id = """
#       SELECT server_id, server_address
#       FROM servers
#       WHERE server_address LIKE '%s';
#     """ % server_address
#
#     check_existence = """
#         SELECT exists(
#             SELECT app_name FROM apps
#             WHERE
#               app_name = '%s'
#               AND
#               apps.server_id = '%s'
#           )
#       """
#
#
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#
#
#         # get server id of address
#         cur.execute(get_server_id)
#         server_id = cur.fetchone()[0]
#
#         # check if software already exists
#         cur.execute(check_existence % (app_name, server_id))
#         print('Adding %s on server %s into database' % (app_name, server_address))
#
#         # chujowo sprawdza
#         if cur.fetchone()[0]:
#             print('App %s already exist on %s server address' % (app_name, server_address))
#             return False
#
#         # chujowo wrzuca
#         # insert our software into apps
#         cur.execute(insert_app, (app_name, server_id))
#
#         # commit changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


def add_hardware(space, network, server_address):
    # we should get id of server address we are looking for
    server_id = None
    # statement for inserting a new row into the parts table

    """
                    hardware_id SERIAL PRIMARY KEY,
                space_all VARCHAR(255) NOT NULL,
                space_taken VARCHAR(255) NOT NULL,
                space_free VARCHAR(255) NOT NULL,
                network VARCHAR(255) NOT NULL,
                server_id INTEGER NOT NULL,
    """
    insert_app = """
        INSERT INTO hardwares(space_all,
                              space_taken,
                              space_free,
                              network,
                              server_id) VALUES(%s, %s, %s, %s, %s);
      """

    get_server_id = """
      SELECT server_id, server_address
      FROM servers
      WHERE server_address LIKE '%s';
    """ % server_address

    check_existence = """
        SELECT exists(
            SELECT hardware_id FROM hardwares
            WHERE
              space_free = '%s'
              AND
              hardwares.server_id = '%s'
          )
      """


    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # get id of server address
        cur.execute(get_server_id)
        server_id = cur.fetchone()[0]

        # check if software already exists
        cur.execute(check_existence % (space['free'], server_id))
        print('Pushing  hardware information of %s server into database' % (server_address))

        # check if exist
        if cur.fetchone()[0]:
            print('Space didnt change' % (space['free'], server_address))
            return False


        # insert our software into apps
        cur.execute(insert_app, (space['all'],
                                 space['taken'],
                                 space['free'],
                                 network,
                                 server_id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_hardware(server_address):
    # we should get id of server address we are looking for
    server_id = None
    # statement for inserting a new row into the parts table
    get_apps = """
        SELECT * FROM apps
        WHERE apps.server_id = %s;
      """

    get_server_id = """
      SELECT server_id, server_address
      FROM servers
      WHERE server_address LIKE '%s';
    """ % server_address


    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # get id of server address
        cur.execute(get_server_id)
        server_id = cur.fetchone()[0]

        # check if software already exists
        cur.execute(get_apps % server_id)
        apps = cur.fetchone()

        return apps
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# def add_hardware(app_name, server_address):
#     # we should get id of server address we are looking for
#     server_id = None
#     # statement for inserting a new row into the parts table
#     insert_app = """
#         INSERT INTO apps(app_name, server_id) VALUES(%s, %s);
#       """
#
#     get_server_id = """
#       SELECT server_id, server_address
#       FROM servers
#       WHERE server_address LIKE '%s';
#     """ % server_address
#
#     check_existence = """
#         SELECT exists(
#             SELECT app_name FROM apps
#             WHERE
#               app_name = '%s'
#               AND
#               apps.server_id = '%s'
#           )
#       """
#
#
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#
#
#         # get server id of address
#         cur.execute(get_server_id)
#         server_id = cur.fetchone()[0]
#
#         # check if software already exists
#         cur.execute(check_existence % (app_name, server_id))
#         print('Adding %s on server %s into database' % (app_name, server_address))
#
#         # chujowo sprawdza
#         if cur.fetchone()[0]:
#             print('App %s already exist on %s server address' % (app_name, server_address))
#             return False
#
#         # chujowo wrzuca
#         # insert our software into apps
#         cur.execute(insert_app, (app_name, server_id))
#
#         # commit changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()

def get_server_information(server_address):
    pass