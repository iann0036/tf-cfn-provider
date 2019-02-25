# Terraform::NSXT::NsGroup

This resource provides a method to create and manage a network and security (NS) group in NSX. A NS group is used to group other objects into collections for application of other settings.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this NS group.

`Member` - (Optional) Reference to the direct/static members of the NSGroup. Can be ID based expressions only. VirtualMachine cannot be added as a static member.
* `TargetType` - (Required) Static member type, one of: NSGroup, IPSet, LogicalPort, LogicalSwitch, MACSet
* `Value` - (Required) Member ID.

`TargetType` - (Required) Static member type, one of: NSGroup, IPSet, LogicalPort, LogicalSwitch, MACSet
* `Value` - (Required) Member ID.

`Value` - (Required) Member ID.

`MembershipCriteria` - (Optional) List of tag or ID expressions which define the membership criteria for this NSGroup. An object must satisfy at least one of these expressions to qualify as a member of this group.
* `TargetType` - (Required) Dynamic member type, one of: LogicalPort, LogicalSwitch, VirtualMachine.
* `Scope` - (Optional) Tag scope for matching dynamic members.
* `Tag` - (Optional) Tag value for matching dynamic members.

`TargetType` - (Required) Dynamic member type, one of: LogicalPort, LogicalSwitch, VirtualMachine.
* `Scope` - (Optional) Tag scope for matching dynamic members.
* `Tag` - (Optional) Tag value for matching dynamic members.

`Scope` - (Optional) Tag scope for matching dynamic members.
* `Tag` - (Optional) Tag value for matching dynamic members.

`Tag` - (Optional) Tag value for matching dynamic members.


## Return Values

### Fn::GetAtt

`Id` - ID of the NS group.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ns_group](https://www.terraform.io/docs/providers/nsxt/r/ns_group.html) in the _Terraform Provider Documentation_