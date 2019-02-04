# Terraform::Google::ComputeNetwork

Manages a network within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

## Properties

`Name` - (Required) A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

`AutoCreateSubnetworks` - (Optional) If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support `Terraform::Google::ComputeSubnetwork` resources. Defaults to true.

`Ipv4Range` - (Optional) If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, `AutoCreateSubnetworks` must be
explicitly set to false.

`RoutingMode` - (Optional) Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are `"GLOBAL"` or `"REGIONAL"`. Defaults to `"REGIONAL"`.
Refer to the [Cloud Router documentation](https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode)
for more details.

`Description` - (Optional) A brief description of this resource.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.


## Return Values

### Fn::GetAtt

`GatewayIpv4` - The IPv4 address of the gateway.

`Name` - The unique name of the network.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_network](https://www.terraform.io/docs/providers/google/r/compute_network.html) in the _Terraform Provider Documentation_