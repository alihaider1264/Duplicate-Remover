from DuplicateRemover import DuplicateRemover

DIR_NAME = "duplicate_images"

# Remove Duplicates
dr = DuplicateRemover(DIR_NAME)
dr.find_duplicates()

# Find Similar Images
#dr.find_similar("pl_f.png",70)
