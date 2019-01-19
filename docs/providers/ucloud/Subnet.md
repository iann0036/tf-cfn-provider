# Terraform::UCloud::Subnet

Provides a Subnet resource under VPC resource.

## Properties

`CidrBlock` - (Required) The cidr block of the desired subnet, format in "0.0.0.0/0", such as: `192.168.0.0/24`.

`VpcId` - (Required) The id of the VPC that the desired subnet belongs to.

`Name` - (Optional) The name of the desired subnet. If not specified, terraform will autogenerate a name beginning with `tf-subnet`.

`Remark` - (Optional) The remarks of the subnet. (Default: `""`).

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation of subnet, formatted in RFC3339 time string.

## See Also

* [ucloud_subnet](https://www.terraform.io/docs/providers/ucloud/r/subnet.html) in the _Terraform Provider Documentation_