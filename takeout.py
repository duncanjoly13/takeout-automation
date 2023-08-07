import glob, sys, zipfile

class Migrate(): 

    def __init__(self):
        self.output_folder_path = r'./MOVE_ME/'
        self.source_folder_path = r'./ZIPS_HERE/'
        self.all_zip_paths = glob.glob(str(self.source_folder_path + '*.zip'))

    def run(self):
        for zip_path in self.all_zip_paths:
            print('extracting ' + zip_path + '...')
            new_zip_obj = zipfile.ZipFile(zip_path)
            new_zip_obj.extractall(path = self.output_folder_path)
            new_zip_obj.close()
            print(zip_path + ' completed, moving on...')

        print('all files from ' + self.source_folder_path + ' extracted to ' + self.output_folder_path + ', rearranging folder structure')

        # DELETE UNIMPORTANT FOLDERS WHILE RETAINING ALBUM NAMES (e.g. 'Photos from 2023')
        # check if contains non paths and non .jsons

        print('folders rearranged, deleting .json files')

        # DELETE ALL .json FILES FROM ALL DIRECTORIES

        print('completed')
        print('your files may be found in ' + self.output_folder_path + ', either rename that folder and move it to the directory of your choice \
            (e.g. C://Users/YOUR_USERNAME/Pictures/) or drag its contents to a directory of your choice if you\'ve done this before')
        
if __name__ == '__main__':
    migration = Migrate()
    migration.run()