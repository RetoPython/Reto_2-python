from package.module_exec_SP import exec_SP_mssql
from package.module_logging import module_logging
import os
osfile = os.path.basename(__file__)

#para crear log
module_logging(message_logging='Ejecutando SP', osfile=osfile )

#Ejecutando SP
exec_SP_mssql(msg_boolean=1,
            id_database=0,
            id_procedure=0
            )
