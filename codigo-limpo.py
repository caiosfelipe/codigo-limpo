import os

def create_directory_if_missing(directory_path):
    """Ensure that the specified directory exists; create it if it does not.

    Args:
    directory_path (str): The file path to the directory to check and potentially create.

    Returns:
    None
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    else:
        print("Directory already exists.")
