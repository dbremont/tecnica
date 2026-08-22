> …
> 

## List of Features

> Here's a table summarizing some of the key features and descriptions related to `pytest` tests, useful for understanding the functionality and usage of this popular testing framework in Python:
> 

| **Feature** | **Description** |
| --- | --- |
| **Test Discovery** | `pytest` automatically discovers test files and functions based on naming conventions, such as files starting with `test_` or ending with `_test.py`, and functions starting with `test_`. |
| **Fixtures** | Reusable pieces of code that can be shared across tests. Fixtures can be used for setup, teardown, and injecting dependencies into tests. |
| **Parameterization** | Allows running a test function multiple times with different arguments, using `@pytest.mark.parametrize`. This is useful for testing various input combinations. |
| **Assertions** | `pytest` provides better error messages for simple `assert` statements compared to standard `unittest`. If an assertion fails, `pytest` will provide detailed information about the failure. |
| **Plugins** | `pytest` has a rich ecosystem of plugins that extend its functionality, such as coverage reporting (`pytest-cov`), mocking (`pytest-mock`), and more. |
| **Markers** | Custom markers can be added to tests to categorize them or to apply conditional test execution. Common markers include `@pytest.mark.skip`, `@pytest.mark.xfail`, and user-defined markers. |
| **Test Grouping** | Tests can be grouped into classes or modules. While test classes are optional, they can be useful for organizing related tests and sharing setup/teardown code through `setup_method` and `teardown_method`. |
| **Test Setup and Teardown** | `pytest` supports multiple levels of setup and teardown, including module-level, class-level, and function-level fixtures, using `setup_module`, `setup_class`, `setup_method`, and equivalent teardown functions. |
| **Test Reporting** | Generates detailed test reports, including output on test successes, failures, and skips. Reports can be customized with plugins like `pytest-html` for HTML reports. |
| **Expected Failures and Skips** | Mark tests that are expected to fail (`@pytest.mark.xfail`) or should be skipped (`@pytest.mark.skip`). This helps in managing known issues or conditional testing. |
| **Capturing Output** | Captures output to stdout/stderr during test execution. This output is shown only if the test fails, helping with debugging without cluttering successful test runs. |
| **Test Filtering** | Use command-line options to run specific tests based on test names, markers, or file locations. Examples include `pytest -k 'expression'`, `pytest -m 'marker'`, or specifying the path directly. |
| **Debugging** | Supports integration with debuggers like `pdb`. You can invoke a debugger on test failures by adding `--pdb` to the command line, or use `pdb.set_trace()` within tests. |
| **Command-Line Interface** | `pytest` offers a powerful CLI with options for test selection, verbosity control, debugging, and more. Common commands include `pytest -v` for verbose output and `pytest --maxfail=1` to stop on the first failure. |
| **Code Coverage** | With the `pytest-cov` plugin, you can measure code coverage while running tests. It provides detailed reports on which parts of the codebase are covered by tests. |
| **Fixture Scope** | Fixtures can have different scopes: function, class, module, or session. This determines how often the fixture is invoked (e.g., once per test function, once per class, etc.). |
| **Assertions with Custom Messages** | Although `pytest` provides detailed failure messages, you can add custom error messages to assertions for additional clarity using the `assert <condition>, <message>` syntax. |
| **Test Parameterization with IDs** | When using `@pytest.mark.parametrize`, you can assign custom IDs to different test cases for more readable test output, using the `ids` parameter. |
| **Test Timeouts** | Tests can be configured to fail if they run longer than a specified time limit using the `pytest-timeout` plugin. This is useful for catching tests that hang. |

## References

- https://github.com/pytest-dev/pytest/
- https://docs.pytest.org/en/stable/
- https://pytest-cov.readthedocs.io/en/latest/readme.html#installation
- https://realpython.com/pytest-python-testing/