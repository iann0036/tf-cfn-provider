# Terraform::Google::ComputeNetwork

Manages a network within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`GatewayIpv4` - The IPv4 address of the gateway.

`Name` - The unique name of the network.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_network](https://www.terraform.io/docs/providers/google/r/compute_network.html) in the _Terraform Provider Documentation_