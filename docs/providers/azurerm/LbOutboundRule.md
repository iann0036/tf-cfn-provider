# Terraform::AzureRM::LbOutboundRule

Manages a Load Balancer Outbound Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration and a Backend Address Pool Attached.

## Properties

`Name` - (Required) Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

`LoadbalancerId` - (Required) The ID of the Load Balancer in which to create the Outbound Rule. Changing this forces a new resource to be created.

`FrontendIpConfiguration` - (Required) One or more `FrontendIpConfiguration` blocks as defined below.

`BackendAddressPoolId` - (Required) The ID of the Backend Address Pool. Outbound traffic is randomly load balanced across IPs in the backend IPs.

`Protocol` - (Required) The transport protocol for the external endpoint. Possible values are `Udp`, `Tcp` or `All`.

`EnableTcpReset` - (Optional) Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.

`AllocatedOutboundPorts` - (Optional) The number of outbound ports to be used for NAT.

`IdleTimeoutInMinutes` - (Optional) The timeout for the TCP idle connection.

### FrontendIpConfiguration Properties

`Name` - (Required) The name of the Frontend IP Configuration.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurerm_lb_outbound_rule](https://www.terraform.io/docs/providers/azurerm/r/lb_outbound_rule.html) in the _Terraform Provider Documentation_