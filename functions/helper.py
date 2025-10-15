
import os


def is_in_working_directory(working_directory, file_path):
    work_abs = os.path.abspath(working_directory)
    full_abs = os.path.abspath(os.path.join(work_abs, file_path))
    return os.path.commonpath([work_abs, full_abs]) == work_abs