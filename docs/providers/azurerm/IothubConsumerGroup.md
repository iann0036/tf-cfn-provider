# Terraform::AzureRM::IothubConsumerGroup

Manages a Consumer Group within an IotHub

## Properties

`Name` - (Required) The name of this Consumer Group. Changing this forces a new resource to be created.

`IothubName` - (Required) The name of the IoT Hub. Changing this forces a new resource to be created.

`EventhubEndpointName` - (Required) The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the IoTHub Consumer Group.

## See Also

* [azurerm_iothub_consumer_group](https://www.terraform.io/docs/providers/azurerm/r/iothub_consumer_group.html) in the _Terraform Provider Documentation_