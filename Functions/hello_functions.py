# Define your first function

def call_function():
    print('hello functions !')

def params_function(sample_param):
    print(sample_param)

def multiparams_function(sample_param, function_name='default function'):
    print(sample_param, function_name)

call_function()
params_function('hello param function !')
multiparams_function('hello multiparams ', 'hello function !')

print('call multiparams function again')
multiparams_function('hello multiparams ')