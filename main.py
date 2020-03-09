#!/usr/bin/env python3
import mmap,os,glob,shutil

folder_path = '/some/path/to/file'
report_path = '/some/path/to/file'

for filename in glob.glob(os.path.join(folder_path, '*.html')):
    failFound = false
    with open(filename, 'rb', 0) as file, \
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if re.search(br'(?i)false', s):
            failFound = true
            s.close()
            file.close()
    if(failFound):
        shutil.copy(filename,report_path)