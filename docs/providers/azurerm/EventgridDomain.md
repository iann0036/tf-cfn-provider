# Terraform::AzureRM::EventgridDomain

Manages an EventGrid Domain

## Properties

`Name` - (Required) Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`InputSchema` - (Optional) Specifies the schema in which incoming events will be published to this domain. Allowed values are `cloudeventv01schema`, `customeventschema`, or `eventgridschema`. Defaults to `eventgridschema`. Changing this forces a new resource to be created.

`InputMappingFields` - (Optional) A `InputMappingFields` block as defined below.

`InputMappingDefaultValues` - (Optional) A `InputMappingDefaultValues` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### InputMappingFields Properties

`Id` - (Optional) Specifies the id of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`Topic` - (Optional) Specifies the topic of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`EventType` - (Optional) Specifies the event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`EventTime` - (Optional) Specifies the event time of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`DataVersion` - (Optional) Specifies the data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`Subject` - (Optional) Specifies the subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

### InputMappingDefaultValues Properties

`EventType` - (Optional) Specifies the default event type of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`DataVersion` - (Optional) Specifies the default data version of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.

`Subject` - (Optional) Specifies the default subject of the EventGrid Event to associate with the domain. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the EventGrid Domain.

`Endpoint` - The Endpoint associated with the EventGrid Domain.

## See Also

* [azurerm_eventgrid_domain](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_domain.html) in the _Terraform Provider Documentation_