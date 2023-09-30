#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION



def calculate_sum(start, end):
#Start with a number, then use a for loop to add each consecutive number to the starting number, up to a specified ending number. Return the total sum of numbers in your specified range
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.

    # TODO: Return the calculated sum.

    total_sum = 0

    for num in range(start, end + 1):
        total_sum += num

    return total_sum

print('Function 1:')

# calculate_sum(start=1, end=5)

print('Function 2:')

def find_smallest_number(start, end):
#Specify a range of numbers, then use the min function to determine the smallest number within the specified range. 
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.

    # TODO: Return the found smallest number.

    sm_num = range(start, end + 1)
    print(min(sm_num))

    return min(sm_num)


# find_smallest_number(start= 3, end= 9)


print('Function 3:')

def find_largest_number(start, end):
#Specify a range of numbers, then use the max function to determine the largest number within the specified range. 
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

    lg_num = range(start, end + 1)
    print(max(lg_num))

    return max(lg_num)



# find_largest_number(start= 10, end= 20)

print('Function 4:')

def count_even_numbers(start, end):
# Start with a number, then use a for loop to determine if each consecutive number is divisible by 2, up to a specified ending number. Return each number that is divisible by 2. 
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.

    # TODO: Return the count of even numbers.

    even_num = []

    for num_in_range in range(start, end + 1):
        if num_in_range % 2 == 0:
            even_num.append(num_in_range)
            

    
            

    
    return len(even_num)


# count_even_numbers(start=1, end=10)

print('Function 5:')

def count_odd_numbers(start, end):
# Start with a number, then use a for loop to determine if each consecutive number is not divisible by 2, up to a specified ending number. Return each number that is not divisible by 2. 
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.

    odd_num = []

    for num_in_range in range(start, end + 1):
        if num_in_range % 2 != 0:
            odd_num.append(num_in_range)

    
            

    
    return len(odd_num)


# count_odd_numbers(start=15, end=25)