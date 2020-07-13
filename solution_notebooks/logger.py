import time,os,re,csv,sys,uuid,joblib
from datetime import date
import numpy as np

def update_predict_log(y_pred,y_proba,query,runtime):
    """
    update predict log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    logfile = "example-predict-{}-{}.log".format(today.year, today.month)

    ## write the data to a csv file    
    header = ['unique_id','timestamp','y_pred','y_proba','x_shape','model_version','runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),time.time(),y_pred,y_proba,query.shape,MODEL_VERSION,runtime])
        writer.writerow(to_write)

def update_train_log(unique_id, dates, rmse, runtime,
                     MODEL_VERSION, MODEL_VERSION_NOTE,test=True):
    """
    update train log file
    """
    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    logfile = "example-train-{}-{}.log".format(today.year, today.month)

    ## write the data to a csv file    
    # header = ['unique_id','timestamp','y_pred','y_proba','x_shape','model_version','runtime']
    header = ['unique_id','start date', 'end date', 'rmse', 'runtime', 'model_version', 'model_version_note']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'r+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        if write_header:
            writer.writerow(header)

        to_write = map(unique_id,(str(dates[0]),str(dates[-1])),{'rmse':eval_rmse},runtime, 
                       MODEL_VERSION, MODEL_VERSION_NOTE,test=True)
        writer.writerow(to_write) 