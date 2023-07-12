from collections import Counter

def addToInventory(inventory, addedItems):
    items_counter = Counter(addedItems)
    inventory_counter = Counter(inventory)
    new_inventory = dict(items_counter + inventory_counter)
    
    return new_inventory
    
def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for k,v in inventory.items():
        print(v,k)
        total_items = total_items + v
    print('\nTotal number of items: {0}'.format(total_items))
    
     
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)