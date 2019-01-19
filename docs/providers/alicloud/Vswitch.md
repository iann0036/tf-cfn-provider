# Terraform::Alicloud::Vswitch

Provides a VPC switch resource.

## Properties

`AvailabilityZone` - (Required, Forces new resource) The AZ for the switch.

`VpcId` - (Required, Forces new resource) The VPC ID.

`CidrBlock` - (Required, Forces new resource) The CIDR block for the switch.

`Name` - (Optional) The name of the switch. Defaults to null.

`Description` - (Optional) The switch description. Defaults to null.


## Return Values

### Fn::GetAtt

`Id` - The ID of the switch.

`CidrBlock` - The CIDR block for the switch.

`VpcId` - The VPC ID.

`Name` - The name of the switch.

`Description` - The description of the switch.

## See Also

* [alicloud_vswitch](https://www.terraform.io/docs/providers/alicloud/r/vswitch.html) in the _Terraform Provider Documentation_