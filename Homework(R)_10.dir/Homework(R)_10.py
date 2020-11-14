import os

initial_directory_path = "/Users/User/Desktop/"

def create_a_testing_work_environment(initial_directory_path):
    os.mkdir(os.path.join(initial_directory_path, "test"))
    with open(os.path.join(initial_directory_path, "test", "file_1.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "file_2.txt"), 'w'):
        pass
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_1"))
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_2"))
    with open(os.path.join(initial_directory_path, "test", "dir_1", "file_3.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "dir_1", "file_4.txt"), 'w'):
        pass
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_1", "dir_3"))
    with open(os.path.join(initial_directory_path, "test", "dir_1", "dir_3", "file_5.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "dir_1", "dir_3", "file_6.txt"), 'w'):
        pass
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_1", "dir_3", "dir_4"))
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_1", "dir_3", "dir_5"))
    with open(os.path.join(initial_directory_path, "test", "dir_1", "dir_3", "dir_4", "file_7.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "dir_2", "file_8.txt"), 'w'):
        pass
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_2", "dir_6"))
    os.mkdir(os.path.join(initial_directory_path, "test", "dir_2", "dir_7"))
    with open(os.path.join(initial_directory_path, "test", "dir_2", "dir_6", "file_9.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "dir_2", "dir_6", "file_10.txt"), 'w'):
        pass
    with open(os.path.join(initial_directory_path, "test", "dir_2", "dir_7", "file_11.txt"), 'w'):
        pass


create_a_testing_work_environment(initial_directory_path)

directory = os.path.join(initial_directory_path, "test")

def delete_all_the_files_and_directories_recursively(directory):
    for path in os.listdir(directory):
        new_path = os.path.join(directory, path)
        if os.path.isfile(new_path):
            os.remove(new_path)
        elif os.path.isdir(new_path):
            delete_all_the_files_and_directories_recursively(new_path)
    for path in os.listdir(directory):
        os.rmdir(os.path.join(directory, path))


delete_all_the_files_and_directories_recursively(directory)