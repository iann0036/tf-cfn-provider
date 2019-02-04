# Terraform::CloudStack::AffinityGroup

Creates an affinity group.

## Properties

`Name` - (Required) The name of the affinity group. Changing this
forces a new resource to be created.

`Description` - (Optional) The description of the affinity group.

`Type` - (Required) The affinity group type. Changing this
forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to register this
affinity group to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The id of the affinity group.

`Description` - The description of the affinity group.

## See Also

* [cloudstack_affinity_group](https://www.terraform.io/docs/providers/cloudstack/r/affinity_group.html) in the _Terraform Provider Documentation_