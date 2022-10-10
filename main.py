def fill_list_from_string(string: str) -> []:
    new_list = []
    i = 0
    while i < len(string):
        new_list.append(int(string[i]))
        i += 1
    return new_list


def sum_arrays(first_list: [], first_size: int, second_list: [], second_size: int):
    sum_array_size = first_size if first_size > second_size else second_size
    array_sum = []
    for i in range(sum_array_size):
        array_sum.append(0)
    carry = 0
    length_counter = 0
    i = first_size - 1
    j = second_size - 1
    k = sum_array_size - 1

    while i >= 0 and j >= 0:
        temp = first_list[i] + second_list[j] + carry
        carry = 0
        k = max(i, j)
        array_sum[k] = temp % 10
        k -= 1
        length_counter += 1

        if temp > 9:
            carry = 1

        i -= 1
        j -= 1

    while i >= 0:
        array_sum[k] = first_list[i] + carry
        k -= 1
        carry = 0
        length_counter += 1
        i -= 1

    while j >= 0:
        array_sum[k] = second_list[j] + carry
        k -= 1
        carry = 0
        length_counter += 1
        j -= 1

    print("The Sum of your two numbers is: ")
    number = ''.join(str(x) for x in array_sum)
    print(number)


if __name__ == '__main__':
    keep_going: bool = True

    while keep_going:
        entered_number = input("Enter a number: ")
        first_size = len(entered_number)
        first_list = fill_list_from_string(entered_number)

        entered_number = input("Enter a second number: ")
        second_size = len(entered_number)
        second_list = fill_list_from_string(entered_number)

        sum_arrays(first_list, first_size, second_list, second_size)
        break
