## Getting Started

This page introduces basics of Python as a start point 

## Installing packages 

By default if you install package via pip, it'll install the packages **globally** means for all Python applications for your PC, which is why common way to install packages locally by using a **virtual environment** ( similar to package.json then cread node_modules folder )

```
# Install virtual environment
pip install virtualenv

# Windows systems
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

```

Activate the virtual envionment in windows ( here **venv** is the folder name)  : 


```
# by using powershell 
 .\venv\Scripts\activate.ps1

# by uing cmd.exe
 .\venv\Scripts\activate.bat

# Bash Shell 
../venu/Scripts/activate

```

Then you can use the following method to install Python packages, to use pip to install an individual package, you'll use the following command  : 

  ```
    pip install < package name >
  ```

If you would like to install from a list of packages  :

  ```
    pip install -r requirements.txt 
  ```


Youtube course they took 'colorama' package as an example. 

## Input and print out variables 

When you're ready, just show you some quick examples : 


    ```
    # this is a comment
    print('What is your name?')
    name = input()
    print(name)

    ```


## Coding in VS Code

Quick comment and discomment with shortcut : CTRL + / 

## Functions

In Play 2 we introduced formatting and functions. A function is an individual structured piece designed to reuse of code snippets.  Check out a sample function that I've created under the folder Modules, it's called : hello_functions.py

## Modules

A module is a python file with functions, classes and other components. It is designed to break code down into individual reusable structured pieces. 

### How to input a module : 

Just take the module hello_module.py that I've created, log_helper.py

```
def show_log(sample_log, is_exception=False):
    if is_exception:
        print('this is an exception !')
    print(sample_log)

```

Let's call it from other modules ( different ways vary from the scope of modules to import ):

Option 1 : Import the whole namespace, this way must be the most comfortable way for JavaScript developer. 

```
import log_helper  # import the whole namespace 

log_helper.show_log('This a log message !')

```


Option 2 : Import the whole namespace into current namespace ( basically, the advantage of this option is to use direct method name in the code )

```
from log_helper import *

show_log('This a log message !')

```


Option 3 : Import specific methods into current namespace ( here show_log is the specific method that you're importing )

```
# if you use only the show log function
from log_helper import show_log   

show_log('This a log message !')

```


