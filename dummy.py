from glob import glob
from os import stat

files = glob("./videos/*.mp4")
sorted_list = sorted(files, key=lambda x: stat(x).st_mtime)

truncated_list = sorted_list[-10:]
