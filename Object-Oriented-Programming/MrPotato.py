class Potato:
    def __init__(self, right_arm=[], left_arm=[], right_leg=[], left_leg=[], smile=[], eyes=[], bag=[]):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.smile = smile
        self.eyes = eyes
        self.bag = bag
    
    def __str__(self):
        return f'Mr Potato features {self.right_arm} : {self.left_arm} : {self.right_leg} : {self.left_leg} : {self.smile} : {self.eyes} : {self.bag}'


# spud = Potato('right arm','left arm','right leg','left leg','cheek to cheek smile','blue eyes','bag')
# print(spud)



class Item():
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return f'item_name: {self.item_name} : item_description: {self.item_description} '
    
 
# item = Item('eyes', 'ginger eyes')
# print(item)

items = {
    'right_arm': Item('right_arm','right arm'),
    'left_arm': Item('left_arm','left arm'),
    'right_leg': Item('right_leg','right leg'),
    'left_leg': Item('left_leg','left leg'),
    'smile': Item('smile','fake ass frown'),
    'eyes': Item('eyes', 'brown eyes'),
    'eyes': Item('eyes', 'hazel eyes'),
    'eyes': Item('eyes', 'blue eyes'),
    'smile': Item('smile', 'super happy'),
    'left_leg': Item('smile', 'sad'),
    'left_arm': Item('smile', 'grin'),
    'right_arm': Item('smile', 'wut?'),
    'right_leg': Item('smile', 'ohh (spillin tea)'),
}

for i in items:
    print(i)

print(items['smile'])