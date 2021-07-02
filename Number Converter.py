# ask user to select menu
select_menu = eval(input("1. Binary to Decimal\n2. Decimal to Binary\n3. Octal to Decimal\n4. Decimal to Octal\n\
5. Octal to Binary\n6. Binary to Octal\n7. Decimal to Hexadecimal\n8. Hexadecimal to Decimal\n\
9. Hexadecimal to Binary\n10. Binary to Hexadecimal\nPlease select a menu: "))


# binary to decimal
if select_menu == 1:
    print("1. Binary to Decimal")
    # Binary to decimal
    # ask user to input
    binary_number = input("Enter a binary number: ")
    binary_number_num = eval(binary_number)
    len_binary = len(binary_number)

    # integer part
    binary_int = int(binary_number_num)
    int_len = len(str(binary_int))
    binary_int_str = str(binary_int)

    # fractional part
    binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
    fra_len = len(str(binary_fra))
    fra_len_to_sub = fra_len
    binary_fra_str = str(binary_fra)

    # result
    result_fra = 0
    result_int = 0

    # for positive
    if binary_number_num >= 0:

        # integer loop
        for int_num in binary_int_str:
            result_int += eval(int_num) * pow(2, int_len - 1)
            int_len -= 1

        # fractional loop
        for fra_num in binary_fra_str:
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

        print("Number in decimal is", result_int + result_fra)

    # for negative
    else:

        # integer loop
        for int_num in binary_int_str:
            if int_num == "-":
                continue
            result_int += eval(int_num) * pow(2, int_len - 2)
            int_len -= 1

        # fractional loop
        for fra_num in binary_fra_str:
            if fra_num == "-":
                continue
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

        print("Number in decimal is", - (result_int + result_fra))

# decimal to binary
elif select_menu == 2:
    print("2. Decimal to Binary")

    # Decimal to binary
    # ask user to enter decimal number
    decimal_number = input("Enter a decimal number: ")
    decimal_number_num = eval(decimal_number)
    len_decimal = len(decimal_number)

    # integer part
    decimal_int = int(decimal_number_num)
    int_len = len(str(decimal_int))

    # fractional part
    decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
    fra_len = len(str(decimal_fra))
    decimal_fra_num_to_loop = 0

    # result
    result_fra = "0."
    result_int = ""

    # for positive
    if decimal_number_num >= 0:
        if decimal_int > 0:

            # integer loop
            while decimal_int >= 1:
                result_int += str(decimal_int % 2)
                decimal_int = decimal_int // 2

            # fractional loop
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 2
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1
            print("Number in binary is", eval(result_int[::-1]) + eval(result_fra))

        # if 0 < x < 1
        elif decimal_int == 0:
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 2
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1
            print("Number in binary is", result_fra)

