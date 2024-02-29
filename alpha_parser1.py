#The excel_sheet_alarm_call function is simplified using a dictionary comprehension.
#The all_alarm_dict is constructed using a dictionary comprehension with a nested loop.
#The for loop in the main function is optimized using assignment expressions (PEP 572) and conditional expressions.
#Unnecessary comments are removed to make the code more concise.
import os
from helper import conftools, data_upload

config_data = conftools.yaml_to_dictionary(os.path.join(os.getcwd(), 'static', 'config.yaml'))
xml = conftools.xml_load(os.path.join(os.getcwd(), 'static', 'mapping_Alpha_Adapter.xlsx'))
logger = conftools.load_logger(os.path.join(os.getcwd(), 'logs'), 'socket-server.log')
alarm_sheet = conftools.xml_load(os.path.join(os.getcwd(), 'static', 'Alpha_Alarm_Adapter.xlsx'))


def excel_sheet_alarm_call(sheet, start_row):
    return {row[0].value: row[2].value for row in sheet.iter_rows(min_row=start_row) if row[2].value}


all_alarm_dict = {col: val for sheet in ['ERR_EMS', 'ERR_BMS', 'DG Alarm'] for col, val in excel_sheet_alarm_call(alarm_sheet[sheet], start_row=3).items()}
alarms_columns = excel_sheet_alarm_call(alarm_sheet['alarm_columns'], start_row=0)


def main():
    column_dict = {}
    scaling_factor = {}

    for row in xml['mapping'].iter_rows(min_row=2):
        if column := row[3].value:
            column_dict[column] = row[0].value
        if scal_column := row[4].value:
            scaling_factor[column] = scal_column

    data_upload.main(logger, config_data, column_dict, scaling_factor, all_alarm_dict, alarms_columns)


if __name__ == '__main__':
    main()





