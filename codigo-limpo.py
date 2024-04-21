import os

def check_create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print("Directory created:", dir_path)
    else:
        print("Directory exists.")
