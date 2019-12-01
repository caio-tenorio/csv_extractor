from database.database_connection import select_from_db
from database.database_connection import update_to_db
from utils import remover_acentos
from database.database_connection import insert_to_db

SELECT_VEREADORES = 'select id, nome_parlamentar from vereadores;'
SELECT_VERBAS = 'select id, vereador from verbas_indenizatorias;'
SELECT_MATERIAS = 'select id, autor from materias;'
SELECT_SESSOES = 'select id, lista_de_presenca from sessoes;'
SELECT_REMUNERACOES = 'select id, vereador from remuneracoes;'
SELECT_VERBAS_DATA = 'select id, data from verbas_indenizatorias;'
SELECT_MATERIAS_DATE = 'select id, data_materia from materias;'
SELECT_REMUNERACOES_DATE = 'select id, data from remuneracoes;'
SELECT_SESSOES_DATE = 'select id, data_sessao from sessoes;'


def fix_date_format_of_verbas():
    verbas = select_from_db(SELECT_VERBAS_DATA)
    for verba in verbas:
        id = verba[0]
        data = verba[1]
        data_list = data.split('/')
        ano = data_list[1]
        mes = data_list[0]
        data_fixed = ano + "/" + mes
        query = get_update_date_query('verbas_indenizatorias', data_fixed, id)
        update_to_db(query)


def fix_date_format_of_remuneracoes():
    remuneracoes = select_from_db(SELECT_REMUNERACOES_DATE)
    for remuneracao in remuneracoes:
        id = remuneracao[0]
        data = remuneracao[1]
        data_list = data.split('/')
        ano = data_list[1]
        mes = data_list[0]
        data_fixed = ano + "/" + mes
        query = get_update_date_query('remuneracoes', 'data', data_fixed, id)
        update_to_db(query)


def get_update_date_query(table, field, data, id):
    query = """UPDATE {}
    SET {} = '{}'
    WHERE id = {};""".format(table, field, data, id)
    return query


def fix_date_format_of_materias():
    fix_date_format('materias', 'data_materia', SELECT_MATERIAS_DATE)


def fix_date_format_of_sessoes():
    fix_date_format('sessoes', 'data_sessao', SELECT_SESSOES_DATE)


def fix_date_format(table, field, select_query):
    rows = select_from_db(select_query)
    for row in rows:
        id = row[0]
        data = row[1]
        if not (data.startswith('2019') or data.startswith('2018') or data.startswith('2017')):
            data_list = data.split('/')
            ano = data_list[2]
            mes = data_list[1]
            dia = data_list[0]
            data_fixed = ano + "/" + mes + "/" + dia
            query = get_update_date_query(table, field, data_fixed, id)
            update_to_db(query)


def populate_presencas():
    vereadores = select_from_db(SELECT_VEREADORES)
    sessoes = select_from_db(SELECT_SESSOES)

    for vereador in vereadores:
        nome_parlamentar = remover_acentos(vereador[1].upper())
        for sessao in sessoes:
            lista_de_presenca = sessao[1]
            for vereador_presente in lista_de_presenca:
                if nome_parlamentar in remover_acentos(vereador_presente).upper():
                    presente = "true"
                    id_vereador = vereador[0]
                    id_sessao = sessao[0]
                    insert_string = get_insert_string_presencas(presente, id_vereador, id_sessao)
                    insert_to_db(insert_string)


def put_key_to_materias():
    vereadores = select_from_db(SELECT_VEREADORES)
    materias = select_from_db(SELECT_MATERIAS)

    for vereador in vereadores:
        nome_parlamentar = remover_acentos(vereador[1].upper())
        if nome_parlamentar == 'Jairo Britto':
            nome_parlamentar = 'Jairo Brito'
        elif nome_parlamentar == 'Amaro Cipriano':
            nome_parlamentar = 'Amaro Cipriano Maguari'
        elif nome_parlamentar == 'Hélio Guabiraba':
            nome_parlamentar = 'Hélio da Guabiraba'
        for materia in materias:
            autor_materia = remover_acentos(materia[1].upper())
            if autor_materia in nome_parlamentar:
                query = get_update_query_materias(vereador[0], materia[0])
                update_to_db(query)


def get_update_query_materias(id_vereador, id_materia):
    query = """UPDATE materias
        SET id_vereador = {}
        WHERE id = {}""".format(id_vereador, id_materia)
    return query


