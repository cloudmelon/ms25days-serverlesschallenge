# Python Azure Functions

There are a couple of files in this example : 




If you want to work with with Log Analytics :

''' shell
requests
| project timestamp, id, operation_Name, success, resultCode, duration, operation_Id, cloud_RoleName, invocationId=customDimensions['InvocationId']
| where timestamp > ago(30d)
| where cloud_RoleName =~ 'melon-serverlesschallenge-app' and operation_Name == 'C1-ServerlessDreidel'
| order by timestamp desc
| take 20

''' shell
