# Terraform::AzureRM::DnsMxRecord

Enables you to manage DNS MX Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS MX Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Record` - (Required) A list of values that make up the MX record. Each `Record` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Preference` - (Required) String representing the "preference” value of the MX records. Records with lower preference value take priority.

`Exchange` - (Required) The mail server responsible for the domain covered by the MX record.


## Return Values

### Fn::GetAtt

`Id` - The DNS MX Record ID.

## See Also

* [azurerm_dns_mx_record](https://www.terraform.io/docs/providers/azurerm/r/dns_mx_record.html) in the _Terraform Provider Documentation_