import sys
print(1 / 2)
print(1 // 2)

print(sys.float_info)
print(sys.float_info.max)

n = -37
bin(n)
print(bin(n))
print(n.bit_length())

m = 0
bin(m)
print(bin(m))
print(m.bit_length())

x = 127895
bin(x)
print(bin(x))
print(x.bit_length())

print("gg" in "eggs")

lists = [[]] * 3
print(lists)
lists[0].append(3)
print(lists)

print(range(10))
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(1, 11, 2)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))

r = range(0, 20, 2)
print(list(r))
print(r)
print(11 in r)
print(10 in r)
print(r.index(10))
print(r[5])
print(r[:5])