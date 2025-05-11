#!/usr/bin/python3
print('\n'.join(["{} = 0x{}".format(i, format(i, 'x')) for i in range(99)]))