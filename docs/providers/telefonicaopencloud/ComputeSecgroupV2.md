# Terraform::TelefonicaOpenCloud::ComputeSecgroupV2

Manages a V2 security group resource within TelefonicaOpenCloud.

Please note that managing security groups through the TelefonicaOpenCloud Compute API
has been deprecated. Unless you are using an older TelefonicaOpenCloud environment, it is
recommended to use the [`telefonicaopencloud_networking_secgroup_v2`](networking_secgroup_v2.html)
and [`telefonicaopencloud_networking_secgroup_rule_v2`](networking_secgroup_rule_v2.html)
resources instead, which uses the TelefonicaOpenCloud Networking API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Name` - See Argument Reference above.

`Description` - See Argument Reference above.

`Rule` - See Argument Reference above.

## See Also

* [telefonicaopencloud_compute_secgroup_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/compute_secgroup_v2.html) in the _Terraform Provider Documentation_