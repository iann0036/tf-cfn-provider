# Terraform::OCI::IdentityIdpGroupMapping

This resource provides the Idp Group Mapping resource in Oracle Cloud Infrastructure Identity service.

Creates a single mapping between an IdP group and an IAM Service
[group](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Group/).

## Properties

`GroupId` - (Required) (Updatable) The OCID of the IAM Service [group](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Group/) you want to map to the IdP group.

`IdentityProviderId` - (Required) The OCID of the identity provider.

`IdpGroupName` - (Required) (Updatable) The name of the IdP group you want to map.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the tenancy containing the `IdentityProvider`.

`GroupId` - The OCID of the IAM Service group that is mapped to the IdP group.

`Id` - The OCID of the `IdpGroupMapping`.

`IdentityProviderId` - The OCID of the `IdentityProvider` this mapping belongs to.

`IdpGroupName` - The name of the IdP group that is mapped to the IAM Service group.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`State` - The mapping's current state.

`TimeCreated` - Date and time the mapping was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_identity_idp_group_mapping](https://www.terraform.io/docs/providers/oci/r/identity_idp_group_mapping.html) in the _Terraform Provider Documentation_