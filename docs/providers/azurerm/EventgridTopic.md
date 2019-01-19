# Terraform::AzureRM::EventgridTopic

Manages an EventGrid Topic

~> **Note:** at this time EventGrid Topic's are only available in a limited number of regions.

## Properties

`Name` - (Required) Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The EventGrid Topic ID.

`Endpoint` - The Endpoint associated with the EventGrid Topic.

`PrimaryAccessKey` - The Primary Shared Access Key associated with the EventGrid Topic.

`SecondaryAccessKey` - The Secondary Shared Access Key associated with the EventGrid Topic.

## See Also

* [azurerm_eventgrid_topic](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic.html) in the _Terraform Provider Documentation_