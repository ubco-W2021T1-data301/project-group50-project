import numpy as np
import pandas as pd

def load_and_process(pathname):

    # Method Chain 1 (Load data, remove unneeded columns and remove rows with missing data)

    ldr1 = (
        pd.read_csv("../data/raw/EMLSdata_10Aug.csv")
        .drop(labels=['MeanDepth_m','Lake_ID','MC_LY_ugL','MC_LW_ugL','MC_LF_ugL','NOD_ugL','MaximumDepth_m', 'TN_mgL', 'NO3NO2_mgL', 'NH3_mgL', 'PO4_ugL','Date','LabName','Latitude','ThermoclineDepth_m','SamplingDepth_m','Longitude','Altitude_m','SurfaceTemperature_C','EpilimneticTemperature_C','CYN_ugL','ATX_ugL','Lutein_ugL','Echinenone_ugL','Chlorophyllc2_ugL','Peridinin_ugL','Alloxanthin_ugL','Diadinoxanthin_ugL','Fucoxanthin_ugL','Zeaxanthin_ugL','Chlorophyllb_ugL','Diatoxanthin_ugL','Chlorophylla_ugL','SecchiDepth_m','Violaxanthin_ugL'], axis=1)
        .dropna(axis=0)
    )
    
    # Method Chain 2 (Drop unneeded columns, rename columns, drop outlier row, sort with ascending Mean Depth (m)
    
    ldr2 = (
        ldr1
        .rename(columns=
            {"LakeName": "Lake Name", 
            "TP_mgL": "Concentration of total phosphorus (mgL)",
            "MC_YR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin YR (ugL)", 
            "MC_dmRR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin dmRR (ugL)", 
            "MC_RR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin RR (ugL)", 
            "MC_dmLR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin dmLR (ugL)", 
            "MC_LR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LR (ugL)", 
            "MC_LW_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LW (ugL)", 
            "MC_LF_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LF (ugL)", 
            "NOD_ugL": "Concentration of cyanobacterial hepatotoxin nodularin (ugL)"})
        .sort_values(by=['Concentration of total phosphorus (mgL)'], ascending=True)
    )
    
    return ldr2

load_and_process('../data/raw/EMLSdata_10Aug.csv')
