import unittest
from io import StringIO
import sys
import time


class ExtendedTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.test_timings = []

    def startTest(self, test):
        self._start_time = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        elapsed = time.time() - self._start_time
        self.test_timings.append((test.id(), 'OK', elapsed))
        if self.showAll:
            self.stream.write("ok\n")
        elif self.dots:
            self.stream.write('.')
        super().addSuccess(test)

    def addError(self, test, err):
        elapsed = time.time() - self._start_time
        self.test_timings.append((test.id(), 'ERROR', elapsed))
        self.stream.write('ERROR\n')
        self.stream.write(self._exc_info_to_string(err, test))
        self.stream.write('\n')
        super().addError(test, err)

    def addFailure(self, test, err):
        elapsed = time.time() - self._start_time
        self.test_timings.append((test.id(), 'FAIL', elapsed))
        self.stream.write('FAIL\n')
        self.stream.write(self._exc_info_to_string(err, test))
        self.stream.write('\n')
        super().addFailure(test, err)


def run_tests():
    suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2, resultclass=ExtendedTestResult)
    result = runner.run(suite)
    print("\n\nTest Report Summary:")
    print(f"{'Test Name':<85} {'Result':<10} {'Time (s)':>10}")
    for name, outcome, timing in result.test_timings:
        print(f"{name:<85} {outcome:<10} {timing:10.4f}")

    print("\n\nTest Output:")
    print(stream.getvalue())

    print("\n\nSummary:")
    print(f"Total Tests: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.testsRun - len(result.failures) - len(result.errors)}")


if __name__ == "__main__":
    run_tests()
