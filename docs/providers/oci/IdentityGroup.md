# Terraform::OCI::IdentityGroup

This resource provides the Group resource in Oracle Cloud Infrastructure Identity service.

Creates a new group in your tenancy.

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
reside within compartments inside the tenancy. For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You must also specify a *name* for the group, which must be unique across all groups in your tenancy and
cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more
information about policies, see [How Policies Work](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

You must also specify a *description* for the group (although it can be an empty string). It does not
have to be unique, and you can change it anytime with [UpdateGroup](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Group/UpdateGroup).
After creating the group, you need to put users in it and write policies for it.
See [AddUserToGroup](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/UserGroupMembership/AddUserToGroup) and
[CreatePolicy](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Policy/CreatePolicy).

## Properties

`CompartmentId` - (Required) The OCID of the tenancy containing the group.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - (Required) (Updatable) The description you assign to the group during creation. Does not have to be unique, and it's changeable.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Name` - (Required) The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the tenancy containing the group.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - The description you assign to the group. Does not have to be unique, and it's changeable.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Id` - The OCID of the group.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`Name` - The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`State` - The group's current state.

`TimeCreated` - Date and time the group was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_identity_group](https://www.terraform.io/docs/providers/oci/r/identity_group.html) in the _Terraform Provider Documentation_