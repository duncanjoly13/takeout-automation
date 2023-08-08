import glob, os, shutil, zipfile

class Migrate():
    def __init__(self):
        self.output_file_path = r'./MOVE_ME/'
        self.first_extracted_file_structure = r'./first_extracted/'
        self.second_extracted_file_structure = r'./second_extracted/'
        self.all_zip_paths = glob.glob('*.zip')
        print('zip files to be extracted:')
        print(self.all_zip_paths)
        print()

    def run(self):
        # check for zips
        if self.all_zip_paths == []:
            print('no .zip files found!')
            print('ensure that your takeout .zip files are in this directory')
            print()
            no_zips_user_input = input('press "q" then "Enter" to exit\n')
            print()
            while no_zips_user_input != 'q':
                print('invalid input!')
                print()
                no_zips_user_input = input('press "q" then "Enter" to exit\n')
                print()
            if no_zips_user_input == 'q':
                return
        
        # check for output folder
        if os.path.isdir(self.first_extracted_file_structure):
            print('WARNING: output folder ' + self.first_extracted_file_structure + ' exists!')
            folder_exists_user_input = input('press "q" then "Enter" to quit or "a" then "Enter" to proceed\n')
            print()
            while (folder_exists_user_input != 'q') and (folder_exists_user_input != 'a'):
                print('invalid input!')
                print()
                folder_exists_user_input = input('press "q" then "Enter" to quit or "a" then "Enter" to proceed\n')
            if folder_exists_user_input == 'q':
                return
            if folder_exists_user_input == 'a':
                print('proceeding...')
                print()

        # extract each zip to self.first_extracted_file_structure
        for zip_path in self.all_zip_paths:
            print('extracting ' + zip_path + '...')
            new_zip_obj = zipfile.ZipFile(zip_path)
            new_zip_obj.extractall(path = self.first_extracted_file_structure)
            new_zip_obj.close()
            print(zip_path + ' completed, moving on...')
            print()

        print('all .zip files in the current directory have been extracted to ' + self.first_extracted_file_structure + ', rearranging folder structure')
        print()

        # move files to self.second_extracted_file_structure and remove one irrelevant directory level
        for entry in os.scandir(self.first_extracted_file_structure):
            shutil.move(entry.path, self.second_extracted_file_structure)

        # delete self.first_extracted_file_structure
        os.rmdir(self.first_extracted_file_structure)

        # move files to self.output_file_path and remove the other irrelevant directory level
        for entry in os.scandir(self.second_extracted_file_structure):
            shutil.move(entry.path, self.output_file_path)

        print('folders rearranged, deleting .json files')
        print()

        # delete all .json files
        for file in glob.glob("**/*.json", recursive=True):
            os.remove(file)

        # delete self.second_extracted_file_structure
        os.rmdir(self.second_extracted_file_structure)

        # see if the user wants to delete the .zip files
        print('completed!')
        print()
        print('would you like to delete the zip files as they are no longer needed?')
        delete_zips_user_input = input('press "y" then "Enter" to delete the unneeded files or "n" then "Enter" to leave them alone\n')
        print()
        while (delete_zips_user_input != 'n') and (delete_zips_user_input != 'y'):
            print('invalid input!')
            delete_zips_user_input = input('press "y" then "Enter" to delete the unneeded files or "n" then "Enter" to leave them alone\n')
        if delete_zips_user_input == 'n':
            print('your files may be found in ' + self.first_extracted_file_structure + ', either rename that folder and move it to the directory of your choice' + \
                '(e.g. C://Users/YOUR_USERNAME/Pictures/) or drag its contents to a directory of your choice if you\'ve done this before')
            print('exiting...')
        if delete_zips_user_input == 'y':
            for zip_file in self.all_zip_paths:
                if os.path.isfile(zip_file):
                    print('deleting ' + zip_file)
                    os.remove(zip_file)
            print()
            print('all zip files have been deleted')
            print()
            print('your files may be found in ' + self.first_extracted_file_structure + ', either rename that folder and move it to the directory of your choice' + \
                '(e.g. C://Users/YOUR_USERNAME/Pictures/) or drag its contents to a directory of your choice if you\'ve done this before')
            print('exiting...')

        
if __name__ == '__main__':
    migration = Migrate()
    migration.run()