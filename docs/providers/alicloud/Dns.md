# Terraform::Alicloud::Dns

Provides a DNS Record resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The record id.

`Name` - (Required) The record domain name.

`Type` - (Required) The record type.

`HostRecord` - The host record of record.

`Value` - The record value.

`Ttl` - The record effective time.

`Priority` - The record priority.

`Routing` - The record parsing line.

`Status` - The record status. `Enable` or `Disable`.

`Locked` - The record locked state. `true` or `false`.

## See Also

* [alicloud_dns](https://www.terraform.io/docs/providers/alicloud/r/dns.html) in the _Terraform Provider Documentation_