import requests
import pandas as pd

def get_faostat_data(
    domain="PP",
    area="68",
    element="5532",
    item="15",
    year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
):
    """
    Retrieves CAM data for a given domain, and certain parameters 
    (area, element, item, year).
    For items, here is the list of codes for cereals:
    - 15: Wheat
    - 75: Oats
    - 270: Rapeseed
    - 267: Sunflower
    - 56: Corn
    Returns a pandas DataFrame.
    """

    base_url = "https://faostatservices.fao.org/api/v1/en/data"
    url = f"{base_url}/{domain}"

    params = {
        "area": area,
        "element": element,
        "item": item,
        "year": year
    }

    print("Sending request to:", url)
    response = requests.get(url, params=params)
    response.raise_for_status()

    data_json = response.json()

    records = data_json.get("data", [])
    if not records:
        print("No data returned by the API FAOSTAT.")
        return pd.DataFrame()

    df = pd.DataFrame(records)

    return df


if __name__ == "__main__":
    df_wheat = get_faostat_data(
        domain="PP",
        area="68",
        element="5532",
        item="15",
        year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
    )

    df_oats = get_faostat_data(
        domain="PP",
        area="68",
        element="5532",
        item="75",
        year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
    )

    df_rapeseed = get_faostat_data(
        domain="PP",
        area="68",
        element="5532",
        item="270",
        year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
    )

    df_sunflower = get_faostat_data(
        domain="PP",
        area="68",
        element="5532",
        item="267",
        year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
    )

    df_corn = get_faostat_data(
        domain="PP",
        area="68",
        element="5532",
        item="56",
        year="2023,2022,2021,2020,2019,2018,2017,2016,2015,2014",
    )

    df_wheat.to_csv("data/wheat_france_prices.csv", index=False)
    df_oats.to_csv("data/oats_france_prices.csv", index=False)
    df_rapeseed.to_csv("data/rapeseed_france_prices.csv", index=False)
    df_sunflower.to_csv("data/sunflower_france_prices.csv", index=False)
    df_corn.to_csv("data/corn_france_prices.csv", index=False)
