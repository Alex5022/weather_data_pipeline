
import os
import json
import asyncio
import aiohttp
import aiofiles


async def fetch_weather_data(url,params,session):
    """
    Fetch weather forecast data asynchronously from the url API and save it to a local JSON file.
    
    Parameters
    ----------
     url : str
        The API endpoint URL.
    params : dict
        Dictionary of query parameters for the request. Must include at least:
        - "latitude" (float or list of floats)
        - "longitude" (float or list of floats)

        Additional parameters (e.g., "hourly") may be included.
    session : aiohttp.ClientSession
        An active aiohttp session used to perform the HTTP request.

    File Output
    -----------
    - If `params["latitude"]` and `params["longitude"]` are  single values:
        File is saved as `downloads/weather_lat_<latitude>_long_<longitude>.json`
    - If `params["latitude"]` and `params["longitude"]` are lists:
        File is saved as `downloads/weather_combined.json`

    Returns
    -------
    None
    """
    cwd = os.getcwd()
    os.makedirs(f"{cwd}/downloads", exist_ok=True)
    async with session.get(url,params=params, timeout= 15) as response:
        try:
            response.raise_for_status()
            if type(params["latitude"]) != list:
                filename = f"downloads/weather_lat_{params['latitude']}_long_{params['longitude']}.json"
            else:
                filename = f"downloads/weather_combined.json"
            async with aiofiles.open(filename,mode = "wb") as file:
                async for chunk in response.content.iter_chunked(4096):
                    await file.write(chunk)
            print(f"Saved:{filename}")    

        except aiohttp.ClientResponseError as e:
            print(f"Response error: {e.status} {e.message}")
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error: {e}")
        except asyncio.TimeoutError:
            print("Timeout error")
        except aiohttp.ClientPayloadError as e:
            print(f"Payload error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


     
async def fetch_all_weather_data(url,params_list):
    """
    Fetch multiple weather datasets concurrently from the Open-Meteo API.

    Parameters
    ----------
    url : str
        The API endpoint URL (e.g., "https://api.open-meteo.com/v1/forecast").
    params_list : list[dict] or dict
        Either:
        - A list of parameter dictionaries, each containing query parameters such as
          "latitude", "longitude", and optional fields like "hourly".
        - A single parameter dictionary for one request.
    """

    async with aiohttp.ClientSession() as session:
        tasks = []
        if type(params_list) == list:
            for params in params_list:
                tasks.append(fetch_weather_data(url,params,session))
        else:
            tasks.append(fetch_weather_data(url,params_list,session))

        await asyncio.gather(*tasks)


def load_params(params_filepath):
    with open('weather_fetch_params.json', mode = 'r') as file:
        return json.load(file)


async def main():

    params = load_params("weather_fetch_params.json")

    url = "https://api.open-meteo.com/v1/forecast"

    await fetch_all_weather_data(url,params)

if __name__ == "__main__":
    asyncio.run(main())