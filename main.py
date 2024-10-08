from DuplicateRemover import DuplicateRemover

DIR_NAME = "../duplicate-images"

# Remove Duplicates
dr = DuplicateRemover(DIR_NAME)
dr.find_duplicates()

# Find Similar Images
dr.find_similar("IMG-20110704-00007.jpg",70)
