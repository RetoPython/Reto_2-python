
from package.module_config import Configuration
from package.module_list_files import list_files
from package.module_read_files import read_file_xlsx
from package.module_move_files import move_files
from package.module_insert import insert_bd_mssql
from package.module_delete import delete_bd_mssql
from querys.query_reporte_prueba import delete_report_prueba
from package.module_logging import module_logging
import os
osfile = os.path.basename(__file__)

#para crear log
module_logging(message_logging='Iniciando log del reporte', osfile=osfile )

#para obtener fecha
dates = Configuration(id_dates=0, keyword="date_process").get_date_iso8601(utc=False)
StartDate = dates[0]
EndDate   = dates[1]
print(dates)

#Fomateando fechas en el query delete
module_logging(message_logging='Formateando fechas en query' + str(dates), osfile=osfile )
query_delete_format = delete_report_prueba.format(StartDate=StartDate, EndDate=EndDate)

#Lista archivos de una ruta
list_files = list_files(id_path_files=0)

for file in list_files:

    #Lee el archivo
    module_logging(message_logging='Leyendo datos del excel', osfile=osfile )
    data = read_file_xlsx(msg_boolean=1,
                        id_path_files=0,
                        name_file=file
                        )


    #elimina el archivo en la bd
    module_logging(message_logging='Eliminando datos residuales', osfile=osfile )
    msg_delete = delete_bd_mssql(msg_boolean=1,
                                id_database=0,
                                query_delete=query_delete_format
                                )


    #Inserta datos a la db
    module_logging(message_logging='Insertando datos a la BD', osfile=osfile )
    msg_insert = insert_bd_mssql(msg_boolean=msg_delete,
                                data=data,
                                id_database=0,
                                id_table=0
                                )


    #Mover archivo a procesados
    module_logging(message_logging='Moviendo excel a procesados', osfile=osfile )
    move_files( msg_boolean=msg_insert,
                id_path_files=0,
                name_file=file
                )


