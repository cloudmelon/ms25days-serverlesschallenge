## Getting Started



## Installing packages 

use pip to install an individual package : 

  ```
    pip install < package name >
  ```

If you would like to install from a list of packages :

  ```
    pip install -r requirements.txt 
  ```
  
## Input and print out variables 

When you're ready 


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


