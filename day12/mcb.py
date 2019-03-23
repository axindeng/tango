
# 
# 多重剪贴板
#
#  针对要检查的关键字，提供关键字参数
# (1)如果关键字是save，保存到对应的关键字剪贴板 
# (2)如果关键字是list，列出已有的所有关键字剪贴板
# (3)如果关键字是其他，根据关键字读取对应的剪贴板
#

# usage:
# mcb.pwy list  
# mcb.pwy save keyword
# mcb.pwy keyword

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1] == 'save':
    # save keyword
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':

    
    # list keyword
    # load contend 



mcbShelf.close()

