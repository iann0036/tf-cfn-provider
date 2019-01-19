# Terraform::AzureRM::DnsPtrRecord

Enables you to manage DNS PTR Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS PTR Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Records` - (Required) List of Fully Qualified Domain Names.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS PTR Record ID.

## See Also

* [azurerm_dns_ptr_record](https://www.terraform.io/docs/providers/azurerm/r/dns_ptr_record.html) in the _Terraform Provider Documentation_