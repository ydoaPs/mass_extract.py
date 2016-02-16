#MassExtract.py

def mass_extract(source_directory, target_directory):
    """This, hopefully, will extract large numbers of zipped files to a target folder. This version is for python 2 only since it uses 'raw_input()' rather than 'input()'."""

    import os
    import ZipFile

    source_directory = raw_input("Where are the zips? ")
    target_directory = raw_input("To where do you want to extract the files? ")
    
    if not os.path.exists(source_directory):
        print "Sorry, that folder doesn't seem to exist."
        source_directory = raw_input("Where are the zips? ")

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)
        
    for path, directory, filename in os.walk(source_directory):
        zip_file = ZipFile.ZipFile(filenames)
        ZipFile.extract(zip_file, target_directory)
        zip_file.close()

    print "Done."
