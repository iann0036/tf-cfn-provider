# Terraform::AzureStack::AvailabilitySet

Manages an availability set for virtual machines.

## Properties

`Name` - (Required) Specifies the name of the availability set. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`PlatformUpdateDomainCount` - (Optional) Specifies the number of update domains that are used. Defaults to 5.

`PlatformFaultDomainCount` - (Optional) Specifies the number of fault domains that are used. Defaults to 3.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The virtual Availability Set ID.

## See Also

* [azurestack_availability_set](https://www.terraform.io/docs/providers/azurestack/r/availability_set.html) in the _Terraform Provider Documentation_