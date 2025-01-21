#Load packages
import pandas as pd
import logging
import mlflow
import os

# configure logger
logname = "imported_data.txt"
logging.basicConfig(filename=logname, filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.getLogger('matplotlib.font_manager').disabled = True
logging.info("Data Import Log")


def load_data():
    with mlflow.start_run(run_name = "import_data"):
        mlflow.set_tag("mlflow.runName", "import_data")

        dirpath = os.path.dirname('C:/Users/berly/PycharmProjects/flightdelays/data/BTS_data.csv')
        filepath = os.path.join(dirpath, 'BTS_data.csv')

        #Load data
        df = pd.read_csv(filepath)
        #Rename columns
        df2 = df.rename(columns = {'DAY_OF_MONTH': 'DAY', 'ORIGIN': 'ORG_AIRPORT',
                                   'DEST': 'DEST_AIRPORT', 'CRS_DEP_TIME': 'SCHEDULED_DEPARTURE',
                                   'DEP_TIME': 'DEPARTURE_TIME', 'DEP_DELAY': 'DEPARTURE_DELAY',
                                   'CRS_ARR_TIME': 'SCHEDULED_ARRIVAL', 'ARR_TIME': 'ARRIVAL_TIME',
                                   'ARR_DELAY': 'ARRIVAL_DELAY'})
        #Save to csv file
        csv_location = df2.to_csv('./data/imported_data.csv')
        logging.info("Data import successful")
        print("Data import successful")
        mlflow.log_artifact("./data/imported_data.csv")
        return csv_location
    mlflow.end_run()

load_data()

logging.shutdown()
