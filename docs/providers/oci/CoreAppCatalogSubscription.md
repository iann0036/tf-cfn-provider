# Terraform::OCI::CoreAppCatalogSubscription

This resource provides the App Catalog Subscription resource in Oracle Cloud Infrastructure Core service.

Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.

## Properties

`CompartmentId` - (Optional) The compartmentID for the subscription.

`EulaLink` - (Optional) EULA link.

`ListingId` - (Optional) The OCID of the listing.

`ListingResourceVersion` - (Optional) Listing resource version.

`OracleTermsOfUseLink` - (Optional) Oracle TOU link.

`Signature` - (Optional) A generated signature for this listing resource version retrieved the agreements API.

`TimeRetrieved` - (Optional) Date and time the agreements were retrieved, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`.


## Return Values

### Fn::GetAtt

`ListingId` - The ocid of the listing resource.

`DisplayName` - The display name of the listing.

`ListingResourceVersion` - Listing resource version.

`CompartmentId` - The compartmentID of the subscription.

`TimeCreated` - Date and time at which the subscription was created, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`.

`Summary` - The short summary to the listing.

`ListingResourceId` - Listing resource id.

`PublisherName` - Name of the publisher who published this listing.

## See Also

* [oci_core_app_catalog_subscription](https://www.terraform.io/docs/providers/oci/r/core_app_catalog_subscription.html) in the _Terraform Provider Documentation_