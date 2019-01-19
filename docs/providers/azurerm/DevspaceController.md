# Terraform::AzureRM::DevspaceController

Manages a DevSpace Controller.

## Properties

`ResourceGroupName` - (Required) The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as documented below. Changing this forces a new resource to be created.

`HostSuffix` - (Required) The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.

`TargetContainerHostResourceId` - (Required) The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

`TargetContainerHostCredentialsBase64` - (Required) Base64 encoding of `kube_config_raw` of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Required) The name of the SKU for DevSpace Controller. Currently the only supported value is `S1`. Changing this forces a new resource to be created.

`Tier` - (Required) The tier of the SKU for DevSpace Controller. Currently the only supported value is `Standard`. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the DevSpace Controller.

`DataPlaneFqdn` - DNS name for accessing DataPlane services.

## See Also

* [azurerm_devspace_controller](https://www.terraform.io/docs/providers/azurerm/r/devspace_controller.html) in the _Terraform Provider Documentation_