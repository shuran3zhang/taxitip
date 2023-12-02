import os
from urllib.request import urlretrieve

output_relative_dir = f'data/'

# download taxi data
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

for type in ['raw']:
    path = output_relative_dir + type
    if not os.path.exists(path):
        os.makedirs(path)

    for source in ['yellow_data']:
        path = output_relative_dir + type + '/' + source
        if not os.path.exists(path):
            os.makedirs(path)

URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

YEAR = '2022'
MONTHS = range(1,13)
for month in MONTHS:
    month = str(month).zfill(2) 
    print(f"Begin month {month}")
    
    url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'

    output_dir = "data/raw/yellow_data/" + YEAR+"-"+month+".parquet"
    # download
    urlretrieve(url, output_dir) 
    
    print(f"Completed month {month}")

