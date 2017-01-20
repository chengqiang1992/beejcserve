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
