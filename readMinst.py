import struct

filename = '../Data/train-im'

file = open(filename, 'rb')

magic,imgs,rows,cols = struct.unpack('>IIII',file.read(16))

print(magic)
print(imgs)
print(rows)
print(cols)

