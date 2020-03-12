from glob import glob
from os import stat

def reverse(lst):
    return [ele for ele in reversed(lst)]

files = glob("./videos/*.mp4")
sorted_list = sorted(files, key=lambda x: stat(x).st_mtime)

truncated_list=reverse(sorted_list)
#truncated_list = sorted_list

print(truncated_list)
hundred_list=truncated_list[-100:]


with open('your_file.txt', 'w') as f:
        for item in hundred_list:
                    f.write("%s\n" % item)

