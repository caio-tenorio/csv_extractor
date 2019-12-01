import csv
import os
from models.Remuneracao import Remuneracao
from paths import get_year_folder
from paths import CSV_ROOT_FOLDER_PATH
from utils import create_insert_dict
from database.database_connection import connect_to_db
from database.database_connection import insert_remuneracao


def extract_csv():
    database_connection = connect_to_db()
    for year_folder in os.listdir(CSV_ROOT_FOLDER_PATH):
        year_folder_path = get_year_folder(year_folder, CSV_ROOT_FOLDER_PATH)
        for month_csv in os.listdir(year_folder_path):
            month_file_path = os.path.join(year_folder_path, month_csv)
            with open(month_file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        row_dict = create_insert_dict(row)
                        remuneracao = Remuneracao(row_dict['vereador'], row_dict['total_vantagens'],
                                                  row_dict['descontos_totais'], row_dict['valor_liquido'],
                                                  month_csv.split("-")[0] + "/" + year_folder)
                        insert_remuneracao(remuneracao, database_connection)
                    line_count += 1

    if database_connection:
        database_connection.close()


