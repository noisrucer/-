import os
cur_dir = os.getcwd()

for folder in os.listdir('./'):
    folder_path = os.path.join(cur_dir, folder)
    if not os.path.isdir(folder_path) or folder == ".git":
        continue

    f = open(os.path.join(folder_path, "dummy.txt"), "w")
    f.write("dummy")
    f.close()
