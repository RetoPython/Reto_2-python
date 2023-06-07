from package.module_insert import insert_bd_mssql
from package.module_read_files import read_file_csv
from package.module_list_files import list_files
from package.module_move_files import move_files
"""
from package.module_send_report import send_report

send_report(msg_boolean=1,
            id_dates=0,
            id_path_files=1,
            id_mails=1
            )
"""
list_files = list_files(id_path_files=0)

for file in list_files:

    data = read_file_csv(msg_boolean=1, id_path_files=0, name_file=file)



    msg_insert = insert_bd_mssql(msg_boolean=1,
                                data=data,
                                id_database=0,
                                id_table=0
                                )

    move_files( msg_boolean=msg_insert,
                id_path_files=0,
                name_file=file
                )
