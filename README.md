Python-selenium-starter
=========
Starter set up for writing selenium tests with Python. The Goal is to make it easier to write and run tests
using Selenium for multiple browsers and devices. With this repo, you should be able to just start writing your tests
and not be concerned with the basic set up of your test framework. This has options to also run on browserstack but could easily be modified to use another service with some elementary coding.

Installing Selenium
----------
- Install pip first if needed obviously (google is your friend here)
- pip install -U selenium


Getting Started
-----------
- You can add more tests by adding modules to the tests directory. Copy the structure in the examples and your tests
should be executed automagically by the above.
- You will likely want to update the data in the config.py file. But should not need to update anything in the
run.py file unless you are applying a general fix to this repo that you plan to contribute..

General Examples
---------
To run all tests on Firefox
```
python run.py
```
To override the base url you set in run.py
```
python run.py --base_url "http://google.com"
````
To only run one test
```
python run.py --test "example_a.py"
````
To see more options
```
python run.py --help
```
