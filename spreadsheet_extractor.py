import os
import xlrd
from paths import get_year_folder
from paths import SPREADSHEET_ROOT_FOLDER_PATH
from database.database_connection import connect_to_db
from constants import get_verbas_indenizatorias_mapping
from models.VerbaIndenizatoria import VerbaIndenizatoria
from database.database_connection import insert_to_db
from database_utils import get_insert_string_verbas


def spreadsheet_extractor():
    verbas_mapping = get_verbas_indenizatorias_mapping()
    for year_folder in os.listdir(SPREADSHEET_ROOT_FOLDER_PATH):
        year_folder_path = get_year_folder(year_folder, SPREADSHEET_ROOT_FOLDER_PATH)
        bigger_month = get_last_month(os.listdir(year_folder_path))
        for month_csv in os.listdir(year_folder_path):
            if month_csv.startswith(str(bigger_month)):
                month_file_path = os.path.join(year_folder_path, month_csv)
                xls = xlrd.open_workbook(month_file_path)
                sheets_list = xls.sheet_names()
                for sheet in sheets_list:
                    if sheet.isdigit():
                        break
                    sheet_read = xls.sheet_by_name(sheet)

                    col_number = 1

                    while col_number < 13:
                        verba_indenizatoria_dict = dict()
                        verba_indenizatoria_dict["vereador"] = sheet
                        row_number = 4
                        while row_number < 23:
                            cell_value = sheet_read.cell(row_number, col_number).value
                            if (cell_value == '' or type(cell_value) != float):
                                cell_value = 0.0
                            verba_indenizatoria_dict[verbas_mapping[row_number]] = cell_value
                            row_number += 1

                        if (len(str(col_number))) == 1:
                            date_month = "0" + (str(col_number))
                        else:
                            date_month = (str(col_number))
                        verba_indenizatoria_dict["data"] = date_month + "/" + year_folder
                        verba_indenizatoria = VerbaIndenizatoria(verba_indenizatoria_dict)
                        query = get_insert_string_verbas(verba_indenizatoria)
                        insert_to_db(query)
                        col_number += 1


def get_last_month(month_list):
    month_numbers_list = list()
    for month_file in month_list:
        month_numbers_list.append(int(month_file.split("-")[0]))
    bigger_number = max(month_numbers_list)
    return bigger_number