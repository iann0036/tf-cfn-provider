# Terraform::AzureRM::EventgridTopic

Manages an EventGrid Topic

~> **Note:** at this time EventGrid Topic's are only available in a limited number of regions.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The EventGrid Topic ID.

`Endpoint` - The Endpoint associated with the EventGrid Topic.

`PrimaryAccessKey` - The Primary Shared Access Key associated with the EventGrid Topic.

`SecondaryAccessKey` - The Secondary Shared Access Key associated with the EventGrid Topic.

## See Also

* [azurerm_eventgrid_topic](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_topic.html) in the _Terraform Provider Documentation_