# Terraform::AzureStack::VirtualMachine

Manages a virtual machine.

## Properties

`Name` - (Required) Specifies the name of the data disk.

`ResourceGroupName` - (Required) The name of the resource group in which to create the virtual machine.

`Location` - (Required) Specifies the supported Azure Stack Region where the resource exists. Changing this forces a new resource to be created.

`Plan` - (Optional) A plan block as documented below.

`AvailabilitySetId` - (Optional) The Id of the Availability Set in which to create the virtual machine.

`BootDiagnostics` - (Optional) A boot diagnostics profile block as referenced below.

`VmSize` - (Required) Specifies the [size of the virtual machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

`StorageImageReference` - (Optional) A Storage Image Reference block as documented below.

`StorageOsDisk` - (Required) A `StorageOsDisk` block.

`StorageDataDisk` - (Optional) A list of Storage Data disk blocks as referenced below.

`DeleteDataDisksOnTermination` - (Optional) Flag to enable deletion of storage data disk VHD blobs when the VM is deleted, defaults to `false`.

`OsProfile` - (Optional) An OS Profile block as documented below. Required when `CreateOption` in the `StorageOsDisk` block is set to `FromImage`.

`Identity` - (Optional) An identity block as documented below.

`LicenseType` - (Optional, when a Windows machine) Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

`OsProfileWindowsConfig` - (Required, when a Windows machine) A Windows config block as documented below.

`OsProfileLinuxConfig` - (Required, when a Linux machine) A Linux config block as documented below.

`OsProfileSecrets` - (Optional) A collection of Secret blocks as documented below.

`NetworkInterfaceIds` - (Required) Specifies the list of resource IDs for the network interfaces associated with the virtual machine.

`PrimaryNetworkInterfaceId` - (Optional) Specifies the resource ID for the primary network interface associated with the virtual machine.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Publisher` - (Required, when not using image resource) Specifies the publisher of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Product` - (Required) Specifies the product of the image from the marketplace.

`Id` - (Optional) Specifies the ID of the (custom) image to use to create the virtual machine, for example:.

`Offer` - (Required, when not using image resource) Specifies the offer of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Sku` - (Required, when not using image resource) Specifies the SKU of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Version` - (Optional) Specifies the version of the image used to create the virtual machine. Changing this forces a new resource to be created.

`VhdUri` - (Optional) Specifies the uri of the location in storage where the vhd for the virtual machine should be placed.

`CreateOption` - (Required) Specifies how the data disk should be created. Possible values are `Attach`, `FromImage` and `Empty`.

`Caching` - (Optional) Specifies the caching requirements.

`ImageUri` - (Optional) Specifies the image_uri in the form publisherName:offer:skus:version. `ImageUri` can also specify the [VHD uri](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image) of a custom VM image to clone. When cloning a custom disk image the `OsType` documented below becomes required.

`OsType` - (Optional) Specifies the operating system Type, valid values are windows, linux.

`DiskSizeGb` - (Required) Specifies the size of the data disk in gigabytes.

`Lun` - (Required) Specifies the logical unit number of the data disk.

`ComputerName` - (Required) Specifies the name of the virtual machine.

`AdminUsername` - (Required) Specifies the name of the administrator account.

`AdminPassword` - (Required for Windows, Optional for Linux) Specifies the password of the administrator account.

`CustomData` - (Optional) Specifies custom data to supply to the machine. On linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, Terraform will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.

`Type` - (Required) Specifies the identity type of the virtual machine. The only allowable value is `SystemAssigned`. To enable Managed Service Identity the virtual machine extension "ManagedIdentityExtensionForWindows" or "ManagedIdentityExtensionForLinux" must also be added to the virtual machine. The Principal ID can be retrieved after the virtual machine has been created, e.g.

`ProvisionVmAgent` - (Optional) This value defaults to false.

`EnableAutomaticUpgrades` - (Optional) This value defaults to false.

`Winrm` - (Optional) A collection of WinRM configuration blocks as documented below.

`AdditionalUnattendConfig` - (Optional) An Additional Unattended Config block as documented below.

`Protocol` - (Required) Specifies the protocol of listener.

`CertificateUrl` - (Required) Specifies the URI of the key vault secrets in the format of `https://<vaultEndpoint>/secrets/<secretName>/<secretVersion>`. Stored secret is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be.

`Pass` - (Required) Specifies the name of the pass that the content applies to. The only allowable value is `oobeSystem`.

`Component` - (Required) Specifies the name of the component to configure with the added content. The only allowable value is `Microsoft-Windows-Shell-Setup`.

`SettingName` - (Required) Specifies the name of the setting to which the content applies. Possible values are: `FirstLogonCommands` and `AutoLogon`.

`Content` - (Optional) Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.

`DisablePasswordAuthentication` - (Required) Specifies whether password authentication should be disabled. If set to `false`, an `AdminPassword` must be specified.

`SshKeys` - (Optional) Specifies a collection of `path` and `key_data` to be placed on the virtual machine.

`SourceVaultId` - (Required) Specifies the key vault to use.

`VaultCertificates` - (Required) A collection of Vault Certificates as documented below.

`CertificateStore` - (Required, on windows machines) Specifies the certificate store on the Virtual Machine where the certificate should be added to.


## Return Values

### Fn::GetAtt

`Id` - The virtual machine ID.

## See Also

* [azurestack_virtual_machine](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine.html) in the _Terraform Provider Documentation_