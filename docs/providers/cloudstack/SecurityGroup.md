# Terraform::CloudStack::SecurityGroup

Creates a security group.

## Properties

`Name` - (Required) The name of the security group. Changing this forces a new resource to be created.

`Description` - (Optional) The description of the security group. Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to create this security group in. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group.

## See Also

* [cloudstack_security_group](https://www.terraform.io/docs/providers/cloudstack/r/security_group.html) in the _Terraform Provider Documentation_