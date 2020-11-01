list  = []
# Сама функция
def tipes(*arg):
	for i in arg:
		list.append(type(i))
	print(list)
#
a = input()
d = input()
c = input().split()
tipes(a, d, c)