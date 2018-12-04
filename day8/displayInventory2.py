'''
你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字典。其中键是字符串，描述清单中的物品，值是一个整型值，
说明玩家有多少该物品。
例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 意味着玩家有1 条绳索、6 个火把、42枚金币等。 
写一个名为 displayInventory()的函数，它接受任何可能的物品清单，并显示如下： 
Inventory: 
12 arrow  
42 gold coin 
1 rope  
6 torch 
1 dagger  
Total number of items: 62

'''
inv = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k ,v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print('Total number of items: ' + str(item_total))

#displayInventory(stuff)

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','ruby','dagger','tiger']

def addToInventory(inventory,addedItems):
    for i in range(len(addedItems)):
        item = addedItems[i]
        inventory.setdefault(item,0)
        inventory[item] += 1        
    return inventory

#inv = {'gold coin':42,'rope':1}
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
