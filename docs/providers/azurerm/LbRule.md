# Terraform::AzureRM::LbRule

Manages a Load Balancer Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the LB Rule.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the Load Balancer in which to create the Rule.

`FrontendIpConfigurationName` - (Required) The name of the frontend IP configuration to which the rule is associated.

`Protocol` - (Required) The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.

`FrontendPort` - (Required) The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.

`BackendPort` - (Required) The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.

`BackendAddressPoolId` - (Optional) A reference to a Backend Address Pool over which this Load Balancing Rule operates.

`ProbeId` - (Optional) A reference to a Probe used by this Load Balancing Rule.

`EnableFloatingIp` - (Optional) Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

`IdleTimeoutInMinutes` - (Optional) Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

`LoadDistribution` - (Optional) Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurerm_lb_rule](https://www.terraform.io/docs/providers/azurerm/r/lb_rule.html) in the _Terraform Provider Documentation_