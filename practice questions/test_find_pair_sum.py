"""
Given any list of integers to a method find_pairs_sum, we get all pairs (x, y) which add up to k
Eg: find_pairs_sum([-3, -1, 4, 5, 7, 8, 10], k=15) we get output like [(7, 8), (10,5)]
Write ONLY test cases (in pytest) for method find_pairs_sum
"""


import pytest

def find_pair_sum(input_data_list, sum_variable):
    """This function returns dictionary of tuple of sum_of_pair is k"""
    if not isinstance(input_data_list, list) or not isinstance(sum_variable, int):
        raise TypeError
    pair_sum_data = []
    list_len = len(input_data_list)
    for first_index in range(list_len):
        for sec_index in range(first_index+1, list_len):
            if (input_data_list[first_index] + input_data_list[sec_index]) == sum_variable:
                pair_sum_data.append((input_data_list[first_index], input_data_list[sec_index]))
    return pair_sum_data

def test_valid_find_pair_sum():
    # case 1
    valid_data_list = [-3, -1, 4, 5, 7, 8, 10]
    sum = 15
    assert len(find_pair_sum(valid_data_list, sum)), f"Pair_of_sum not available {valid_data_list}"

def test_invalid_find_pair_sum():
    # Case 2
    valid_data_list = [-3, -1, 4, 5, 7, 8, 10]
    sum = 111
    # function retuns empty list, which means it doesn't have pair available
    assert not len(find_pair_sum(valid_data_list, sum)), f"Pair_of_sum not available {valid_data_list}"

#if __name__=="__main__":
#   list1 = [-3, -1, 4, 5, 7, 8, 10]
#   k = 15
#   find_pair_sun(list1, k)

"""
 [localhost@workspace]$ pytest test.py -vs
============================================================================ test session starts ============================================================================

test.py::test_valid_find_pair_sum PASSED
test.py::test_invalid_find_pair_sum PASSED

============================================================================= 2 passed in 0.01s =============================================================================
"""
