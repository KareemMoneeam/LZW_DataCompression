Dictionary = [chr(i) for i in range(128)]
data = list(map(int, input("Enter the data : ").split()))
Decompressed_Data = []
for i in range(len(data)):
    if data[i] < len(Dictionary):
            letter = Dictionary[int(data[i])]
            Decompressed_Data.append(letter)
            for i in range(1, len(data)):
                # takes the previous found pattern + the first letter of the next pattern
                # if the index of the pattern doesn't exist in the table
                # put the pattern you have and extend it with the first letter of your pattern
                pattern = Dictionary[data[i-1]]
                try:
                     pattern += Dictionary[data[i]][0]
                except:
                     pattern = Dictionary[data[i-1]]+Dictionary[data[i-1]][0]
                if pattern not in Dictionary:
                    Dictionary.append(pattern)

print("Decompressed Data: ", end=" ")
for i in range(len(Decompressed_Data)):
 print(Decompressed_Data[i], end="")
