"""
Problem name: PROBLEM-ID        # This name must be put in the openEDX problem.
Part of:      WEEK 0
Exercise:     <Put here a short task description>

This example asks for the following code:

def f(a, b):
    return a+b
"""
import random
import grading_tools as gt


def check(code):
    """
    Instructions:
        The file must be named check_{}.py where {} is the problem name
        which must match the one specified on openEDX.
        The check function must return a list of dictionaries. Each dictionary
        represents a test case and has one of the following forms:

        {'correct': (bool), 'function': (str),
         'result': (str), 'expected': (str)}
        {'correct': False, 'error': (str)}

        The first one is for usual test results and the second one if
        bigger errors occurred which prevented the start of the test.
        (E.g. SyntaxError, NameError)

    Arguments:
        code (module): imported module containing the students code.

    Valid output formats:
        - {'correct': False, 'error': (str)}
        - {'correct':(bool), 'function':(str),
           'result':(str), 'expected':(str)}
        - a list of multiple of those dictionaries, each representing one
          test case.

    Print to sys.stdout:
        you can get the programs output with
        `sys.stdout.getvalue()` and `sys.stderr.getvalue()`
        It can be cleared with `sys.stdout.truncate(0)`
        (sys.stdout is just redirected to a `io.StringIO`)

        Also note that sys.stderr will usually be empty since a print to stderr
        is usually combined with an exception, which will cause the
        context manager in `testrunner.py` to exit and then print the
        error to the original stderr.
    """

    # Check that the student has defined the function
    try:
        fct = code.f
    except AttributeError:
        return {'correct': False, 'error': 'function ({}) is not defined. '
                                           'Check for correct '
                                           'naming.'.format('f')}

    # Define a correct solution
    def solution(x, y):
        """addition."""
        return x + y

    # Using 5 fixed and 15 random test values
    test_values = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -2)]
    while len(test_values) < 20:
        new = (random.randint(-1000, 1001), random.randint(-1000, 1001))
        if new not in test_values:
            test_values.append(new)

    # Compare code with solution
    return gt.function(fct=fct, values=test_values, solution=solution)
