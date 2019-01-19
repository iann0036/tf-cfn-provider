# Terraform::Alicloud::Dns

Provides a DNS Record resource.

## Properties

`Name` - (Required) Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.

`HostRecord` - (Required) Host record for the domain record. This host_record can have at most 253 characters, and each part split with "." can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as "-",".","*","@",  and must not begin or end with "-".

`Type` - (Required) The type of domain record. Valid values are `A`,`NS`,`MX`,`TXT`,`CNAME`,`SRV`,`AAAA`,`REDIRECT_URL` and `FORWORD_URL`.

`Value` - (Required) The value of domain record.

`Ttl` - (Optional) The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is `[600, 86400]`, Basic is `[120, 86400]`, Standard is `[60, 86400]`, Ultimate is `[10, 86400]`, Exclusive is `[1, 86400]`. Default value is `600`.

`Priority` - (Optional) The priority of domain record. Valid values are `[1-10]`. When the `Type` is `MX`, this parameter is required.

`Routing` - (Optional) The parsing line of domain record. Valid values are `default`, `telecom`, `unicom`, `mobile`, `oversea` and `edu`. When the `Type` is `FORWORD_URL`, this parameter must be `default`. Default value is `default`.


## Return Values

### Fn::GetAtt

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