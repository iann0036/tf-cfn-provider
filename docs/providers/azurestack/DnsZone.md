# Terraform::AzureStack::DnsZone

Enables you to manage DNS zones within Azure DNS. These zones are hosted on Azure's name servers to which you can delegate the zone from the parent domain.

## Properties

`Name` - (Required) The name of the DNS Zone. Must be a valid domain name.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS Zone ID.

`MaxNumberOfRecordSets` - (Optional) Maximum number of Records in the zone. Defaults to `1000`.

`NumberOfRecordSets` - (Optional) The number of records already in the zone.

`NameServers` - (Optional) A list of values that make up the NS record for the zone.

## See Also

* [azurestack_dns_zone](https://www.terraform.io/docs/providers/azurestack/r/dns_zone.html) in the _Terraform Provider Documentation_