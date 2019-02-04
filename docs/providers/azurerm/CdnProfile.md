# Terraform::AzureRM::CdnProfile

Manage a CDN Profile to create a collection of CDN Endpoints.

## Properties

`Name` - (Required) Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the CDN Profile.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) The pricing related information of current CDN profile. Accepted values are `Standard_Akamai`, `Standard_ChinaCdn`, `Standard_Microsoft`, `Standard_Verizon` or `Premium_Verizon`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The CDN Profile ID.

## See Also

* [azurerm_cdn_profile](https://www.terraform.io/docs/providers/azurerm/r/cdn_profile.html) in the _Terraform Provider Documentation_