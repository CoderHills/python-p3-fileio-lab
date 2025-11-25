def write_file(file_name, file_content):
    with open(str(file_name) + ".txt", "w") as f:
        f.write(file_content)  # ✅ remove the \n


def append_file(file_name, append_content):
    with open(str(file_name) + ".txt", "a") as f:
        f.write(append_content)  # ✅ remove the \n


def read_file(file_name):
    with open(str(file_name) + ".txt", "r") as f:
        return f.read()
