# coding:utf-8
convert_table = ("ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu")

def sum2pinyin(string):
	# sum
	tmpNum = 0
	for x in xrange(0,len(string)):
		tmpNum = tmpNum + int(string[x])

	# convert
	result = ""
	tmpNum = str(tmpNum)
	for x in xrange(0,len(tmpNum)):
		result = result + convert_table[int(tmpNum[x])] + " "

	return result[:len(result) - 1]

# print "please enter a integer: "
string = raw_input()
print sum2pinyin(string)