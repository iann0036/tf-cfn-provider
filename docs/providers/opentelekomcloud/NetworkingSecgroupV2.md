# Terraform::OpenTelekomCloud::NetworkingSecgroupV2

Manages a V2 neutron security group resource within OpenTelekomCloud.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client. A networking client is needed to create a port. If omitted, the `Region` argument of the provider is used. Changing this creates a new security group.

`Name` - (Required) A unique name for the security group.

`Description` - (Optional) A unique name for the security group.

`TenantId` - (Optional) The owner of the security group. Required if admin wants to create a port for another tenant. Changing this creates a new security group.

`DeleteDefaultRules` - (Optional) Whether or not to delete the default egress security rules. This is `false` by default. See the below note for more information.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [opentelekomcloud_networking_secgroup_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/networking_secgroup_v2.html) in the _Terraform Provider Documentation_