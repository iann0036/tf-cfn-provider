# Terraform::Alicloud::NetworkInterface

Provides an ECS Elastic Network Interface resource.

For information about Elastic Network Interface and how to use it, see [Elastic Network Interface](https://www.alibabacloud.com/help/doc-detail/58496.html).

~> **NOTE** Only one of private_ips or private_ips_count can be specified when assign private IPs.

## Properties

`VswitchId` - (Required, ForceNew) The VSwitch to create the ENI in.

`SecurityGroups` - (Require) A list of security group ids to associate with.

`PrivateIp` - (Optional) The primary private IP of the ENI.

`Name` - (Optional) Name of the ENI. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-", ".", "_", and must not begin or end with a hyphen, and must not begin with http:// or https://. Default value is null.

`Description` - (Optional) Description of the ENI. This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Default value is null.

`PrivateIps` - (Optional) List of secondary private IPs to assign to the ENI. Don't use both private_ips and private_ips_count in the same ENI resource block.

`PrivateIpsCount` - (Optional) Number of secondary private IPs to assign to the ENI. Don't use both private_ips and private_ips_count in the same ENI resource block.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ENI ID.

## See Also

* [alicloud_network_interface](https://www.terraform.io/docs/providers/alicloud/r/network_interface.html) in the _Terraform Provider Documentation_