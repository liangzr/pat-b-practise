convert_table = {"ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"}
result = ""

function number2pinyin(naturalNum, i)

	-- sum
	tmpNum = 0;
	list = num2list(naturalNum)
	for i=1, #list do
		tmpNum = tmpNum + list[i]
	end

	-- convert
	list = num2list(tostring(tmpNum))
	for i=1, #list do
		result = result .. convert_table[list[i]+1] .. " "
	end

	return string.sub(result, 1, string.len(result) - 1)
end

function num2list(str)
	list = {}
	for i=1, string.len(str) do
		list[i] = tonumber(string.sub(str, i, i))
	end
	return list
end

-- print("please enter a integer: ")
string = tostring(io.read("*l"))
print(number2pinyin(string))