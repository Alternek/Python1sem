# Сгенерировать файл с неубывающими целыми числами
# За один цикл убрать повторы

import struct

numbers = [10, 10, 15, 15, 15, 15, 16, 16, 18, 22, 22, 80, 80, 92, 95, 95, 101, 102, 103, 104, 105, 1000, 1000, 1000]

with open('1.txt', 'wb+') as file:
    file.write(struct.pack('{}q'.format(len(numbers)), *numbers))
with open('1.txt', 'rb') as file:
    print(struct.unpack('{}q'.format(len(numbers)), file.read()))
with open('1.txt', 'rb+') as file:
    num_last = None
    u_count = 0
    while True:
        num_bin = file.read(8)
        if not num_bin:
            break
        num = struct.unpack('q', num_bin)
        if num != num_last:
            last_tell = file.tell()
            file.seek(8 * u_count)
            file.write(num_bin)
            file.seek(last_tell)
            u_count += 1
        num_last = num
    file.truncate(u_count * 8)
with open('1.txt', 'rb') as file:
    print(struct.unpack('{}q'.format(u_count), file.read(u_count * 8)))
