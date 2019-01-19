# Terraform::AzureRM::NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation

Manages the association between a Network Interface and a Application Gateway's Backend Address Pool.

## Properties

`NetworkInterfaceId` - (Required) The ID of the Network Interface. Changing this forces a new resource to be created.

`IpConfigurationName` - (Required) The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.

`BackendAddressPoolId` - (Required) The ID of the Application Gateway's Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The (Terraform specific) ID of the Association between the Network Interface and the Load Balancers Backend Address Pool.

## See Also

* [azurerm_network_interface_application_gateway_backend_address_pool_association](https://www.terraform.io/docs/providers/azurerm/r/network_interface_application_gateway_backend_address_pool_association.html) in the _Terraform Provider Documentation_