def isValid(s: str) -> bool:
    open   = ['[','{','(']
    close = [']','}',')']
    list =[]
    brackets = {'[' : 1, '{' : 2, '(' : 3, ']' : 4, '}' : 5, ')' : 6}
    for i in range(len(s)):
        print("i:" , i)
        print("s[i]", s[i])
        print("list:", list)
        print("len: ", len(list))
        if i == 0:
            if s[i] in open:
                list.append(s[i])
                # print(list)
            else:
                return False
        else:
            if s[i] in open:
                list.append(s[i])
                print("if s[i] in open:")
            else:
                if s[i] in close and len(list) > 0:
                    print("if s[i] in close:")
                    print("list[-1]: ",list[-1])
                    print("close index: ",close.index(s[i]))
                    #to samo co (list[-1]) == list(len(list)-1)
                    try:
                        if open.index(list[-1]) == close.index(s[i]):
                            # list.pop(len(list)-1)
                            list.pop()
                            # print(list)
                        else:
                            return False
                    except ValueError:
                        return False
                else:
                    print("add to list")
                    list.append(s[i])

    return len(list) == 0


# isValid('[][][][][][]')
print(isValid('[][][({})]{{{{{[][]}[]}}[]}}'))

print("\n\n--------------------------------\n\n")
def isValidInternet(s: str) -> bool:
    brackets = { ")": "(", "]":"[", "}":"{" }
    if s[0] in brackets:
        return False
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] in brackets:
            if not stack: return False

            check = stack.pop()
            print("Checks: ",check)
            print("brackets[s[i]]: ",brackets[s[i]])
            if check != brackets[s[i]]:
                return False
        else:
            stack.append(s[i])
        print(stack)
    return len(stack) == 0

print(isValidInternet("(([(){]{})})"))