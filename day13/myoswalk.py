import os

for folderName,subfolders,filenames in os.walk('E:\\我的工作文档\\1.全资产投资管理平台\\oracle'):
    print('The Current Folder is ' + '<<< ' + folderName + ' >>>' )
    for subfolder in  subfolders:
        print('   subfolder of ' + folderName + ': ' + subfolder )
    for filename  in   filenames:
        print('   InsideFile of ' + folderName + ':    ' + filename)
    print('')