# Terraform::AzureRM::DnsZone

Enables you to manage DNS zones within Azure DNS. These zones are hosted on Azure's name servers to which you can delegate the zone from the parent domain.

## Properties

`Name` - (Required) The name of the DNS Zone. Must be a valid domain name.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneType` - (Required) Specifies the type of this DNS zone. Possible values are `Public` or `Private` (Defaults to `Public`).

`RegistrationVirtualNetworkIds` - (Optional) A list of Virtual Network ID's that register hostnames in this DNS zone. This field can only be set when `ZoneType` is set to `Private`.

`ResolutionVirtualNetworkIds` - (Optional) A list of Virtual Network ID's that resolve records in this DNS zone. This field can only be set when `ZoneType` is set to `Private`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS Zone ID.

`MaxNumberOfRecordSets` - (Optional) Maximum number of Records in the zone. Defaults to `1000`.

`NumberOfRecordSets` - (Optional) The number of records already in the zone.

`NameServers` - (Optional) A list of values that make up the NS record for the zone.

## See Also

* [azurerm_dns_zone](https://www.terraform.io/docs/providers/azurerm/r/dns_zone.html) in the _Terraform Provider Documentation_