# Terraform::AzureStack::DnsARecord

Enables you to manage DNS A Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS A Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`TTL` - (Required) The Time To Live (TTL) of the DNS record.

`Records` - (Required) List of IPv4 Addresses.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS A Record ID.

## See Also

* [azurestack_dns_a_record](https://www.terraform.io/docs/providers/azurestack/r/dns_a_record.html) in the _Terraform Provider Documentation_