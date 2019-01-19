# Terraform::AzureRM::DnsNsRecord

Enables you to manage DNS NS Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS NS Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Records` - (Optional) A list of values that make up the NS record. *WARNING*: Either `Records` or `Record` is required.

`Record` - (Optional) A list of values that make up the NS record. Each `Record` block supports fields documented below. This field has been deprecated and will be removed in a future release.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Record Properties

`Nsdname` - (Required) The value of the record.


## Return Values

### Fn::GetAtt

`Id` - The DNS NS Record ID.

## See Also

* [azurerm_dns_ns_record](https://www.terraform.io/docs/providers/azurerm/r/dns_ns_record.html) in the _Terraform Provider Documentation_