import psycopg2


def connect_to_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="testingPassword",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="camaradb")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


conn = connect_to_db()


def insert_remuneracao(remuneracao, conn):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO remuneracoes (vereador, total_vantagens, descontos_totais, valor_liquido, data) VALUES (' + "'" + remuneracao.vereador + "', " + remuneracao.total_vantagens + ', ' +
                   remuneracao.descontos_totais + ', ' + remuneracao.valor_liquido + ", '" + remuneracao.data + "');")
    conn.commit()


def insert_to_db(insert_string):
    cursor = conn.cursor()
    cursor.execute(insert_string)
    conn.commit()


def select_from_db(select_query):
    cursor = conn.cursor()
    cursor.execute(select_query)
    data = cursor.fetchall()
    cursor.close()
    return data


def update_to_db(update_query):
    cursor = conn.cursor()
    cursor.execute(update_query)
    conn.commit()
    cursor.close()
