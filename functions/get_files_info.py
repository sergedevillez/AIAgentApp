import os
from functions.helper import is_in_working_directory


# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator



def get_files_info(working_directory, directory="."):
    """List files under working_directory/directory and return a textual report.

    The function treats `directory` as a path relative to `working_directory`.
    It joins the two, normalizes to absolute paths, and checks containment
    using os.path.commonpath so user-supplied absolute paths or `..` cannot
    escape the allowed working directory.
    """
    # Normalize working directory to an absolute path
    work_abs = os.path.abspath(working_directory)
    # Join under the working directory and make absolute
    full_abs = os.path.abspath(os.path.join(work_abs, directory))

    # Ensure the final path is inside the working directory
    if not is_in_working_directory(working_directory, directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_abs):
        return f'Error: "{directory}" is not a directory'

    report = ''
    try:
        for entry in sorted(os.listdir(full_abs)):
            entry_path = os.path.join(full_abs, entry)
            try:
                file_size = os.path.getsize(entry_path) if os.path.exists(entry_path) else 0
            except Exception:
                file_size = 0
            is_dir = os.path.isdir(entry_path)
            report += f'- {entry}: file_size={file_size} bytes, is_dir={is_dir}\n'
    except Exception as e:
        return f'Error:{e}'

    return report
