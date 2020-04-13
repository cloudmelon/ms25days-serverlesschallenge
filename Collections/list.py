note1 = ["num1", "num2", "num3"]
note2 = []

note2.append(19)
note2.append(12)
note2.insert(0,10)

print(note1)
print(note2)
print(note1[0])
print(note1[1])

print(len(note1))

note2.sort()
print(note2)

# if you wanna a sub-collection

note3 = note2[1:3] # or note2[:3]
print(note3)