def put_key_to_verbas():
    vereadores = select_from_db(SELECT_VEREADORES)
    verbas_indenizatorias = select_from_db(SELECT_VERBAS)

    for vereador in vereadores:
        nome_parlamentar = remover_acentos(vereador[1].upper())
        for verba in verbas_indenizatorias:
            nome_vereador = remover_acentos(verba[1])
            nome_parlamentar_first_name = nome_parlamentar.split(" ")[0]
            if nome_parlamentar_first_name == "BENJAMIM":
                nome_parlamentar_first_name = "BENJAMIN"
            elif nome_parlamentar_first_name == "MISSIONARIA":
                nome_parlamentar_first_name = "DAIZE"
            elif nome_parlamentar_first_name == "ERIBERTO":
                nome_parlamentar_first_name = "RAFAEL"
            elif nome_parlamentar_first_name == "PROFESSORA":
                nome_parlamentar_first_name = "ANA"
            elif nome_parlamentar_first_name == "EDUARDO":
                nome_parlamentar_first_name = nome_parlamentar

            if (nome_parlamentar_first_name in nome_vereador) or (nome_parlamentar_first_name == nome_vereador):
                query = get_update_query_verbas(vereador[0], verba[0])
                update_to_db(query)


def put_key_to_remuneracoes():
    vereadores = select_from_db(SELECT_VEREADORES)
    remuneracoes = select_from_db(SELECT_REMUNERACOES)

    for vereador in vereadores:
        nome_parlamentar = remover_acentos(vereador[1].upper())
        for remuneracao in remuneracoes:
            nome_vereador = remover_acentos(remuneracao[1])
            nome_parlamentar_first_name = nome_parlamentar.split(" ")[0]
            if nome_parlamentar_first_name == "BENJAMIM":
                nome_parlamentar_first_name = "BENJAMIN"
            elif nome_parlamentar_first_name == "MISSIONARIA":
                nome_parlamentar_first_name = "DAIZE"
            elif nome_parlamentar_first_name == "ERIBERTO":
                nome_parlamentar_first_name = "RAFAEL"
            elif nome_parlamentar_first_name == "PROFESSORA":
                nome_parlamentar_first_name = "ANA"
            elif nome_parlamentar_first_name == "JUNIOR":
                nome_parlamentar_first_name = "INALDO"
            elif nome_parlamentar_first_name == "CHICO":
                nome_parlamentar_first_name = "FRANCISCO"
            elif nome_parlamentar_first_name == "EDUARDO":
                nome_parlamentar_first_name = nome_parlamentar
                if nome_parlamentar_first_name == "EDUARDO CHERA":
                    nome_parlamentar_first_name = "EDUARDO PEREIRA"
                else:
                    nome_parlamentar_first_name = "EDUARDO AMORIM"

            if (nome_parlamentar_first_name in nome_vereador) or (nome_parlamentar_first_name == nome_vereador):
                query = get_update_query_remuneracoes(vereador[0], remuneracao[0])
                update_to_db(query)


def get_update_query_verbas(id_vereador, id_verba):
    query = """UPDATE verbas_indenizatorias
    SET id_vereador = {}
    WHERE id = {}""".format(id_vereador, id_verba)
    return query


def get_update_query_remuneracoes(id_vereador, id_remuneracoes):
    query = """UPDATE remuneracoes
        SET id_vereador = {}
        WHERE id = {}""".format(id_vereador, id_remuneracoes)
    return query


def get_insert_string_presencas(presente, id_vereador, id_sessao):
    query = """INSERT INTO presencas (presente, id_vereador, id_sessao) 
    VALUES ({}, {}, {});""".format(presente, id_vereador, id_sessao)
    return query


def get_insert_string_verbas(verba_indenizatoria):
    insert_string = "INSERT INTO verbas_indenizatorias ("
    values_list = list()
    for key in verba_indenizatoria.__dict__.keys():
        insert_string = insert_string + str(key) + ", "
        values_list.append(verba_indenizatoria.__dict__[key])
    insert_string = insert_string[:-2] + ") VALUES ("

    for value in values_list:
        if type(value) == str:
            value = "'" + value + "'"
        else:
            value = str(value)
        insert_string = insert_string + value + ", "
    insert_string = insert_string[:-2] + ");"

    return insert_string