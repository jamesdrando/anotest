# anotest
Simple annotated testing for Python using the @test decorator

## About
anotest serves one singular purpose: provide one simple uniform way to test your python code.

anotest includes two things:
1. The Anotest class - this keeps track of all your tests, prints the results, prints failures, stacktraces, etc. You need to declare it before all of your tests and set debug to True.
2. The test function - define your test functions using assertions. Place the @test decorator above these functions.

anotest **IS NOT** feature rich\
anotest **IS NOT** robust\
anotest **IS NOT** a fully complete testing and debugging module\

anotest **IS** nice and easy to use for the vast majority of simple applications and scripts.

Have fun


## How to use anotest
```

from anotest import *

# Initialize the test and set debug to True
Anotest.debug = True

@test
def test_something():
  assert True

@test
def test_something_else():
  assert 1 + 1 == 2

@test
def test_something_else_again():
  assert 2 + 2 == 5, "2 + 2 == 4"

@test
def test_something_else__yet_again():
  assert True == False

@test
def testola():
  assert 69 > 420

# Run test
Anotest.run_tests()

```
