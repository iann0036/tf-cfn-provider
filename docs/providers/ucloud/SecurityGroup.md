# Terraform::UCloud::SecurityGroup

Provides a Security Group resource.

## Properties

`Rules` - (Required) A list of security group rules. Each element contains the following attributes: `Protocol`, `PortRange`, `CidrBlock`, `Policy` (possbile values are:`accept` and `drop`) and priority (possible values are: `high`, `medium` and `low`. (eg: tcp|22|192.168.1.1/22|drop|low).

`Name` - (Optional) The name of the security group which contains 1-63 characters and only support Chinese, English, numbers, '-', '_' and '.'. If not specified, terraform will autogenerate a name beginning with `tf-security-group`.

`Remark` - (Optional) The remarks of the security group. (Default: `""`).

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

### Rules Properties

`CidrBlock` - The cidr block of source.

`Policy` - Authorization policy. Can be either `accept` or `drop`.

`PortRange` - The range of port numbers, range: 1-65535. (eg: `port` or `port1-port2`).

`Priority` - Rule priority. Can be `high`, `medium`, `low`.

`Protocol` - The protocol. Can be `tcp`, `udp`, `icmp`, `gre`.


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation of security group, formatted in RFC3339 time string.

## See Also

* [ucloud_security_group](https://www.terraform.io/docs/providers/ucloud/r/security_group.html) in the _Terraform Provider Documentation_