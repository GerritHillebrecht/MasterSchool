import os

# path = os.path.join("folder", "subfolder")

# print(os.listdir(path))
# print(os.listdir(f"{os.getcwd()}/{path}"))

# FOLDER_NAME = "folder"
# SUBFOLDER_NAME = "subfolder"
# FILE_NAME = "content.py"

# task
FOLDER_NAME = "project"
SUBFOLDER_NAME = "module"
os.mkdir(FOLDER_NAME)
os.mkdir(os.path.join(FOLDER_NAME, SUBFOLDER_NAME))
os.listdir(FOLDER_NAME)
os.chdir(FOLDER_NAME)
os.rename(SUBFOLDER_NAME, f"../{SUBFOLDER_NAME}")
os.chdir("../")
os.rmdir(FOLDER_NAME)
os.rmdir(SUBFOLDER_NAME)



# os.rename(os.path.join(FOLDER_NAME, SUBFOLDER_NAME, FILE_NAME), os.path.join(FOLDER_NAME, FILE_NAME))
# os.rename(os.path.join(FOLDER_NAME, FILE_NAME), os.path.join(FOLDER_NAME, SUBFOLDER_NAME, FILE_NAME))

# if FOLDER_NAME in os.listdir():
#     os.rmdir(FOLDER_NAME)
# print(os.listdir())
# os.mkdir(FOLDER_NAME)

# print(os.getcwd())
print(os.listdir())
