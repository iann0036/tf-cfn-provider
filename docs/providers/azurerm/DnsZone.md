# Terraform::AzureRM::DnsZone

Enables you to manage DNS zones within Azure DNS. These zones are hosted on Azure's name servers to which you can delegate the zone from the parent domain.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The DNS Zone ID.

`MaxNumberOfRecordSets` - (Optional) Maximum number of Records in the zone. Defaults to `1000`.

`NumberOfRecordSets` - (Optional) The number of records already in the zone.

`NameServers` - (Optional) A list of values that make up the NS record for the zone.

## See Also

* [azurerm_dns_zone](https://www.terraform.io/docs/providers/azurerm/r/dns_zone.html) in the _Terraform Provider Documentation_