from functions import \
    from_2_to_10, \
    from_10_to_2, \
    from_2_to_8, \
    from_8_to_2, \
    from_8_to_16, \
    from_16_to_8


class NumConverter:
    def __init__(self, in_ss, out_ss, in_number):
        self.in_not = in_ss
        self.out_not = out_ss
        self.in_num = in_number

    def __str__(self):
        print_num = ''
        if self.in_not == '2' and self.out_not == '10':
            print_num = from_2_to_10(
                self.in_not,
                self.in_num
            )
        elif self.in_not == '10' and self.out_not == '2':
            print_num = from_10_to_2(
                self.out_not,
                self.in_num
            )
        elif self.in_not == '2' and self.out_not == '8':
            print_num = from_2_to_8(
                self.in_not,
                self.out_not,
                self.in_num
            )
        elif self.in_not == '8' and self.out_not == '2':
            print_num = from_8_to_2(
                self.in_not,
                self.out_not,
                self.in_num
            )
        elif self.in_not == '8' and self.out_not == '16':
            print_num = from_8_to_16(
                self.in_not,
                self.out_not,
                self.in_num
            )
        elif self.in_not == '16' and self.out_not == '8':
            print_num = from_16_to_8(
                self.in_not,
                self.out_not,
                self.in_num
            )
        return f'{print_num}'
