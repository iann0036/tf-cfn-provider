# Terraform::AzureRM::DnsSrvRecord

Enables you to manage DNS SRV Records within Azure DNS.

## Properties

`Name` - (Required) The name of the DNS SRV Record.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`ZoneName` - (Required) Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

`Ttl` - (Required) The Time To Live (TTL) of the DNS record in seconds.

`Record` - (Required) A list of values that make up the SRV record. Each `Record` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Priority` - (Required) Priority of the SRV record.

`Weight` - (Required) Weight of the SRV record.

`Port` - (Required) Port the service is listening on.

`Target` - (Required) FQDN of the service.


## Return Values

### Fn::GetAtt

`Id` - The DNS SRV Record ID.

## See Also

* [azurerm_dns_srv_record](https://www.terraform.io/docs/providers/azurerm/r/dns_srv_record.html) in the _Terraform Provider Documentation_