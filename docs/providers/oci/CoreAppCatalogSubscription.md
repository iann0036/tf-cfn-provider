# Terraform::OCI::CoreAppCatalogSubscription

This resource provides the App Catalog Subscription resource in Oracle Cloud Infrastructure Core service.

Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The compartmentID of the subscription.

`DisplayName` - The display name of the listing.

`ListingId` - The ocid of the listing resource.

`ListingResourceId` - Listing resource id.

`ListingResourceVersion` - Listing resource version.

`PublisherName` - Name of the publisher who published this listing.

`Summary` - The short summary to the listing.

`TimeCreated` - Date and time at which the subscription was created, in RFC3339 format. Example: `2018-03-20T12:32:53.532Z`.

## See Also

* [oci_core_app_catalog_subscription](https://www.terraform.io/docs/providers/oci/r/core_app_catalog_subscription.html) in the _Terraform Provider Documentation_