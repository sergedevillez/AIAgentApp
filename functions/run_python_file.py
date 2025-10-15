import os
import subprocess
from functions.helper import is_in_working_directory


def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []

    if not is_in_working_directory(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.join(working_directory, file_path)):
        return f'Error: File "{file_path}" not found'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ["python", os.path.join(os.path.abspath(working_directory), file_path)] + args
        print(cmd)
        completed_process = subprocess.run(
            cmd,
            timeout=30,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.abspath(working_directory),
        )

        if completed_process.returncode != 0:
            return f'Process exited with code {completed_process.returncode}'
        if completed_process.stdout is None and completed_process.stderr is None:
            return 'No output produced.'
        elif completed_process.returncode != 0:
            return f'Error: Process exited with code {completed_process.returncode}\nSTDOUT: {completed_process.stdout.decode()}\nSTDERR: {completed_process.stderr.decode()}'
        else:
            return f'STDOUT: {completed_process.stdout.decode()}\nSTDERR: {completed_process.stderr.decode()}'
    except Exception as e:
        return f'Error: executing Python file: {e}'
