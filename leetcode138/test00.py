def rev(n):  # 32-bit bit-reversion
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n

print(bin(240&0xFFFFFFFF))                    #                          0b11110000
print(format(240&0xFFFFFFFF, '#034b'))        #  0b00000000000000000000000011110000
print(bin(rev(240&0xFFFFFFFF)))               #  0b1111000000000000000000000000
print(format(rev(240&0xFFFFFFFF), '#034b'))   #  0b00001111000000000000000000000000

print(bin(-240&0xFFFFFFFF))                   #  0b11111111111111111111111100010000
print(format(-240&0xFFFFFFFF, '#034b'))       #  0b11111111111111111111111100010000
print(bin(rev(-240&0xFFFFFFFF)))              #  0b1000111111111111111111111111
print(format(rev(-240&0xFFFFFFFF), '#034b'))  #  0b00001000111111111111111111111111

