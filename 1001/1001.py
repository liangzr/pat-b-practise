# coding:utf-8
# 卡拉兹(Callatz)猜想

def calc_callatz(num, i = 0):
	if num == 1: 
		return i

	if num % 2 != 0: 
		num = num * 3 + 1

	num = num / 2
	return calc_callatz(num, i + 1)

print "please enter a integer: "
integer = input()
print calc_callatz(integer)