from colorama import Fore

def recover(a):
    """
    Convert the bytearray back into a string. However, modify the string so only
    ascii printable characters are there.
    """
    b = []
    for c in a:
        if 0x7e >= c >= 0x20:  # only print ascii chars
            b.append(chr(c))
        else:  # all others just replace with '.'
            b.append(Fore.RED + '.' + Fore.GREEN)
    ret = ''.join(b)
    return ret


def hexdump(data, cols=80):
    """
    This is the main function which prints everything.
    """
    # print the header
    print(Fore.MAGENTA + 'pyhexdump: {} bytes'.format(len(data)))
    print('ascii characters: GREEN')
    print('non-ascii: RED')
    print(Fore.BLUE + '{:>6} | {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} | {}'.format(
        'Offset(h)',
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        'String'
    ))
    print('-'*cols + Fore.RESET)

    # formating string for each line
    print_string = Fore.BLUE + '{:09X} | ' + Fore.RESET + '{:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} ' + Fore.GREEN + '| {}' + Fore.RESET

    # break data up into 16 byte chunks
    size = 16
    buff = []
    line = [0]*size
    for i, char in enumerate(data):
        if i % size == 0 and i != 0:
            buff.append(line)
            line = [0]*size
            line[0] = char
        else:
            line[i % size] = char

            if i == len(data) - 1:
                buff.append(line)

    # print data out
    for i, line in enumerate(buff):
        if i + 1 == len(buff):
            begin = Fore.BLUE + '{:09X} | ' + Fore.RESET
            item = '{:02x} ' 
            end =  Fore.GREEN + '| {}' + Fore.RESET
            print(begin.format(i), end='') 
            for j, char in enumerate(line):
                if i * len(line) + j < len(data):
                    print(item.format(char), end='')
                else:
                    print('   ', end='')
            print(end.format(recover(line)))
        else:
            print(print_string.format(i,
                                      line[0], line[1], line[2], line[3], line[4], line[5],
                                      line[6], line[7],
                                line[8],
                                line[9],
                                line[10],
                                line[11],
                                line[12],
                                line[13],
                                line[14],
                                line[15],
                                recover(line)
                )
            )

