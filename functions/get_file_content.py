import os
from config import FILE_CONTENT_MAX_SIZE
from functions.helper import is_in_working_directory
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specific file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to retrieve, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    # check that the file is in the working directory
    work_abs = os.path.abspath(working_directory)
    full_abs = os.path.abspath(os.path.join(work_abs, file_path))
    if not is_in_working_directory(working_directory, file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(full_abs, 'r', encoding='utf-8') as f:
            content = f.read()
        return content[:FILE_CONTENT_MAX_SIZE] + f'[...File "{file_path}" truncated at {FILE_CONTENT_MAX_SIZE} characters]' if len(content) > FILE_CONTENT_MAX_SIZE else content
    except Exception as e:
        return f'Error: Failed to read "{file_path}": {e}'
    