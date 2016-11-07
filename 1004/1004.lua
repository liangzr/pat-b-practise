function sortByGrade(tb)
    for j=1,#tb-1 do
        for i=j, #tb - 1 do
            if tb[i][3] < tb[i+1][3] then
                tb[i], tb[i+1] = tb[i+1], tb[i]
            end
        end
    end
    print(tb[1][1].." "..tb[1][2])
    print(tb[#tb][1].." "..tb[#tb][2])
end

-- print("please enter number of students: ")
count = tonumber(io.read("*l"))
list = {}
for i=1,count do
    -- print("enter name/id/score, separate theme by space: ")
    s = io.read("*l")
    item = {}   
    for i in string.gmatch(s, "%S+") do
        table.insert(item, i)
    end
    item[3] = tonumber(item[3])
    table.insert(list, item)
end
sortByGrade(list)

