def get_file_info(file_path):
    *path_file, buf_str = file_path.split("/")
    path_file = "" if len(path_file) == 0 else "/".join(path_file) + "/"
    name_file, type_file = (".".join(buf_str.split(".")[:-1]), "." + buf_str.split(".")[-1]) if "." in buf_str else ("", "." + buf_str)
    return path_file, name_file, type_file

print(get_file_info("C:/Users/User/Documents/example.txt"))
print(get_file_info("/home/user/data/file"))
print(get_file_info("/home/user/docs/my.file.with.dots.txt"))
print(get_file_info("file_in_current_directory.txt"))
