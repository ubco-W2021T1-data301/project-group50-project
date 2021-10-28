import pandas as pd

def load_and_process(pathname):

  # Method Chain 1 (Load data and deal with missing data)

  df1 = (
      pd.read_csv(pathname)
      .rename(columns={'Lake_ID' : "LakeID", 'Altitude_m' : 'Altitude', 'MaximumDepth_m' : 'MaximumDepth', 'MeanDepth_m' : 'MeanDepth', 
                        'SurfaceTemperature_C' : 'SurfaceTemperature', 'Chlorophylla_ugL' : 'Chlorophylla', 'Chlorophyllb_ugL' : 'Chlorophyllb',
                        'Chlorophyllc2_ugL' : 'Chlorophyllc'})
      [['LakeID', 'Date', 'LakeName', 'LabName', 'Country', 'Latitude', 'Longitude', 'Altitude', 'MaximumDepth', 'MeanDepth', 'Chlorophylla', 'Chlorophyllb', 'Chlorophyllc']]
      .dropna(how="any")
      .sort_values("Altitude")
      .reset_index(drop=True)
  )

  # Method Chain 2 (Create new columns, drop others, and do processing)

  df2 = (
      df1
      .assign(Year = lambda x : df1['Date'].str[:4])
      .assign(Month = lambda x : df1['Date'].str[5:7])
  )

  return df2