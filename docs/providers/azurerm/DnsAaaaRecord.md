# Terraform::AzureRM::DnsAaaaRecord

Enables you to manage DNS AAAA Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS AAAA Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`TTL` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Records` - (Required) List of IPv6 Addresses.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS AAAA Record ID.

## See Also

* [azurerm_dns_aaaa_record](https://www.terraform.io/docs/providers/azurerm/r/dns_aaaa_record.html) in the _Terraform Provider Documentation_