#Load packages
import pandas as pd
import logging
import mlflow

def clean_data():
    # configure logger
    logname = "cleaned_data.txt"
    logging.basicConfig(filename=logname,
                        filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.getLogger('matplotlib.font_manager').disabled = True
    logging.info("Data Cleaning Log")


    with mlflow.start_run(run_name = "clean_data") as run:
        mlflow.set_tag("mlflow.runName", "clean_data")
        #Load and preview data
        df1 = pd.read_csv('./data/imported_data.csv')

        #Check for duplicate rows
        print(df1.duplicated())
        print(df1.duplicated().sum())

        #Filter for departures from ORD
        df = df1[df1['ORG_AIRPORT'] == 'ORD']

        #Check for and remove missing values
        df.isnull().any()
        df.isnull().sum()
        df2 = df.dropna()

        #Check and correct data format
        df2 = df2.astype({'ARRIVAL_DELAY': 'int64'})
        df2 = df2.astype({'ARRIVAL_TIME': 'int64'})
        df2 = df2.astype({'DEPARTURE_TIME': 'int64'})
        df2 = df2.astype({'DEPARTURE_DELAY': 'int64'})
        df2 = df2.astype({'ORG_AIRPORT': 'string'})
        df2 = df2.astype({'DEST_AIRPORT': 'string'})

        #Check destination airport format
        df2['DEST_AIRPORT'].unique()
        #All are 3 digit codes in correct format

        #Save data set to csv
        clean_csv_location = df2.to_csv('cleaned_data.csv')

        logging.info('Data cleaning successful')
        mlflow.log_artifact('./data/cleaned_data.csv')
        return clean_csv_location

clean_data()
print('Data cleaning successful')

logging.shutdown()