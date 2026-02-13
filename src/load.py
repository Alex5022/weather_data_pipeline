
import os

from sqlalchemy import create_engine
from transform import normalize_hourly_weather_data

db_url = os.getenv("DATABASE_URL")
def load_to_postgresql():
    """
    Load weather data files from `downloads` folder into a PostgreSQL database.
    """

    files = os.listdir('downloads')

     # postgresql://user:password@host:port/database
    engine = create_engine(db_url)
    for i,file in enumerate(files):
        df = normalize_hourly_weather_data(f"downloads/{file}")
        df.to_sql(f'weather_{i}',engine, if_exists="replace", index=False)
        print(f"File {file} was loaded into table  weather_{i} ")

