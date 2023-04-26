import pandas as pd
import statistics as stat

def import_fun():
    ais_frame = pd.read_csv(r"data/ais_disabling_events.csv")

    return ais_frame

 

def exploratory_fun(ais_frame):
    print(ais_frame.head())

    print("max timestamp: " + str(max(ais_frame["gap_start_timestamp"])))

    print("min timestamp: "+str(min(ais_frame["gap_start_timestamp"])))

    print("max gap_hours: "+ str(max(ais_frame["gap_hours"])))

    print("min gap_hours: " + str(min(ais_frame["gap_hours"])))

    print("most common vessel flag: " + str(stat.mode(ais_frame["flag"])))



def ais_clean(ais_frame):
    ais_frame



def master_call():
    
    ais_frame= import_fun()

    exploratory_fun(ais_frame)


master_call()