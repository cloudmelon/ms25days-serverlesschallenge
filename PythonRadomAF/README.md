# Python Azure Functions

There are a couple of files in this example : 

- **__init__.py** is the python source code file
- **function.json** is where you set up your trigger and bindings
- **host.json** defines your Azure function version

If you want to work with with Log Analytics, here is the query that you can use :

 ```shell
requests
| project timestamp, id, operation_Name, success, resultCode, duration, operation_Id, cloud_RoleName, invocationId=customDimensions['InvocationId']
| where timestamp > ago(30d)
| where cloud_RoleName =~ 'name of function app' and operation_Name == 'name of your azure function'
| order by timestamp desc
| take 20

 ```
