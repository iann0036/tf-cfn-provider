# Terraform::OCI::LoadBalancerHostname

This resource provides the Hostname resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a hostname resource to the specified load balancer. For more information, see
[Managing Request Routing](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Hostname` - A virtual hostname. For more information about virtual hostname string construction, see [Managing Request Routing](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm#routing).  Example: `app.example.com`.

`Name` - A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_hostname_001`.

## See Also

* [oci_load_balancer_hostname](https://www.terraform.io/docs/providers/oci/r/load_balancer_hostname.html) in the _Terraform Provider Documentation_