ALPHABET = '0123456789ABCDEF'


def from_2_to_10(in_not, in_num):
    return int(in_num, int(in_not))


def from_10_to_2(out_not, in_num):
    in_numb = int(in_num)
    out_ss = int(out_not)
    out_num = ''
    while in_numb > 0:
        out_num = str(in_numb % out_ss) + out_num
        in_numb //= out_ss
    return out_num


def from_2_to_8(in_not, out_not, in_num):
    get_10_not = int(in_num, int(in_not))
    return from_10_to_2(out_not, get_10_not)


def from_8_to_2(in_not, out_not, in_num):
    get_10_not = int(in_num, int(in_not))
    return from_10_to_2(out_not, get_10_not)


def from_8_to_16(in_not, out_not, in_num):
    out_ss = int(out_not)
    get_10_not = int(in_num, int(in_not))
    out_num = ''
    res = []

    status = True
    while status:
        if get_10_not < out_ss:
            res.append(out_num + ALPHABET[get_10_not])
            status = False
        else:
            res.append(ALPHABET[get_10_not % out_ss])
            get_10_not //= out_ss

    res.reverse()
    result = ''.join(res)

    return result


def from_16_to_8(in_not, out_not, in_num):
    out_ss = int(out_not)
    get_10_not = int(in_num, int(in_not))
    out_num = ''
    res = []

    status = True
    while status:
        if get_10_not < out_ss:
            res.append(out_num + ALPHABET[get_10_not])
            status = False
        else:
            res.append(ALPHABET[get_10_not % out_ss])
            get_10_not //= out_ss

    res.reverse()
    result = ''.join(res)

    return result
