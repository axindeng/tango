#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##########################################

import os,zipfile
def backup2zip(folder):
    #todo
#1.确定备份文件名的编号
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if  os.path.exists(zipFileName):
            number = number + 1
        else:
            break
    
#2.使用os.walk进行递归压缩
    backupZipfile = zipfile.ZipFile(zipFileName,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        print('Adding folder in %s....' % (foldername) )
        backupZipfile.write(foldername)
        for file in filenames:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            filename = os.path.join(foldername,file)
            print('Adding file   in %s....' % filename)
            backupZipfile.write(filename)
    backupZipfile.close()
    
    print('Done.')
    print(zipFileName)
backup2zip('E:\\python\\tango')
#backup2zip('E:\\docker')
