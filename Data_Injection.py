# THIS IS A SCRIPT ___________________________________________

# There are a lot of .csv files with us regarding the Problem Statement.
# Normally in companies the data is present in the databases,
#         but here we need to first store our .csv data in a database.

import pandas as pd
import os
from sqlalchemy import create_engine

import logging
import time

# When we write import logging, it gives us access to:
# 1.) logging.info(), 2.) logging.error(), 3.) logging.debug()
# But before using them, Python needs to know:
# Where to write messages?... Which messages to write?... How should messages look?...
# That setup is done by logging.basicConfig() :-> 

logging.basicConfig( # <- This means whenever my program writes a log message, follow these rules :-
    filename = 'Logs/injection_db.log',
    # Rule 1 -> Where to write the logs, 
    # Inside LOGS folder create ingestion_db.log and write all the logs in it
    level = logging.DEBUG,
    # Rule 2 -> You tell the guard: Let everything inside, even very small details/log.
    # debug messages → allowed, info messages → allowed, warning messages → allowed, error messages → allowed.
    format = "%(asctime)s - %(levelname)s - %(message)s",
    # Rule 3 -> How the log should look like (time+date | INFO/ERROR/DEBUG | Message)
    filemode = 'a'
    # Rule 4 -> It controls what happens when the log file already exists.
    # 'a' -> append, 'w' -> Old log file deleted New file created.
)

path = r'C:\Users\DELL\VENDER PERFORMANCE ANALYSIS\DATASET' 
# <- This is the path where the data is stored in my storage.

engine = create_engine('sqlite:///inventory.db') # <- CREATING DATABASE
# Engine is the connection to a database and acts as the communication layer.

# Now we will do Injections (Puting the files into the database)
# Normally when we work at companies, we need to do scripting :
# Lets suppose our data is continuously comming from a server in .csv format
#    then we need to put this data in the database for which 
#    we need to perform scripting and then schedule that script. Suppose, 
#        -> If the .csv file is comming in every 15 min, then we need to schedule 
#              the scipt for 15 min so that python runs the script and store the .csv 
#              dataset into database every 15 min.

# We should always make a function for scripting put every thing under it.
# We also add LOGGING in Scripting :
#    Logging is a process to record the errors and warnings.
#    It is mainly used to check what all steps are executed & which are not.
#    For logging we need to first create a folder. 

def injest_db(df, table_name, engine) :
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
#   .to_sql will convert a DataFrame file into SQL table
#      -> df is the DataFrame that we will convert.
#      -> con = engine is the connection to SQL database where we will store the table.
#      -> if_exist = 'replace' will delete the existing table, create a new table &
#                              insert the DataFrame data into it.
#                  = 'append' will add rows to existing table.
#      -> index = False will prevents the DataFrame index from being saved as a column.

# Now we need to call the ingest_db() function in the below function loop.

def Load_Raw_Data() :
    start = time.time()
    for files in os.listdir(path) :
        if '.csv' in files :
            df = pd.read_csv(path+'/'+files)
            logging.info(f'Injesting {files} in DB.')
            injest_db(df, files[ : -4], engine)
    end = time.time()
    logging.info(f'--------------INJECTION COMPLETE--------------')
    logging.info(f'Time Taken in Injection = {(end - start) / 60:.2f} minutes')

if __name__ == '__main__' :
    Load_Raw_Data()





