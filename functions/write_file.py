import os
from functions.helper import is_in_working_directory


def write_file(working_directory, file_path, content):
    work_abs = os.path.abspath(working_directory)
    full_abs = os.path.abspath(os.path.join(work_abs, file_path))
    if not is_in_working_directory(working_directory, file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_abs) :
        # create file if not exists
        os.makedirs(os.path.dirname(full_abs), exist_ok=True)
        
    try:
        with open(full_abs, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to create and write to "{file_path}": {e}'