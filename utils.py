from unicodedata import normalize


def create_insert_dict(row):
    insert_dict = dict()
    insert_dict['vereador'] = row[2].replace("'", "")
    insert_dict['total_vantagens'] = row[5].replace(".", "").replace(",", ".")
    insert_dict['descontos_totais'] = row[6].replace(".", "").replace(",", ".")
    insert_dict['valor_liquido'] = row[7].replace(".", "").replace(",", ".")

    return insert_dict


from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')