# octal to decimal
elif select_menu == 3:
    print("3. Octal to Decimal")
    # Octal to decimal
    # ask user to input
    octal_number = input("Enter a octal number: ")
    octal_number_num = eval(octal_number)
    len_octal = len(octal_number)

    # integer part
    octal_int = int(octal_number_num)
    int_len = len(str(octal_int))
    octal_int_str = str(octal_int)

    # fractional part
    octal_fra = round(octal_number_num - octal_int, len_octal - int_len - 1)
    fra_len = len(str(octal_fra))
    fra_len_to_sub = fra_len
    octal_fra_str = str(octal_fra)

    # result
    result_fra = 0
    result_int = 0

    # for positive
    if octal_number_num >= 0:
        # integer loop
        for int_num in octal_int_str:
            result_int += eval(int_num) * pow(8, int_len - 1)
            int_len -= 1

        # fractional loop
        for fra_num in octal_fra_str:
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(8, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

        print("Number in decimal is", result_int + result_fra)

    # for negative
    else:
        # integer loop
        for int_num in octal_int_str:
            if int_num == "-":
                continue
            result_int += eval(int_num) * pow(8, int_len - 2)
            int_len -= 1

        # fractional loop
        for fra_num in octal_fra_str:
            if fra_num == "-":
                continue
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(8, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

        print("Number in decimal is", - (result_int + result_fra))

# decimal to octal
elif select_menu == 4:
    print("4. Decimal to Octal")
    # Decimal to octal
    # ask user to enter decimal number
    decimal_number = input("Enter a decimal number: ")
    decimal_number_num = eval(decimal_number)
    len_decimal = len(decimal_number)

    # integer part
    decimal_int = int(decimal_number_num)
    int_len = len(str(decimal_int))

    # fractional part
    decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
    fra_len = len(str(decimal_fra))
    fra_len_to_sub = fra_len
    decimal_fra_num_to_loop = 0

    # result
    result_fra = "0."
    result_int = ""

    if decimal_number_num >= 0:
        if decimal_int > 0:

            # integer loop
            while decimal_int >= 1:
                result_int += str(decimal_int % 8)
                decimal_int = decimal_int // 8

            # fractional loop
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 8
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1

            print("Number in octal is", eval(result_int[::-1]) + eval(result_fra))
        # in range (0,1)
        elif decimal_int == 0:
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 8
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1
            print("Number in octal is", result_fra)

# octal to binary
elif select_menu == 5:
    print("5. Octal to Binary")
    # octal to binary
    # ask user to input

    oct_to_bin = (input("Enter a octal number: "))
    oct_to_bin_int = int(eval(oct_to_bin))
    length_full_oct = len(oct_to_bin)
    oct_to_bin_fra = round(eval(oct_to_bin) - oct_to_bin_int, length_full_oct - len(str(oct_to_bin_int)) - 1)
    oct_to_bin_fra_rep = str(oct_to_bin_fra).replace("0.", ".")
    result_int = ""
    result_fra = ""

    for i in str(oct_to_bin_int):

        if i == "0":
            i = "000"
        if i == "1":
            i = "001"
        if i == "2":
            i = "010"
        if i == "3":
            i = "011"
        if i == "4":
            i = "100"
        if i == "5":
            i = "101"
        if i == "6":
            i = "110"
        if i == "7":
            i = "111"
        result_int += i

    # fractional part
    for i in str(oct_to_bin_fra_rep):
        if i == ".":
            continue
        if i == "0":
            i = "000"
        if i == "1":
            i = "001"
        if i == "2":
            i = "010"
        if i == "3":
            i = "011"
        if i == "4":
            i = "100"
        if i == "5":
            i = "101"
        if i == "6":
            i = "110"
        if i == "7":
            i = "111"
        result_fra += i

    # result
    print("Number in binary is:", str(int(result_int)) + "." + result_fra)

# binary to octal
elif select_menu == 6:
    print("6. Binary to Octal")
    # Binary to decimal
    # ask user to input
    binary_number = input("Enter a binary number: ")
    binary_number_num = eval(binary_number)
    len_binary = len(binary_number)

    # integer part
    binary_int = int(binary_number_num)
    int_len = len(str(binary_int))
    binary_int_str = str(binary_int)

    # fractional part
    binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
    fra_len = len(str(binary_fra))
    fra_len_to_sub = fra_len
    binary_fra_str = str(binary_fra)

    # result
    result_fra = 0
    result_int = 0

    # for positive
    if binary_number_num >= 0:

        # integer loop
        for int_num in binary_int_str:
            result_int += eval(int_num) * pow(2, int_len - 1)
            int_len -= 1

        # fractional loop
        for fra_num in binary_fra_str:
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

    # convert from decimal to octal
    decimal_number = str(result_fra + result_int)
    decimal_number_num = eval(decimal_number)
    len_decimal = len(decimal_number)

    # integer part
    decimal_int = int(decimal_number_num)
    int_len = len(str(decimal_int))

    # fractional part
    decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
    fra_len = len(str(decimal_fra))
    fra_len_to_sub = fra_len
    decimal_fra_num_to_loop = 0

    # result
    result_fra = "0."
    result_int = ""

    if decimal_number_num >= 0:
        if decimal_int > 0:

            # integer loop
            while decimal_int >= 1:
                result_int += str(decimal_int % 8)
                decimal_int = decimal_int // 8

                # fractional loop
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 8
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1

            print("Number in octal is", eval(result_int[::-1]) + eval(result_fra))
        # in range (0,1)
        elif decimal_int == 0:
            while decimal_fra_num_to_loop < 10:
                if str(decimal_fra) == ".":
                    continue
                decimal_fra = decimal_fra * 8
                result_fra += str(int(decimal_fra))
                decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                decimal_fra_num_to_loop += 1
            print("Number in octal is", result_fra)

# decimal to hex
elif select_menu == 7:
    print("7. Decimal to Hexadecimal")

    # ask user to choose type
    select_type = eval(input("Type:\n1 For integer number\n2 For float number in range (0,1)\
    \nPlease select a type: "))

    # integer number
    if select_type == 1:
        decimal_num = input("Enter a integer decimal number: ")
        decimal_int = eval(decimal_num)
        result_int = ""

        # integer loop
        while decimal_int >= 1:
            remainder = decimal_int % 16
            if remainder == 10:
                remainder = "A"
            if remainder == 11:
                remainder = "B"
            if remainder == 12:
                remainder = "C"
            if remainder == 13:
                remainder = "D"
            if remainder == 14:
                remainder = "E"
            if remainder == 15:
                remainder = "F"
            result_int += str(remainder)
            decimal_int = decimal_int // 16
        print("Number in hexadecimal is", result_int[::-1])

    # range(0,1)
    if select_type == 2:

        # fractional loop
        decimal_num_str = input("Enter a float decimal number in range (0,1): ")
        decimal_num = eval(decimal_num_str)
        loop_num = 0
        int_int = ""
        result = "0."
        decimal_fra_num_to_loop = 0

        while decimal_fra_num_to_loop < 10:
            if str(decimal_num) == ".":
                continue
            decimal_num = decimal_num * 16
            if decimal_num < 10:
                int_int = int(decimal_num)
            if 10 <= decimal_num < 11:
                int_int = "A"
            if 11 <= decimal_num < 12:
                int_int = "B"
            if 12 <= decimal_num < 13:
                int_int = "C"
            if 13 <= decimal_num < 14:
                int_int = "D"
            if 14 <= decimal_num < 15:
                int_int = "E"
            if 15 <= decimal_num < 16:
                int_int = "F"

            result += str(int_int)
            decimal_num = round(decimal_num - int(decimal_num), len(decimal_num_str) - 2)
            decimal_fra_num_to_loop += 1
        print("Number in hexadecimal is", result)

# hex to decimal
elif select_menu == 8:
    print("8. Hexadecimal to Decimal")

    # ask user to input
    hex_number = input("Enter a hexadecimal number: ")
    int_hex_num = ""
    for i in hex_number:
        int_hex_num += i
        if i == ".":
            break
    int_hex_num_strip = int_hex_num.strip(".")
    int_len = len(int_hex_num_strip)
    result_int = 0
    fra_hex_num = hex_number.replace(int_hex_num, "0.")
    fra_hex_len = len(fra_hex_num)
    fra_len_to_sub = fra_hex_len
    result_fra = 0

    # integer loop
    for int_num in int_hex_num_strip:
        A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
        result_int += eval(int_num) * pow(16, int_len - 1)
        int_len -= 1

    # fractional loop
    for fra_num in fra_hex_num:
        A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
        if fra_num == ".":
            continue
        result_fra += eval(fra_num) * pow(16, fra_len_to_sub - fra_hex_len)
        fra_len_to_sub -= 1
    # result both
    print("Number in decimal is", result_int + result_fra)

# hex to bin
elif select_menu == 9:
    print("9. Hexadecimal to Binary")

    # hex to binary
    # ask user to input
    hex_to_bin = (input("Enter a hexadecimal number: "))
    result = ""

    # loop
    for i in str(hex_to_bin):
        if i == ".":
            i = "."
        if i == "0":
            i = "0000"
        if i == "1":
            i = "0001"
        if i == "2":
            i = "0010"
        if i == "3":
            i = "0011"
        if i == "4":
            i = "0100"
        if i == "5":
            i = "0101"
        if i == "6":
            i = "0110"
        if i == "7":
            i = "0111"
        if i == "8":
            i = "1000"
        if i == "9":
            i = "1001"
        if i == "A":
            i = "1010"
        if i == "B":
            i = "1011"
        if i == "C":
            i = "1100"
        if i == "D":
            i = "1101"
        if i == "E":
            i = "1110"
        if i == "F":
            i = "1111"

        result += i
    # display result
    print("Number in binary is: ", result)

# binary to hex (integer only)
if select_menu == 10:
    print("10. Binary to Hexadecimal")

    # Binary to decimal
    # ask user to input
    binary_number = input("Enter a integer binary number: ")
    binary_number_num = eval(binary_number)
    len_binary = len(binary_number)

    # integer part
    binary_int = int(binary_number_num)
    int_len = len(str(binary_int))
    binary_int_str = str(binary_int)

    # fractional part
    binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
    fra_len = len(str(binary_fra))
    fra_len_to_sub = fra_len
    binary_fra_str = str(binary_fra)

    # result
    result_fra = 0
    result_int = 0

    # for positive
    if binary_number_num >= 0:
        # integer loop
        for int_num in binary_int_str:
            result_int += eval(int_num) * pow(2, int_len - 1)
            int_len -= 1

        # fractional loop
        for fra_num in binary_fra_str:
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
            fra_len_to_sub -= 1

        # decimal to hexadecimal
        decimal_num = str(result_int + result_fra)
        decimal_int = eval(decimal_num)
        result_int = ""

        # integer loop
        while decimal_int >= 1:
            remainder = decimal_int % 16
            if remainder == 10:
                remainder = "A"
            if remainder == 11:
                remainder = "B"
            if remainder == 12:
                remainder = "C"
            if remainder == 13:
                remainder = "D"
            if remainder == 14:
                remainder = "E"
            if remainder == 15:
                remainder = "F"
            result_int += str(remainder)
            decimal_int = decimal_int // 16
        print("Number in hexadecimal is", result_int[::-1])
again = input("Enter yes for again: ")
while again == "yes":
    # ask user to select menu
    select_menu = eval(input("1. Binary to Decimal\n2. Decimal to Binary\n3. Octal to Decimal\n4. Decimal to Octal\n\
5. Octal to Binary\n6. Binary to Octal\n7. Decimal to Hexadecimal\n8. Hexadecimal to Decimal\n\
9. Hexadecimal to Binary\n10. Binary to Hexadecimal\nPlease select a menu: "))

    # binary to decimal
    if select_menu == 1:
        print("1. Binary to Decimal")
        # Binary to decimal
        # ask user to input
        binary_number = input("Enter a binary number: ")
        binary_number_num = eval(binary_number)
        len_binary = len(binary_number)

        # integer part
        binary_int = int(binary_number_num)
        int_len = len(str(binary_int))
        binary_int_str = str(binary_int)

        # fractional part
        binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
        fra_len = len(str(binary_fra))
        fra_len_to_sub = fra_len
        binary_fra_str = str(binary_fra)

        # result
        result_fra = 0
        result_int = 0

        # for positive
        if binary_number_num >= 0:

            # integer loop
            for int_num in binary_int_str:
                result_int += eval(int_num) * pow(2, int_len - 1)
                int_len -= 1

            # fractional loop
            for fra_num in binary_fra_str:
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

            print("Number in decimal is", result_int + result_fra)

        # for negative
        else:

            # integer loop
            for int_num in binary_int_str:
                if int_num == "-":
                    continue
                result_int += eval(int_num) * pow(2, int_len - 2)
                int_len -= 1

            # fractional loop
            for fra_num in binary_fra_str:
                if fra_num == "-":
                    continue
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

            print("Number in decimal is", - (result_int + result_fra))

    # decimal to binary
    elif select_menu == 2:
        print("2. Decimal to Binary")

        # Decimal to binary
        # ask user to enter decimal number
        decimal_number = input("Enter a decimal number: ")
        decimal_number_num = eval(decimal_number)
        len_decimal = len(decimal_number)

        # integer part
        decimal_int = int(decimal_number_num)
        int_len = len(str(decimal_int))

        # fractional part
        decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
        fra_len = len(str(decimal_fra))
        decimal_fra_num_to_loop = 0

        # result
        result_fra = "0."
        result_int = ""

        # for positive
        if decimal_number_num >= 0:
            if decimal_int > 0:

                # integer loop
                while decimal_int >= 1:
                    result_int += str(decimal_int % 2)
                    decimal_int = decimal_int // 2

                # fractional loop
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 2
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1
                print("Number in binary is", eval(result_int[::-1]) + eval(result_fra))

            # if 0 < x < 1
            elif decimal_int == 0:
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 2
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1
                print("Number in binary is", result_fra)

    # octal to decimal
    elif select_menu == 3:
        print("3. Octal to Decimal")
        # Octal to decimal
        # ask user to input
        octal_number = input("Enter a octal number: ")
        octal_number_num = eval(octal_number)
        len_octal = len(octal_number)

        # integer part
        octal_int = int(octal_number_num)
        int_len = len(str(octal_int))
        octal_int_str = str(octal_int)

        # fractional part
        octal_fra = round(octal_number_num - octal_int, len_octal - int_len - 1)
        fra_len = len(str(octal_fra))
        fra_len_to_sub = fra_len
        octal_fra_str = str(octal_fra)

        # result
        result_fra = 0
        result_int = 0

        # for positive
        if octal_number_num >= 0:
            # integer loop
            for int_num in octal_int_str:
                result_int += eval(int_num) * pow(8, int_len - 1)
                int_len -= 1

            # fractional loop
            for fra_num in octal_fra_str:
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(8, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

            print("Number in decimal is", result_int + result_fra)

        # for negative
        else:
            # integer loop
            for int_num in octal_int_str:
                if int_num == "-":
                    continue
                result_int += eval(int_num) * pow(8, int_len - 2)
                int_len -= 1

            # fractional loop
            for fra_num in octal_fra_str:
                if fra_num == "-":
                    continue
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(8, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

            print("Number in decimal is", - (result_int + result_fra))

    # decimal to octal
    elif select_menu == 4:
        print("4. Decimal to Octal")
        # Decimal to octal
        # ask user to enter decimal number
        decimal_number = input("Enter a decimal number: ")
        decimal_number_num = eval(decimal_number)
        len_decimal = len(decimal_number)

        # integer part
        decimal_int = int(decimal_number_num)
        int_len = len(str(decimal_int))

        # fractional part
        decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
        fra_len = len(str(decimal_fra))
        fra_len_to_sub = fra_len
        decimal_fra_num_to_loop = 0

        # result
        result_fra = "0."
        result_int = ""

        if decimal_number_num >= 0:
            if decimal_int > 0:

                # integer loop
                while decimal_int >= 1:
                    result_int += str(decimal_int % 8)
                    decimal_int = decimal_int // 8

                # fractional loop
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 8
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1

                print("Number in octal is", eval(result_int[::-1]) + eval(result_fra))
            # in range (0,1)
            elif decimal_int == 0:
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 8
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1
                print("Number in octal is", result_fra)

    # octal to binary
    elif select_menu == 5:
        print("5. Octal to Binary")
        # octal to binary
        # ask user to input

        oct_to_bin = (input("Enter a octal number: "))
        oct_to_bin_int = int(eval(oct_to_bin))
        length_full_oct = len(oct_to_bin)
        oct_to_bin_fra = round(eval(oct_to_bin) - oct_to_bin_int, length_full_oct - len(str(oct_to_bin_int)) - 1)
        oct_to_bin_fra_rep = str(oct_to_bin_fra).replace("0.", ".")
        result_int = ""
        result_fra = ""

        for i in str(oct_to_bin_int):

            if i == "0":
                i = "000"
            if i == "1":
                i = "001"
            if i == "2":
                i = "010"
            if i == "3":
                i = "011"
            if i == "4":
                i = "100"
            if i == "5":
                i = "101"
            if i == "6":
                i = "110"
            if i == "7":
                i = "111"
            result_int += i

        # fractional part
        for i in str(oct_to_bin_fra_rep):
            if i == ".":
                continue
            if i == "0":
                i = "000"
            if i == "1":
                i = "001"
            if i == "2":
                i = "010"
            if i == "3":
                i = "011"
            if i == "4":
                i = "100"
            if i == "5":
                i = "101"
            if i == "6":
                i = "110"
            if i == "7":
                i = "111"
            result_fra += i

        # result
        print("Number in binary is:", str(int(result_int)) + "." + result_fra)

    # binary to octal
    elif select_menu == 6:
        print("6. Binary to Octal")
        # Binary to decimal
        # ask user to input
        binary_number = input("Enter a binary number: ")
        binary_number_num = eval(binary_number)
        len_binary = len(binary_number)

        # integer part
        binary_int = int(binary_number_num)
        int_len = len(str(binary_int))
        binary_int_str = str(binary_int)

        # fractional part
        binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
        fra_len = len(str(binary_fra))
        fra_len_to_sub = fra_len
        binary_fra_str = str(binary_fra)

        # result
        result_fra = 0
        result_int = 0

        # for positive
        if binary_number_num >= 0:

            # integer loop
            for int_num in binary_int_str:
                result_int += eval(int_num) * pow(2, int_len - 1)
                int_len -= 1

            # fractional loop
            for fra_num in binary_fra_str:
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

        # convert from decimal to octal
        decimal_number = str(result_fra + result_int)
        decimal_number_num = eval(decimal_number)
        len_decimal = len(decimal_number)

        # integer part
        decimal_int = int(decimal_number_num)
        int_len = len(str(decimal_int))

        # fractional part
        decimal_fra = round(decimal_number_num - decimal_int, len_decimal - int_len - 1)
        fra_len = len(str(decimal_fra))
        fra_len_to_sub = fra_len
        decimal_fra_num_to_loop = 0

        # result
        result_fra = "0."
        result_int = ""

        if decimal_number_num >= 0:
            if decimal_int > 0:

                # integer loop
                while decimal_int >= 1:
                    result_int += str(decimal_int % 8)
                    decimal_int = decimal_int // 8

                    # fractional loop
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 8
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1

                print("Number in octal is", eval(result_int[::-1]) + eval(result_fra))
            # in range (0,1)
            elif decimal_int == 0:
                while decimal_fra_num_to_loop < 10:
                    if str(decimal_fra) == ".":
                        continue
                    decimal_fra = decimal_fra * 8
                    result_fra += str(int(decimal_fra))
                    decimal_fra = round(decimal_fra - int(decimal_fra), fra_len - 2)
                    decimal_fra_num_to_loop += 1
                print("Number in octal is", result_fra)

    # decimal to hex
    elif select_menu == 7:
        print("7. Decimal to Hexadecimal")

        # ask user to choose type
        select_type = eval(input("Type:\n1 For integer number\n2 For float number in range (0,1)\
        \nPlease select a type: "))

        # integer number
        if select_type == 1:
            decimal_num = input("Enter a integer decimal number: ")
            decimal_int = eval(decimal_num)
            result_int = ""

            # integer loop
            while decimal_int >= 1:
                remainder = decimal_int % 16
                if remainder == 10:
                    remainder = "A"
                if remainder == 11:
                    remainder = "B"
                if remainder == 12:
                    remainder = "C"
                if remainder == 13:
                    remainder = "D"
                if remainder == 14:
                    remainder = "E"
                if remainder == 15:
                    remainder = "F"
                result_int += str(remainder)
                decimal_int = decimal_int // 16
            print("Number in hexadecimal is", result_int[::-1])

        # range(0,1)
        if select_type == 2:

            # fractional loop
            decimal_num_str = input("Enter a float decimal number in range (0,1): ")
            decimal_num = eval(decimal_num_str)
            loop_num = 0
            int_int = ""
            result = "0."
            decimal_fra_num_to_loop = 0

            while decimal_fra_num_to_loop < 10:
                if str(decimal_num) == ".":
                    continue
                decimal_num = decimal_num * 16
                if decimal_num < 10:
                    int_int = int(decimal_num)
                if 10 <= decimal_num < 11:
                    int_int = "A"
                if 11 <= decimal_num < 12:
                    int_int = "B"
                if 12 <= decimal_num < 13:
                    int_int = "C"
                if 13 <= decimal_num < 14:
                    int_int = "D"
                if 14 <= decimal_num < 15:
                    int_int = "E"
                if 15 <= decimal_num < 16:
                    int_int = "F"

                result += str(int_int)
                decimal_num = round(decimal_num - int(decimal_num), len(decimal_num_str) - 2)
                decimal_fra_num_to_loop += 1
            print("Number in hexadecimal is", result)

    # hex to decimal
    elif select_menu == 8:
        print("8. Hexadecimal to Decimal")

        # ask user to input
        hex_number = input("Enter a hexadecimal number: ")
        int_hex_num = ""
        for i in hex_number:
            int_hex_num += i
            if i == ".":
                break
        int_hex_num_strip = int_hex_num.strip(".")
        int_len = len(int_hex_num_strip)
        result_int = 0
        fra_hex_num = hex_number.replace(int_hex_num, "0.")
        fra_hex_len = len(fra_hex_num)
        fra_len_to_sub = fra_hex_len
        result_fra = 0

        # integer loop
        for int_num in int_hex_num_strip:
            A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
            result_int += eval(int_num) * pow(16, int_len - 1)
            int_len -= 1

        # fractional loop
        for fra_num in fra_hex_num:
            A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
            if fra_num == ".":
                continue
            result_fra += eval(fra_num) * pow(16, fra_len_to_sub - fra_hex_len)
            fra_len_to_sub -= 1
        # result both
        print("Number in decimal is", result_int + result_fra)

    # hex to bin
    elif select_menu == 9:
        print("9. Hexadecimal to Binary")

        # hex to binary
        # ask user to input
        hex_to_bin = (input("Enter a hexadecimal number: "))
        result = ""

        # loop
        for i in str(hex_to_bin):
            if i == ".":
                i = "."
            if i == "0":
                i = "0000"
            if i == "1":
                i = "0001"
            if i == "2":
                i = "0010"
            if i == "3":
                i = "0011"
            if i == "4":
                i = "0100"
            if i == "5":
                i = "0101"
            if i == "6":
                i = "0110"
            if i == "7":
                i = "0111"
            if i == "8":
                i = "1000"
            if i == "9":
                i = "1001"
            if i == "A":
                i = "1010"
            if i == "B":
                i = "1011"
            if i == "C":
                i = "1100"
            if i == "D":
                i = "1101"
            if i == "E":
                i = "1110"
            if i == "F":
                i = "1111"

            result += i
        # display result
        print("Number in binary is: ", result)

    # binary to hex (integer only)
    if select_menu == 10:
        print("10. Binary to Hexadecimal")

        # Binary to decimal
        # ask user to input
        binary_number = input("Enter a integer binary number: ")
        binary_number_num = eval(binary_number)
        len_binary = len(binary_number)

        # integer part
        binary_int = int(binary_number_num)
        int_len = len(str(binary_int))
        binary_int_str = str(binary_int)

        # fractional part
        binary_fra = round(binary_number_num - binary_int, len_binary - int_len - 1)
        fra_len = len(str(binary_fra))
        fra_len_to_sub = fra_len
        binary_fra_str = str(binary_fra)

        # result
        result_fra = 0
        result_int = 0

        # for positive
        if binary_number_num >= 0:
            # integer loop
            for int_num in binary_int_str:
                result_int += eval(int_num) * pow(2, int_len - 1)
                int_len -= 1

            # fractional loop
            for fra_num in binary_fra_str:
                if fra_num == ".":
                    continue
                result_fra += eval(fra_num) * pow(2, fra_len_to_sub - fra_len)
                fra_len_to_sub -= 1

            # decimal to hexadecimal
            decimal_num = str(result_int + result_fra)
            decimal_int = eval(decimal_num)
            result_int = ""

            # integer loop
            while decimal_int >= 1:
                remainder = decimal_int % 16
                if remainder == 10:
                    remainder = "A"
                if remainder == 11:
                    remainder = "B"
                if remainder == 12:
                    remainder = "C"
                if remainder == 13:
                    remainder = "D"
                if remainder == 14:
                    remainder = "E"
                if remainder == 15:
                    remainder = "F"
                result_int += str(remainder)
                decimal_int = decimal_int // 16
            print("Number in hexadecimal is", result_int[::-1])
    again = input("Enter yes for again: ")
print("Bye!!!")