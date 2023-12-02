import os
from urllib.request import urlretrieve

output_relative_dir = f'datas/'
# download taxi data
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

   

