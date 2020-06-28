#list mutable [ , ] => [ , , ] with elements: mut/imm
l1 = [1,2]
l2 = [1,2]
print(id(l1))
print(id(l2))

l1 = [1,2]
l2 = l1
print(id(l1))
print(id(l2))

# tuple: immutable ( , ) with elements: mut/imm
t = (1,[1,2])
t[1].append(3)
print(t)

# set: mutable { , } => { , , } with elements imm

#dictionary: mutable with elements: (key, value) key: imm, value: imm/mut
