from google.genai import types
from config import WORKING_DIRECTORY
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file

def call_function(function_call_part: types.FunctionCall, verbose=False):
    """Handle the abstract task of calling a function based on the function call part."""
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    if function_call_part.name == "get_files_info":
        get_files_info(working_directory=WORKING_DIRECTORY, *function_call_part.args)
    elif function_call_part.name == "get_file_content":
        get_file_content(working_directory=WORKING_DIRECTORY, file_path=function_call_part.args)
    elif function_call_part.name == "run_python_file":
        run_python_file(working_directory=WORKING_DIRECTORY, file_path=function_call_part.args)
    elif function_call_part.name == "write_file":
        write_file(working_directory=WORKING_DIRECTORY, *function_call_part.args)
    else:
        return f"Error: Unknown function '{function_call_part.name}'"