# Terraform::UCloud::Vpc

Provides a VPC resource.

## Properties

`CidrBlocks` - (Required) The CIDR blocks of VPC.

`Name` - (Optional) The name of VPC. If not specified, terraform will autogenerate a name beginning with `tf-vpc`.

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

`Remark` - (Optional) The remarks of the VPC. (Default: `""`).


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation for VPC, formatted in RFC3339 time string.

`UpdateTime` - The time whenever there is a change made to VPC, formatted in RFC3339 time string.

`NetworkInfo` - It is a nested type which documented below.

`CidrBlock` - The CIDR block of the VPC.

## See Also

* [ucloud_vpc](https://www.terraform.io/docs/providers/ucloud/r/vpc.html) in the _Terraform Provider Documentation_