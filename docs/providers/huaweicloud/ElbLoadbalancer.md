# Terraform::HuaweiCloud::ElbLoadbalancer

Manages an elastic loadbalancer resource within huawei cloud.

## Properties

`Name` - (Required) Specifies the load balancer name. The name is a string
of 1 to 64 characters that consist of letters, digits, underscores (_),
and hyphens (-).

`Description` - (Optional) Provides supplementary information about the
listener. The value is a string of 0 to 128 characters and cannot be <>.

`VpcId` - (Required) Specifies the VPC ID.

`Bandwidth` - (Optional) Specifies the bandwidth (Mbit/s). This parameter
is mandatory when type is set to External, and it is invalid when type
is set to Internal. The value ranges from 1 to 300.

`Type` - (Required) Specifies the load balancer type. The value can be
Internal or External.

`AdminStateUp` - (Required) Specifies the status of the load balancer.
Value range: 0 or false: indicates that the load balancer is stopped. Only
tenants are allowed to enter these two values. 1 or true: indicates that
the load balancer is running properly. 2 or false: indicates that the load
balancer is frozen. Only tenants are allowed to enter these two values.

`VipSubnetId` - (Optional) Specifies the ID of the private network
to be added. This parameter is mandatory when type is set to Internal,
and it is invalid when type is set to External.

`Az` - (Optional) Specifies the ID of the availability zone (AZ). This
parameter is mandatory when type is set to Internal, and it is invalid
when type is set to External.

`ChargeMode` - (Optional) This is a reserved field. If the system supports
charging by traffic and this field is specified, then you are charged by
traffic for elastic IP addresses. The value is traffic.

`EipType` - (Optional) This parameter is reserved.

`SecurityGroupId` - (Optional) Specifies the security group ID. The
value is a string of 1 to 200 characters that consists of uppercase and
lowercase letters, digits, and hyphens (-). This parameter is mandatory
only when type is set to Internal.

`VipAddress` - (Optional) Specifies the IP address provided by ELB.
When typeis set to External, the value of this parameter is the elastic
IP address. When type is set to Internal, the value of this parameter is
the private network IP address. You can select an existing elastic IP address
and create a public network load balancer. When this parameter is configured,
parameters bandwidth, charge_mode, and eip_type are invalid.

`Tenantid` - (Optional) Specifies the tenant ID. This parameter is mandatory
only when type is set to Internal.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`Description` - See Properties above.

`VpcId` - See Properties above.

`Bandwidth` - See Properties above.

`Type` - See Properties above.

`AdminStateUp` - See Properties above.

`VipSubnetId` - See Properties above.

`Az` - See Properties above.

`ChargeMode` - See Properties above.

`EipType` - See Properties above.

`SecurityGroupId` - See Properties above.

`VipAddress` - See Properties above.

`Tenantid` - See Properties above.

`UpdateTime` - Specifies the time when information about the load balancer.

`CreateTime` - Specifies the time when the load balancer was created.

`Id` - Specifies the load balancer ID.

`Status` - Specifies the status of the load balancer. The value can be.

## See Also

* [huaweicloud_elb_loadbalancer](https://www.terraform.io/docs/providers/huaweicloud/r/elb_loadbalancer.html) in the _Terraform Provider Documentation_