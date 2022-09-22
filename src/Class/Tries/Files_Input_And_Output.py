import pathlib

home = pathlib.Path.home()

print(home)

current_Working_Directory = pathlib.Path.cwd()
print(current_Working_Directory)

# To check if a file path is absolute i.e. if it begins from the root folder.
print(home.is_absolute())

# The .parents attribute of a Path object returns an iterable containing the list of directories in the file path:
iterating_the_file_directory = list(current_Working_Directory.parents)
print(iterating_the_file_directory)

# LOOK THEM UP i pages 339 - 341
# .exists()
# .is_file()
# .is_dir()













# print("You left off at page 341")
