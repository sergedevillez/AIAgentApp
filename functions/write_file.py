import os
from functions.helper import is_in_working_directory
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specific file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

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