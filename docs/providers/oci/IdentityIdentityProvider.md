# Terraform::OCI::IdentityIdentityProvider

This resource provides the Identity Provider resource in Oracle Cloud Infrastructure Identity service.

Creates a new identity provider in your tenancy. For more information, see
[Identity Providers and Federation](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/federation.htm).

You must specify your tenancy's OCID as the compartment ID in the request object.
Remember that the tenancy is simply the root compartment. For information about
OCIDs, see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You must also specify a *name* for the `IdentityProvider`, which must be unique
across all `IdentityProvider` objects in your tenancy and cannot be changed.

You must also specify a *description* for the `IdentityProvider` (although
it can be an empty string). It does not have to be unique, and you can change
it anytime with
[UpdateIdentityProvider](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/IdentityProvider/UpdateIdentityProvider).

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the tenancy containing the `IdentityProvider`.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`Description` - The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable.

`FreeformAttributes` - Extra name value pairs associated with this identity provider. Example: `{"clientId": "app_sf3kdjf3"}`.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Id` - The OCID of the `IdentityProvider`.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`MetadataUrl` - The URL for retrieving the identity provider's metadata, which contains information required for federating.

`Name` - The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed. This is the name federated users see when choosing which identity provider to use when signing in to the Oracle Cloud Infrastructure Console.

`ProductType` - The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).

`Protocol` - The protocol used for federation. Allowed value: `SAML2`.  Example: `SAML2`.

`RedirectUrl` - The URL to redirect federated users to for authentication with the identity provider.

`SigningCertificate` - The identity provider's signing certificate used by the IAM Service to validate the SAML2 token.

`State` - The current state.

`TimeCreated` - Date and time the `IdentityProvider` was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_identity_identity_provider](https://www.terraform.io/docs/providers/oci/r/identity_identity_provider.html) in the _Terraform Provider Documentation_