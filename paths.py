import os


HOME = os.getenv("HOME")
CSV_ROOT_FOLDER_PATH = os.path.join(HOME, 'Documentos', 'TCC', 'remuneracoes')
SPREADSHEET_ROOT_FOLDER_PATH = os.path.join(HOME, 'Documentos', 'TCC', 'verbas_indenizatorias')


def get_year_folder(year, folder_path):
    return os.path.join(folder_path, year)
