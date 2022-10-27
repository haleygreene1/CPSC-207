def replace_substring(string,remove,add):
    output= []
    index=0
    while index < len(string):
        if string[index:index+len(remove)]== remove :
            index += len(remove)
            output.append(add)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

replace_substring("Hello, I am error how to code!", "error", "learning")
