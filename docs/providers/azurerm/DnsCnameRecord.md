# Terraform::AzureRM::DnsCnameRecord

Enables you to manage DNS CNAME Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS CNAME Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`TTL` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Record` - (Required) The target of the CNAME.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The DNS CName Record ID.

## See Also

* [azurerm_dns_cname_record](https://www.terraform.io/docs/providers/azurerm/r/dns_cname_record.html) in the _Terraform Provider Documentation_