import numpy as np
import pandas as pd

def load_and_process(pathname):

    # Method Chain 1 (Load data and deal with missing data)

    ldr1 = (
          pd.read_csv("../data/raw/EMLSdata_10Aug.csv")
          .drop(labels=['Date','LabName','Latitude','Longitude','Altitude_m','SurfaceTemperature_C','EpilimneticTemperature_C','CYN_ugL','ATX_ugL','Lutein_ugL','Echinenone_ugL','Chlorophyllc2_ugL','Peridinin_ugL','Alloxanthin_ugL','Diadinoxanthin_ugL','Zeaxanthin_ugL','Chlorophyllb_ugL','Chlorophylla_ugL','SecchiDepth_m'], axis=1)
          .dropna(axis=0)
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    ldr2 = (
          ldr1
          .rename(columns={"TP_mgl": "Total phosphorus concentration", "TN_mgl": "Total nitrogen concentration", "NO3NO2_mgL": "Nitrates and nitrites concentration", "NH4_mgL": "ammonia concentration", "PO4_mgL": "ortho-phosphate concentration", "MC_YR.ugL": "Concentration of cyanobacterial hepatotoxin microcystin YR", "MC_dmRR.ugL": "Concentration of cyanobacterial hepatotoxin microcystin dmRR", "MC_RR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin RR", "MC_dmLR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin dmLR", "MC_LR_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LR", "MC_LY_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LY", "MC_LW_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LW", "MC_LF_ugL": "Concentration of cyanobacterial hepatotoxin microcystin LF", "NOD_ugL": "Concentration of cyanobacterial hepatotoxin nodularin"})
          .sort_values(by=['MeanDepth_m'], ascending=True)
      )

    return ldr2 
