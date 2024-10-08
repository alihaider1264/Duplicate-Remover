import os
from PIL import Image
import imagehash
import numpy as np
from tqdm import tqdm

class DuplicateRemover:
    """Class finds and removes duplicates"""

    def __init__(self,dirname,hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
       
    def find_duplicates(self):
        """
        Find and Delete Duplicates
        """
        
        fnames = os.listdir(self.dirname)
        hashes = {}
        duplicates = []
        print("Finding Duplicates in {}".format(self.dirname))
        for image in tqdm(fnames):
            with Image.open(os.path.join(self.dirname,image)) as img:
                temp_hash = imagehash.dhash(img, self.hash_size)
                if temp_hash in hashes:
                    print("{:20s} {:20s} {}".format(image, hashes[temp_hash], temp_hash))
                    duplicates.append(image)
                else:
                    hashes[temp_hash] = image
                   
        if len(duplicates) != 0:
            print("What would you like to do with the", str(len(duplicates)), " duplicates images found? \nd: Delete them\nm: Move them\nn: Do nothing")
            a = input()
            space_saved = 0
            if(a.strip().lower() == "m"):
                print("Note that files with same name in the moved folder will be overwritten.")
                new_folder = input("Enter name for the new folder to  move duplicated: ")
                if not os.path.isdir(new_folder):
                    os.mkdir(os.path.join(new_folder))
                for duplicate in tqdm(duplicates):
                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
                    os.replace(os.path.join(self.dirname,duplicate), os.path.join(new_folder,duplicate))
                    print(duplicate, "Moved Succesfully!")
    
                print("You saved", str(round(space_saved/1000000,2)) ,"MB of Space!")
            elif(a.strip().lower() == "d"):
                for duplicate in duplicates:
                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
                    os.remove(os.path.join(self.dirname,duplicate))
                    print(duplicate, "Moved Succesfully!")
    
                print("You saved", str(round(space_saved/1000000,2)) ,"MB of Space!")
            else:
                print("Thank you for Using Duplicate Remover")
        else:
            print("No Duplicates Found :(")
            
        
            
            
    def find_similar(self,location,similarity=80):
        """function finds similar images"""

        fnames = os.listdir(self.dirname)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        print("Finding Similar Images to {} Now!".format(location))
        for image in fnames:
            with Image.open(os.path.join(self.dirname,image)) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    print("{} image found {}% similar to {}".format(image,similarity,location))
                    
                    
                    
                
        
            
