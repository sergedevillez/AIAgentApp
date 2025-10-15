import logging
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def test_get_file_info():

    # Each test case is a tuple of (working_directory, directory, expected_substrings_in_output)
    test_cases = [
        ("calculator", ".", ['- main.py: file_size=', ' is_dir=False', '- tests.py: file_size=', 'bytes, is_dir=False', '- pkg: file_size=',' bytes, is_dir=True']),
        ("calculator", "pkg", []),
        ("calculator", "/bin", ['Error: Cannot list "/bin" as it is outside the permitted working directory']),
        ("calculator", "../", ['Error: Cannot list "../" as it is outside the permitted working directory'])
    ]

    for working_dir, dir_to_check, expected in test_cases:
        result = get_files_info(working_dir, dir_to_check)
        for exp in expected:
            assert result.__contains__(exp), f"Expected '{exp}' in result but it was not found."
    logging.info(f'Passed {len(test_cases)} tests for the function get_files_info')

def test_get_file_content():
    test_cases = [
        ("calculator", "lorem.txt", ["lorem ipsum"]),
        ("calculator", "main.py", ['# main.py\n\nimport sys']),
        ("calculator", "pkg/calculator.py", ['# calculator.py\n\nclass Calculator:']),
        ("calculator", "/bin/cat", ["Error:"]),
        ("calculator", "pkg/does_not_exist.py", ["Error:"])
    ]
    for working_dir, dir_to_check, expected in test_cases:
        result = get_file_content(working_dir, dir_to_check)
        for exp in expected:
            assert result.__contains__(exp), f"Expected '{exp}' in result but it was not found."
    logging.info(f'Passed {len(test_cases)} tests for the function get_file_content')


def test_write_file():
    test_cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]

    for working_dir, file_path, content in test_cases:
        write_file(working_dir, file_path, content)
        result = get_file_content(working_dir, file_path)
        assert result == content or result.startswith("Error:"), f"Unexpected content in '{file_path}': {result}"
    logging.info(f'Passed {len(test_cases)} tests for the function write_file')


def test_run_python_file():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    # test_get_file_info()
    # test_get_file_content()
    # test_write_file()
    test_run_python_file()