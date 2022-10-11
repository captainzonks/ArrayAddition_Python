def fill_list_from_string(string: str) -> []:
    """
    Takes an integer string and separates out all characters into a single list
    :param string
    :return: list
    """
    new_list = []
    i = 0
    while i < len(string):
        new_list.append(int(string[i]))
        i += 1
    return new_list


def sum_arrays(first_list: [], first_size: int, second_list: [], second_size: int):
    """
    Takes two provided lists of integers which represent single numbers divided into their decimal parts
    and sums them together in the style of pencil-paper, i.e. stacking the two and summing them vertically and
    handling carries.
    :param first_list:
    :param first_size:
    :param second_list:
    :param second_size:
    :return:
    """
    # Find the size of the final array based upon which list is larger
    sum_list_size = first_size if first_size > second_size else second_size
    list_sum = []
    # Create a placeholder list of zeros
    for i in range(sum_list_size):
        list_sum.append(0)
    # Initialize carry and indices
    carry = 0
    i = first_size - 1
    j = second_size - 1
    k = sum_list_size - 1

    while i >= 0 and j >= 0:
        # Add the indexed numbers together, and include a carry value if there is one
        temp = first_list[i] + second_list[j] + carry
        # Reset the carry
        carry = 0
        # Set k to the larger value; i or j
        k = max(i, j)
        # Set the value at index k to the remainder of temp divided by ten
        # i.e. if list_sum is 0000, and k is 3, and temp is 11, the remainder is 1 and the value becomes 0001
        # and the carry flag gets ticked
        list_sum[k] = temp % 10
        # Subtract 1 from k (this will be used if the while loop finishes and k isn't set to a new max)
        k -= 1

        # Tick the carry flag if temp is greater than 9 (as explained above)
        if temp > 9:
            carry = 1

        # Decrement indices
        i -= 1
        j -= 1

    # Only one of these while loops will run, if at all,
    # because one index may be larger than the other and won't
    # have hit 0 yet

    # The carry may have continued over from the previous loop, so add it to the
    # list's value then set it to zero, then fill out the rest of the list with the original values
    # of the number (because we've completed the addition, and we're just bringing
    # down values now)

    while i >= 0:
        list_sum[k] = first_list[i] + carry
        k -= 1
        carry = 0
        i -= 1

    while j >= 0:
        list_sum[k] = second_list[j] + carry
        k -= 1
        carry = 0
        j -= 1

    print("The Sum of your two numbers is: ")
    number = ''.join(str(x) for x in list_sum)
    print(number)


if __name__ == '__main__':
    # keep_going is currently a placeholder to allow the while loop below to be run as many
    # times as the user would like; this has not been implemented however
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
