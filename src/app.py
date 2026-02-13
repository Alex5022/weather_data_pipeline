import extract 
import load 
import transform 
import asyncio

def main():

    # Extracting data 
    asyncio.run(extract.main())
    
    transform.decompose_weather_data()

    # Loading data 
    load.load_to_postgresql()

if __name__ == "__main__":
    main()