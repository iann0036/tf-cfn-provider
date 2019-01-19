# Terraform::AzureStack::ResourceGroup

Creates a new resource group on Azure.

## Properties

`Name` - (Required) The name of the resource group. Must be unique on your Azure subscription.

`Location` - (Required) The location where the resource group should be created. For a list of all Azure locations, please consult [this link](http://azure.microsoft.com/en-us/regions/) or run `az account list-locations --output table`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The resource group ID.

## See Also

* [azurestack_resource_group](https://www.terraform.io/docs/providers/azurestack/r/resource_group.html) in the _Terraform Provider Documentation_