# Terraform::Google::ServiceNetworkingConnection

~> **Warning:** This resource is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta resources.

Manages a private VPC connection with a GCP service provider. For more information see
[the official documentation](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection)
and
[API](https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections).

## Properties

`Network` - (Required) Name of VPC network connected with service producers using VPC peering.

`Service` - (Required) Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
'servicenetworking.googleapis.com'.

`ReservedPeeringRanges` - (Required) Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.


## See Also

* [google_service_networking_connection](https://www.terraform.io/docs/providers/google/r/service_networking_connection.html) in the _Terraform Provider Documentation_