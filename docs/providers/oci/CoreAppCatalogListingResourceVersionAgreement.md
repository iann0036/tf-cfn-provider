# Terraform::OCI::CoreAppCatalogListingResourceVersionAgreement

The `Terraform::OCI::CoreAppCatalogListingResourceVersionAgreement` resource creates AppCatalogListingResourceVersionAgreement for a particular resource version of a listing.

## Properties

`ListingId` - (Required) The OCID of the listing.

`ListingResourceVersion` - (Required) Listing Resource Version.


## Return Values

### Fn::GetAtt

`EulaLink` - EULA link.

`ListingId` - The OCID of the listing associated with these agreements.

`ListingResourceVersion` - Listing resource version associated with these agreements.

`OracleTermsOfUseLink` - Oracle TOU link.

`Signature` - A generated signature for this agreement retrieval operation which should be used in the create subscription call.

`TimeRetrieved` - Date and time the agreements were retrieved, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`.

## See Also

* [oci_core_app_catalog_listing_resource_version_agreement](https://www.terraform.io/docs/providers/oci/r/core_app_catalog_listing_resource_version_agreement.html) in the _Terraform Provider Documentation_