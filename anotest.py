import functools
import traceback

class Anotest:
  debug = False
  test_count = 0
  passed_count = 0
  _tests = []  # Store all the test functions
  failures = []

  @classmethod
  def run_all_tests(cls):
    if not cls.debug:
      return
    print(f"Running {len(cls._tests)} tests...")
    cls.test_count = len(cls._tests)
    cls.passed_count = 0
    cur = 1
    
    for test_func in cls._tests:
      try:
        test_func()  # Run each test
        cls.passed(test_func.__name__, cur)
      except AssertionError as e:
        cls.failed(test_func.__name__, cur, str(e))
        error_info = {
            "cur": cur,
            "test_name": test_func.__name__,
            "error": str(e),
            "stack_trace": traceback.format_exc(),
            }
        cls.failures.append(error_info)
      except Exception as e:
        cls.error(test_func.__name__, cur, str(e))
        error_info = {
            "cur": cur,
            "test_name": test_func.__name__,
            "error": str(e),
            "stack_trace": traceback.format_exc(),
            }
        cls.failures.append(error_info)
      cur += 1

    cls.print_summary()
    cls._print_failures()
    cls.reset()

  @classmethod
  def passed(cls, test_name, cur):
    cls.passed_count += 1
    if cls.debug:
      print(f"[{cur}][\u2713] '{test_name}' ... PASSED")

  @classmethod
  def failed(cls, test_name, cur, message):
    if cls.debug:
      if message:
        print(f"[{cur}][\u2715] '{test_name}' ... FAILED: {message}")
      else:
        print(f"[{cur}][\u2715] '{test_name}' ... FAILED")

  @classmethod
  def error(cls, test_name, cur, message):
    if cls.debug:
      if message:
        print(f"[{cur}][\u2715] '{test_name}' ... FAILED: {message}")
      else:
        print(f"[{cur}][\u2715] '{test_name}' ... FAILED")

  @classmethod
  def print_summary(cls):
    if cls.debug:
        print(f"Test cycle complete... {cls.passed_count}/{cls.test_count} tests passed")

  @classmethod
  def reset(cls):
    cls.test_count = 0
    cls.passed_count = 0
    cls._tests = []
    cls.failures = []

  @classmethod
  def _print_failures(cls):
    if cls.failures:
      print("\nFAILURES =================================================")
      for failure in cls.failures:
        print(f"\nTEST [{failure['cur']}] : {failure['test_name']}")
        if failure['error']:
          print(f"\nError Message: {failure['error']}")
        print(f"\n{failure['stack_trace']}")


def test(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    if Anotest.debug:
      return func(*args, **kwargs)
    else:
      return None
  Anotest._tests.append(wrapper)
  return wrapper