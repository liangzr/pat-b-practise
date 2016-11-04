function match(str)
    -- only P、A、T
    if not onlyPAT(str) then
        -- print("not only PAT")
        return false
    end

    -- xPATx is currect
    if xPATx(str) then
        return true
    else
        -- print("origin string not xPATx")
        return subRecur(str)
    end

end

function onlyPAT(str)
    i, j = string.find(str, "[PAT]+")
    return i, j
end

function xPATx(str)
    i, j = string.find(str, "PAT")
    if not i then return false end

    frontStr = string.sub(str, 0, i - 1)
    backStr = string.sub(str, j + 1, string.len(str))
    if frontStr == backStr and checkA(frontStr) and checkA(backStr) then
        return true
    else
        -- print("not xPATx")
        return false
    end
end

function checkA(str)
    if string.find(str, "^[A]*$") then
        return true
    else
        -- print("not A")
        return false
    end
end

-- aPbTc -> aPbATca -> aPbAATcaa ...
function subRecur(str)
    i, j = string.find(str, "PA+T")
    if not i then 
        -- print("no i, j for recur")
        return false 
    end
    frontStr = string.sub(str, 0, i - 1)
    backStr = string.sub(str, j + 1, string.len(str))

    if (string.len(frontStr) > string.len(backStr)) or not checkA(frontStr) or not checkA(backStr) then
        -- print("can not recur")
        return false
    end

    -- intercept aPbATca to aPbTc
    newStr = string.sub(str, 0, j-2) .. string.sub(str, j, string.len(str))
    newStr = string.sub(newStr, 0, string.len(newStr) - string.len(frontStr))
    if xPATx(newStr) then
        return true
    else
        -- print("new recur: " .. newStr)
        return subRecur(newStr)
    end
end

-- print("please enter the number of stirngs: ")
local list = {}

totel = tonumber(io.read("*l"))
for i=1,totel do
     -- print("enter string you want to check: ")
    str = io.read("*l")
    list[i] = match(str)
end

for k,v in ipairs(list) do
    if v then 
        print("YES")
    else
        print("NO")
    end
end