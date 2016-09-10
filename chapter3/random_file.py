records=[bytes([char]*8) for char in b'spam']
print(records)

file=open('random.bin','w+b')
for rec in records:
    size=file.write(rec)
    print(size)
file.flush()
pos=file.seek(0)
print(file.read())

record=b'X'*8
file.seek(0)
file.write(record)
file.flush()
print(file.read())