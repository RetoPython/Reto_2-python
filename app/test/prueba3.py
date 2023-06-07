from package.module_read_sql import read_bd_mssql
from package.module_df_to_file import df_to_xlsx
from package.module_logging import module_logging
import os
osfile = os.path.basename(__file__)

#para crear log
module_logging(message_logging='Ejecutando SP', osfile=osfile )

#select data de BD
df_select_sql = read_bd_mssql(msg_boolean=1,
                id_database=0,
                id_procedure=1
                )

#genera el excel
df_to_xlsx( msg_boolean=1,
            id_path_files=1,
            df=df_select_sql,
            id_dates=0
            )
