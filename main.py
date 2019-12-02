from csv_extractor import extract_csv
from spreadsheet_extractor import spreadsheet_extractor
import database_utils


def main():
    extract_csv()
    spreadsheet_extractor()
    database_utils.put_key_to_verbas()
    database_utils.put_key_to_materias()
    database_utils.populate_presencas()
    database_utils.put_key_to_remuneracoes()
    database_utils.fix_date_format_of_sessoes()


if __name__ == '__main__':
    main()
