import geopandas as gpd
import requests
import pandas as pd
from shapely.geometry import shape
from sodapy import Socrata
import json
import urllib

http_proxy = "http://chancar:Statcan123@stcweb.statcan.ca:80"
https_proxy = "https://chancar:Statcan123@stcweb.statcan.ca:80"

proxyDict = {
    "http": http_proxy,
    "https": https_proxy,
}

root = "https://opendata.vancouver.ca/api/records/1.0/search//"
search_para = "?dataset="
search_text = "parks"
van_root = "https://opendata.vancouver.ca/api/records/1.0/search//?dataset=parks-polygon-representation&rows=1000"
cal_root = "https://data.calgary.ca/resource/kami-qbfh.json"
ott_root = "https://opendata.arcgis.com/datasets/cfb079e407494c33b038e86c7e05288e_24.geojson"
tor_root = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_search?q=name:parks"

r = requests.get(tor_root, proxies=proxyDict)
r.raise_for_status()
response = r.json()

# test = response["records"]
# fields = []
# for field in test:
#     fields.append(field["fields"])
#
#
# def json_to_table(json):
#     col_name = list(json[0].keys())
#     parks = pd.DataFrame(columns=col_name)
#     i = 0
#     for park in json:
#         for name in list(park.keys()):
#             if "geom" in name:
#                 parks.loc[i, name] = park[name]['coordinates']
#             else:
#                 parks.loc[i, name] = park[name]
#         i = i + 1

# for geo in response:
#     geo["the_geom"] = shape(geo["the_geom"])
#
# gdf = gpd.GeoDataFrame(response).set_geometry("the_geom")
# gdf.to_file("./output/test.shp")
