Dictionary = [chr(i) for i in range(128)]
data = [char for char in input("Enter the data : ")]
Compressed_Data = []
check=''
i = 1
while i < len(data):
    pattern = data[i - 1]
    pattern += data[i]
    if pattern in Dictionary:
            check=pattern
            try:
                check += data[i + 1]
                for x in range(i,len(data)):
                    if check in Dictionary:
                       check+=data[x+1]
            except:
                    check +=data[i]
            if check not in Dictionary:
                Dictionary.append(check)
            index = Dictionary.index(check[:-1])
            Compressed_Data.append(index)
            check_len = len(check)
            i += (check_len)-2
    else:
        Dictionary.append(pattern)
        index = Dictionary.index(pattern[:-1])
        Compressed_Data.append(index)
    i += 1

# print(Compressed_Data)
print("Compressed Data:", end=" ")
for i in range(len(Compressed_Data)):
    print(Compressed_Data[i], end=" ")
