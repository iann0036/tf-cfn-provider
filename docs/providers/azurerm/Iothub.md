# Terraform::AzureRM::Iothub

Manages an IotHub

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the IoTHub.

`EventHubEventsEndpoint` -  The EventHub compatible endpoint for events data.

`EventHubEventsPath` -  The EventHub compatible path for events data.

`EventHubOperationsEndpoint` -  The EventHub compatible endpoint for operational data.

`EventHubOperationsPath` -  The EventHub compatible path for operational data.

`Hostname` - The hostname of the IotHub Resource.

`SharedAccessPolicy` - One or more `shared_access_policy` blocks as defined below.

`KeyName` - The name of the shared access policy.

`PrimaryKey` - The primary key.

`SecondaryKey` - The secondary key.

`Permissions` - The permissions assigned to the shared access policy.

## See Also

* [azurerm_iothub](https://www.terraform.io/docs/providers/azurerm/r/iothub.html) in the _Terraform Provider Documentation_