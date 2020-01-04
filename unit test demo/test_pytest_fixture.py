import pytest_fixture_demo as py
from pytest_fixture_demo import cls_arithmatic
import pytest

@pytest.fixture()
def setup():
	print("------ inside setup -------")
	i = 10
	yield i
	print("------ after yield -------")


def test_cal_add(setup):
	print setup
	assert py.cal_add(10, 20) == 30
	
def test_cal_mul(setup):
	assert py.cal_mul(1, 2) == 2
	
	
'''
unit test demo>python -m pytest test_pytest_fixture.py -v -s

Output -
test_pytest_fixture.py::test_cal_add ------ inside setup -------
10
PASSED------ after yield -------

test_pytest_fixture.py::test_cal_mul ------ inside setup -------
PASSED------ after yield -------

'''

class TestArithmatic(cls_arithmatic):
	
	@pytest.fixture
	def setup(self, val1):
		print("********** Inside setup ***********")
		self.val1 = val1
		self.val2 = 2
		return self
		
		
	def test_function(self, setup):
		assert self.add(self.val1, self.val2) == 7
		#assert self.sub(self.val1, self.val2) == 3
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	