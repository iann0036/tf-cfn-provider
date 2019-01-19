# Terraform::AzureRM::LbProbe

Manages a LoadBalancer Probe Resource.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the Probe.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the LoadBalancer in which to create the NAT Rule.

`Protocol` - (Optional) Specifies the protocol of the end point. Possible values are `Http`, `Https` or `Tcp`. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.

`Port` - (Required) Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.

`RequestPath` - (Optional) The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.

`IntervalInSeconds` - (Optional) The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.

`NumberOfProbes` - (Optional) The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurerm_lb_probe](https://www.terraform.io/docs/providers/azurerm/r/lb_probe.html) in the _Terraform Provider Documentation_