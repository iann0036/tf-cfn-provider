# Terraform::AzureRM::DevTestLinuxVirtualMachine

Manages a Linux Virtual Machine within a Dev Test Lab.

## Properties

`Name` - (Required) Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

`LabName` - (Required) Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

`GalleryImageReference` - (Required) A `GalleryImageReference` block as defined below.

`LabSubnetName` - (Required) The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

`LabVirtualNetworkId` - (Required) The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

`Size` - (Required) The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

`StorageType` - (Required) The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

`Username` - (Required) The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

`AllowClaim` - (Optional) Can this Virtual Machine be claimed by users? Defaults to `true`.

`DisallowPublicIpAddress` - (Optional) Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

`InboundNatRule` - (Optional) One or more `InboundNatRule` blocks as defined below. Changing this forces a new resource to be created.

`Notes` - (Optional) Any notes about the Virtual Machine.

`Password` - (Optional) The Password associated with the `Username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

`SshKey` - (Optional) The SSH Key associated with the `Username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Offer` - (Required) The Offer of the Gallery Image. Changing this forces a new resource to be created.

`Publisher` - (Required) The Publisher of the Gallery Image. Changing this forces a new resource to be created.

`Sku` - (Required) The SKU of the Gallery Image. Changing this forces a new resource to be created.

`Version` - (Required) The Version of the Gallery Image. Changing this forces a new resource to be created.

`Protocol` - (Required) The Protocol used for this NAT Rule. Possible values are `Tcp` and `Udp`. Changing this forces a new resource to be created.

`BackendPort` - (Required) The Backend Port associated with this NAT Rule. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Machine.

`Fqdn` - The FQDN of the Virtual Machine.

`InboundNatRule` - One or more `InboundNatRule` blocks as defined below.

`UniqueIdentifier` - The unique immutable identifier of the Virtual Machine.

`FrontendPort` - The frontend port associated with this Inbound NAT Rule.

## See Also

* [azurerm_dev_test_linux_virtual_machine](https://www.terraform.io/docs/providers/azurerm/r/dev_test_linux_virtual_machine.html) in the _Terraform Provider Documentation_