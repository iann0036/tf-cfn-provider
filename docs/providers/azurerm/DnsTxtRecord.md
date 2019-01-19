# Terraform::AzureRM::DnsTxtRecord

Enables you to manage DNS TXT Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS TXT Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Record` - (Required) A list of values that make up the txt record. Each `Record` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Value` - (Required) The value of the record.


## Return Values

### Fn::GetAtt

`Id` - The DNS TXT Record ID.

## See Also

* [azurerm_dns_txt_record](https://www.terraform.io/docs/providers/azurerm/r/dns_txt_record.html) in the _Terraform Provider Documentation_