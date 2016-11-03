-- 卡拉兹(Callatz)猜想

function calcCallatz(num, i)
	if num == 1 then return i end
	
	if num % 2 ~= 0 then
		num = num * 3 + 1
	end 
	num = num / 2
	return calcCallatz(num, i + 1)
end

-- print("please enter a integer: ")
integer = io.read("*num")
print(calcCallatz(integer, 0))

