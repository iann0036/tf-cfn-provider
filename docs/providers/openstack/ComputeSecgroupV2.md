# Terraform::OpenStack::ComputeSecgroupV2

Manages a V2 security group resource within OpenStack.

Please note that managing security groups through the OpenStack Compute API
has been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the [`openstack_networking_secgroup_v2`](networking_secgroup_v2.html)
and [`openstack_networking_secgroup_rule_v2`](networking_secgroup_rule_v2.html)
resources instead, which uses the OpenStack Networking API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Name` - See Argument Reference above.

`Description` - See Argument Reference above.

`Rule` - See Argument Reference above.

## See Also

* [openstack_compute_secgroup_v2](https://www.terraform.io/docs/providers/openstack/r/compute_secgroup_v2.html) in the _Terraform Provider Documentation_