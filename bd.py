from mysql.connector import connect, Error


def connection_(password, user):
    try:
        with connect(
                host="localhost",
                password=password,
                user=user,
                database="mydb",
        ) as connection:
            select_query = "SELECT * FROM apartments"
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                result1 = cursor.fetchall()
            select_query = "SELECT * FROM users"
            d = []
            with connection.cursor() as cursor:
                cursor.execute(select_query)
                result2 = cursor.fetchall()
                for i in result2:
                    d.append(i[1:])
            return result1, d

    except Error as e:
        print(e)


def add_user(password, user, first_name, last_name):
    try:
        with connect(
                host="localhost",
                password=password,
                user=user,
                database="mydb",
        ) as connection:
            insert_users_query = """
            INSERT INTO users
            (first_name, last_name)
            VALUES (%s, %s)
            """
            users = [(first_name, last_name)]
            with connection.cursor() as cursor:
                cursor.executemany(insert_users_query, users)
                connection.commit()
    except Error as e:
        print(e)


def add_apartment(password, user, area, number_of_rooms, price, address):
    try:
        with connect(
                host="localhost",
                password=password,
                user=user,
                database="mydb",
        ) as connection:
            if all(x != '' for x in [area, number_of_rooms, price, address]):
                insert_apartments_query = """
                INSERT INTO apartments
                (area, number_of_rooms, price, address)
                VALUES (%s, %s, %s, %s)
                """
                apartments = [(area, number_of_rooms, price, address)]
                with connection.cursor() as cursor:
                    cursor.executemany(insert_apartments_query, apartments)
                    connection.commit()
                return True
            else:
                return False
    except Error as e:
        print(e)


def edit_apartment_bd(password, user, array):
    try:
        with connect(
                host="localhost",
                password=password,
                user=user,
                database="mydb",
        ) as connection:
            sql_update1_query = """Update apartments set area = %s where id = %s"""
            sql_update2_query = """Update apartments set number_of_rooms = %s where id = %s"""
            sql_update3_query = """Update apartments set price = %s where id = %s"""
            sql_update4_query = """Update apartments set address = %s where id = %s"""
            input_ = [(array[1], array[0]), (array[2], array[0]), (array[3], array[0]), (array[4], array[0])]
            sql_update = [sql_update1_query, sql_update2_query, sql_update3_query, sql_update4_query]
            with connection.cursor() as cursor:
                for i in range(len(sql_update)):
                    cursor.execute(sql_update[i], input_[i])
                    connection.commit()
    except Error as e:
        print(e)


def delete_apartment_bd(password, user, id):
    try:
        with connect(
                host="localhost",
                password=password,
                user=user,
                database="mydb",
        ) as connection:
            query2 = "SET FOREIGN_KEY_CHECKS=0"  # ну тут тупанул
            delete_query = "DELETE FROM apartments WHERE id = %s" % id
            with connection.cursor() as cursor:
                cursor.execute(query2)
                cursor.execute(delete_query)
                connection.commit()
    except Error as e:
        print(e)
