import pandas as pd
import json
import os


def decompose_weather_data():
    """
     Decompose a combined weather dataset into individual JSON files.

    This function reads a JSON file (`downloads/weather.json`) containing a list of
    weather data entries, each with latitude and longitude values. It then creates
    a new directory (`decomposed_weather_data/`) and writes each entry into its own
    separate JSON file.
    """
    try:
        with open('downloads/weather_combined.json', mode='r') as file:
            res = json.load(file)
    except FileNotFoundError as e:
         return

    for d in res:
        with open(f'downloads/weather_lat_{d["latitude"]}_long_{d["longitude"]}.json', mode='w') as file:
                json.dump(d,file,indent=4)
    os.remove('downloads/weather_combined.json')


def normalize_hourly_weather_data(filepath):
    """
    Flattening of Open-Meteo API JSON into a DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the saved weather JSON file.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing hourly records.
    """
    with open(filepath, 'r') as file:
        data = json.load(file)


    hourly = data["hourly"]
    variables = [k for k in hourly.keys() if k != "time"]
    records = []
    for i, t in enumerate(hourly["time"]):
        record = {"time":t}
        for var in variables:
            record[var] = hourly[var][i]
        records.append(record)

    df = pd.json_normalize(records)
    for meta_key in ["latitude", "longitude"]:
         if meta_key in data:
              df[meta_key] = data[meta_key]
    
    df["time"] = df["time"].str.replace("T", " ")
    df["time"] = pd.to_datetime(df["time"])
    return df
    
def main():
    decompose_weather_data()
    
    data = normalize_hourly_weather_data("downloads/weather_lat_28.625_long_76.875.json")
    

if __name__ == "__main__":
     main()