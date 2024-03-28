mybag = []

def contains(bag, e):
    return e in bag
def insert(bag, e):
    bag.append(e)
def remove(bag, e):
    bag.remove(e)
def count(bag, e):
    return len(bag)
   
insert(mybag, '휴대폰')
insert(mybag, '휴대폰')
insert(mybag, '휴대폰')
insert(mybag, '휴대폰')
insert(mybag, '휴대폰')
insert(mybag, '휴대폰')
print('가방속의 물건:',mybag)

insert(mybag,'빗')
remove(mybag, '손수건')
print('가방속의 물건:',mybag)
