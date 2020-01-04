import mathlib
import pytest
import sys

@pytest.mark.skip(reason="i dont want to run this test at the moment")
def test_calc_total():
	total = mathlib.calc_total(4,5)
	assert total == 9	# total should be 9

@pytest.mark.skipif(sys.version_info == (2.7), reason="python version greater than 3.5")
def test_calc_multiply():
	res = mathlib.calc_multiply(10,3)
	assert res == 30
	
def test_calc_substract():
	res = mathlib.calc_substract(10,3)
	assert res == 7
	
def test_calc_power():
	res = mathlib.calc_power(4,2)
	assert res == 16
	
def test_calc_power_of():
	res = mathlib.calc_power_of(5,3)
	assert res == 125

# here we can mark particular test in that category
# in window there are 2 test cases
@pytest.mark.window
def test_window_1():
	assert True

@pytest.mark.window
def test_window_2():
	assert True

@pytest.mark.mac
def test_mac_1():
	assert True
	
@pytest.mark.mac
def test_mac_2():
	assert True
	
"""
if we want to run mark test cases (window or mac) then use following command

$pytest -m window 	[ -v ]		# -v for verbose output in detail output
$pytest -m "not mac"			# ohter than mac all test cases will run

$pytest -m mac
$pytest -m "not window"			# other than windows all test cases will run
"""