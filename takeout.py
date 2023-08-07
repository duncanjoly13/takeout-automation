import glob, sys, zipfile

directory = ""
output_folder_path = r"./MOVE_ME/"
source_folder_path = r"./ZIPS_HERE/"

all_zips = glob.glob(source_folder_path)

for zip in all_zips:
    pass