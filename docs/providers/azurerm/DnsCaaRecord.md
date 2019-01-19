# Terraform::AzureRM::DnsCaaRecord

Enables you to manage DNS CAA Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS CAA Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Record` - (Required) A list of values that make up the CAA record. Each `Record` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Flags` - (Required) Extensible CAA flags, currently only 1 is implemented to set the issuer critical flag.

`Tag` - (Required) A property tag, options are issue, issuewild and iodef.

`Value` - (Required) A property value such as a registrar domain.


## Return Values

### Fn::GetAtt

`Id` - The DNS CAA Record ID.

## See Also

* [azurerm_dns_caa_record](https://www.terraform.io/docs/providers/azurerm/r/dns_caa_record.html) in the _Terraform Provider Documentation_