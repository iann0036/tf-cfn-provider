# Terraform::HuaweiCloud::ComputeSecgroupV2

Manages a V2 security group resource within HuaweiCloud.

Please note that managing security groups through the HuaweiCloud Compute API
has been deprecated. Unless you are using an older HuaweiCloud environment, it is
recommended to use the [`huaweicloud_networking_secgroup_v2`](networking_secgroup_v2.html)
and [`huaweicloud_networking_secgroup_rule_v2`](networking_secgroup_rule_v2.html)
resources instead, which uses the HuaweiCloud Networking API.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Region` - See Argument Reference above.

`Name` - See Argument Reference above.

`Description` - See Argument Reference above.

`Rule` - See Argument Reference above.

## See Also

* [huaweicloud_compute_secgroup_v2](https://www.terraform.io/docs/providers/huaweicloud/r/compute_secgroup_v2.html) in the _Terraform Provider Documentation_