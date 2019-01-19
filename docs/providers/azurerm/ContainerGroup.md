# Terraform::AzureRM::ContainerGroup

Manage as an Azure Container Group instance.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`IpAddressType` - (Optional) Specifies the ip address type of the container. `Public` is the only acceptable value at this time. Changing this forces a new resource to be created.

`DnsNameLabel` - (Optional) The DNS label/name for the container groups IP.

`OsType` - (Required) The OS for the container group. Allowed values are `Linux` and `Windows`. Changing this forces a new resource to be created.

`RestartPolicy` - (Optional) Restart policy for the container group. Allowed values are `Always`, `Never`, `OnFailure`. Defaults to `Always`.

`ImageRegistryCredential` - (Optional) Set image registry credentials for the group as documented in the `ImageRegistryCredential` block below.

`Container` - (Required) The definition of a container that is part of the group as documented in the `Container` block below. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### ImageRegistryCredential Properties

`Username` - (Required) The username with which to connect to the registry.

`Password` - (Required) The password with which to connect to the registry.

`Server` - (Required) The address to use to connect to the registry without protocol ("https"/"http"). For example: "myacr.acr.io".

### Volume Properties

`Name` - (Required) The name of the volume mount. Changing this forces a new resource to be created.

`MountPath` - (Required) The path on which this volume is to be mounted. Changing this forces a new resource to be created.

`ReadOnly` - (Optional) Specify if the volume is to be mounted as read only or not. The default value is `false`. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.

`StorageAccountKey` - (Required) The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.

`ShareName` - (Required) The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.

### Ports Properties

`Port` - (Required) The port number the container will expose.

`Protocol` - (Required) The network protocol associated with port. Possible values are `TCP` & `UDP`.

### Container Properties

`Image` - (Required) The container image name. Changing this forces a new resource to be created.

`Cpu` - (Required) The required number of CPU cores of the containers. Changing this forces a new resource to be created.

`Memory` - (Required) The required memory of the containers in GB. Changing this forces a new resource to be created.

`Ports` - (Optional) A set of public ports for the container. Changing this forces a new resource to be created. Set as documented in the `Ports` block below.

`EnvironmentVariables` - (Optional) A list of environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.

`SecureEnvironmentVariables` - (Optional) A list of sensitive environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.

`Command` - (Optional) A command line to be run on the container.

`Commands` - (Optional) A list of commands which should be run on the container.

`Volume` - (Optional) The definition of a volume mount for this container as documented in the `Volume` block below. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The container group ID.

`IpAddress` - The IP address allocated to the container group.

`Fqdn` - The FQDN of the container group derived from `DnsNameLabel`.

## See Also

* [azurerm_container_group](https://www.terraform.io/docs/providers/azurerm/r/container_group.html) in the _Terraform Provider Documentation_