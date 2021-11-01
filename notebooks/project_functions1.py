# Import libraries 
import numpy as np 
import pandas as pd 

def load_and_process(pathname):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(pathname)
          .drop(["Lake_ID","LabName","Altitude_m", "SamplingDepth_m", "ThermoclineDepth_m", "SecchiDepth_m"], axis = 1)
          .dropna(axis=0)
          .drop(columns=df_method_chaining.columns[df_method_chaining.eq(0).mean()>0.55])
          .rename(columns = {
               "MaximumDepth_m": "Maximum Lake Depth (m)",
               "MeanDepth_m": "Mean Depth Lake (m)",
               "EpilimneticTemperature_C":"Epilimnetic Temperature (C)",
               "TP_mgL":"Phosphate Concentration (mg/L)",
               "SurfaceTemperature_C": "Lake Surface Temperature (C)",
               "TN_mgL": "Nitrogen Concentration (mg/L)",
                "NO3NO2_mgL": "Concentration of Nitrates and Nitrites (mg/L)",
                "NH3_mgL": "Concentration of Ammonia (mg/L)",
                "PO4_ugL": "Concentration of Ortho-phosphate (ug/L)",
                "Chlorophylla_ugL": "Concentration of Chlorophyll-a (ug/L)",
                "Chlorophyllb_ugL" : "Concentration of Chlorophyll-b (ug/L)",
                "Zeaxanthin_ugL" : "Concentration of Zeaxanthin (ug/L)",
                "Alloxanthin_ugL" : "Concentration of Alloxanthin (ug/L)",
                "Chlorophyllc2_ugL" : "Concentration of Chlorophyll-c2 (ug/L)",
                "MC_YR_ugL" : "Concentration of Microcystin YR (ug/L)",
                "MC_dmLR_ugL" : "Concentration of Microcystin dmLR (ug/L)",
                "MC_LR_ugL" : "Concentration of Microcystin LR (ug/L)",
                "LakeName" : "Lake Name",
                         
              })
          
          
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(Total_Concentration_Photosynthetic_Pigments_ugL = lambda x: 0.2*df_method_chaining["Chlorophylla_ugL"] + 0.2* df_method_chaining["Chlorophyllb_ugL"] + 0.2* df_method_chaining["Zeaxanthin_ugL"] + 0.2* df_method_chaining["Alloxanthin_ugL"] + 0.2*df_method_chaining["Chlorophyllc2_ugL"])
          .rename(columns = {
               "Total_Concentration_Photosynthetic_Pigments_ugL": "Total Concentration Photosynthetic Pigments (ug/L)"
        
             })
    
          .sort_values("Total Concentration Photosynthetic Pigments (ug/L)")
          .reset_index()
          .dropna(axis=0)
          .drop('index',axis =1)
          .reindex(columns = ["Date", "Country", "Lake Name","Total Concentration Photosynthetic Pigments (ug/L)", "Latitude", "Longitude", "Maximum Lake Depth (m)", "Mean Depth Lake (m)", "Lake Surface Temperature (C)", "Epilimnetic Temperature (C)", "Phosphate Concentration (mg/L)", "Nitrogen Concentration (mg/L)", "Concentration of Nitrates and Nitrites (mg/L)", "Concentration of Ammonia (mg/L)", "Concentration of Ortho-phosphate (ug/L)", "Concentration of Chlorophyll-a (ug/L)", "Concentration of Chlorophyll-b (ug/L)", "Concentration of Zeaxanthin (ug/L)", "Concentration of Alloxanthin (ug/L)", "Concentration of Chlorophyll-c2 (ug/L)", "Concentration of Microcystin YR (ug/L)", "Concentration of Microcystin dmLR (ug/L)", "Concentration of Microcystin LR (ug/L)"])
    
      )

    # Make sure to return the latest dataframe

    return df2 