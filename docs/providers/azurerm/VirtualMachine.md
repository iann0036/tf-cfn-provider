# Terraform::AzureRM::VirtualMachine

Manages a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `Terraform::AzureRM::VirtualMachine` resource, or using the `azurermVirtualMachineDataDiskAttachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

## Properties

`ResourceGroupName` - (Required) Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.

`NetworkInterfaceIds` - (Required) A list of Network Interface ID's which should be associated with the Virtual Machine.

`OsProfileLinuxConfig` - (Required, when a Linux machine) A `OsProfileLinuxConfig` block.

`OsProfileWindowsConfig` - (Required, when a Windows machine) A `OsProfileWindowsConfig` block.

`VmSize` - (Required) Specifies the [size of the Virtual Machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

`AvailabilitySetId` - (Optional) The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

`BootDiagnostics` - (Optional) A `BootDiagnostics` block.

`DeleteOsDiskOnTermination` - (Optional) Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

`DeleteDataDisksOnTermination` - (Optional) Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

`Identity` - (Optional) A `Identity` block.

`LicenseType` - (Optional) Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are `Windows_Client` and `Windows_Server`.

`OsProfile` - (Optional) An `OsProfile` block. Required when `CreateOption` in the `StorageOsDisk` block is set to `FromImage`.

`OsProfileSecrets` - (Optional) One or more `OsProfileSecrets` blocks.

`Plan` - (Optional) A `Plan` block.

`PrimaryNetworkInterfaceId` - (Optional) The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.

`StorageDataDisk` - (Optional) One or more `StorageDataDisk` blocks.

`StorageImageReference` - (Optional) A `StorageImageReference` block.

`StorageOsDisk` - (Required) A `StorageOsDisk` block.

`Tags` - (Optional) A mapping of tags to assign to the Virtual Machine.

`Zones` - (Optional) A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.

`Pass` - (Required) Specifies the name of the pass that the content applies to. The only allowable value is `oobeSystem`.

`Component` - (Required) Specifies the name of the component to configure with the added content. The only allowable value is `Microsoft-Windows-Shell-Setup`.

`SettingName` - (Required) Specifies the name of the setting to which the content applies. Possible values are: `FirstLogonCommands` and `AutoLogon`.

`Content` - (Optional) Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.

### OsProfileWindowsConfig Properties

`ProvisionVmAgent` - (Optional) Should the Azure Virtual Machine Guest Agent be installed on this Virtual Machine? Defaults to `false`.

`EnableAutomaticUpgrades` - (Optional) Are automatic updates enabled on this Virtual Machine? Defaults to `false.`.

`Timezone` - (Optional) Specifies the time zone of the virtual machine, [the possible values are defined here](http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).

`Winrm` - (Optional) One or more `Winrm` block.

`AdditionalUnattendConfig` - (Optional) A `AdditionalUnattendConfig` block.

### StorageDataDisk Properties

`Lun` - (Required) Specifies the logical unit number of the data disk. This needs to be unique within all the Data Disks on the Virtual Machine.

### OsProfile Properties

`ComputerName` - (Required) Specifies the name of the Virtual Machine.

`AdminUsername` - (Required) Specifies the name of the local administrator account.

`AdminPassword` - (Required for Windows, Optional for Linux) The password associated with the local administrator account.

`CustomData` - (Optional) Specifies custom data to supply to the machine. On Linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, Terraform will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.

### Winrm Properties

`CertificateUrl` - (Optional) The ID of the Key Vault Secret which contains the encrypted Certificate which should be installed on the Virtual Machine. This certificate must also be specified in the `VaultCertificates` block within the `OsProfileSecrets` block.

`Protocol` - (Required) Specifies the protocol of listener. Possible values are `HTTP` or `HTTPS`.

### CertificateUrl Properties

`CertificateStore` - (Required, on windows machines) Specifies the certificate store on the Virtual Machine where the certificate should be added to, such as `My`.

### OsProfileLinuxConfig Properties

`DisablePasswordAuthentication` - (Required) Specifies whether password authentication should be disabled. If set to `false`, an `AdminPassword` must be specified.

`SshKeys` - (Optional) One or more `SshKeys` blocks. This field is required if `DisablePasswordAuthentication` is set to `true`.

### StorageOsDisk Properties

`Name` - (Required) Specifies the name of the OS Disk.

`Caching` - (Optional) Specifies the caching requirements for the OS Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

`CreateOption` - (Required) Specifies how the OS Disk should be created. Possible values are `Attach` (managed disks only) and `FromImage`.

`DiskSizeGb` - (Optional) Specifies the size of the OS Disk in gigabytes.

`WriteAcceleratorEnabled` - (Optional) Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.

`ManagedDiskType` - (Optional) Specifies the type of Managed Disk which should be created. Possible values are `Standard_LRS`, `StandardSSD_LRS` or `Premium_LRS`.

`ManagedDiskId` - (Optional) Specifies the ID of an existing Managed Disk which should be attached as the OS Disk of this Virtual Machine. If this is set then the `CreateOption` must be set to `Attach`.

`VhdUri` - (Optional) Specifies the URI of the VHD file backing this Unmanaged OS Disk. Changing this forces a new resource to be created.

`ImageUri` - (Optional) Specifies the Image URI in the format `publisherName:offer:skus:version`. This field can also specify the [VHD uri](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image) of a custom VM image to clone. When cloning a Custom (Unmanaged) Disk Image the `OsType` field must be set.

`OsType` - (Optional) Specifies the Operating System on the OS Disk. Possible values are `Linux` and `Windows`.

### OsProfileSecrets Properties

`SourceVaultId` - (Required) Specifies the ID of the Key Vault to use.

`VaultCertificates` - (Required) One or more `VaultCertificates` blocks.

### SshKeys Properties

`KeyData` - (Required) The Public SSH Key which should be written to the `Path` defined above.

`Path` - (Required) The path of the destination file on the virtual machine.

### StorageImageReference Properties

`Publisher` - (Required) Specifies the publisher of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Offer` - (Required) Specifies the offer of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Sku` - (Required) Specifies the SKU of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Version` - (Optional) Specifies the version of the image used to create the virtual machine. Changing this forces a new resource to be created.

`Id` - (Required) Specifies the ID of the Custom Image which the Virtual Machine should be created from. Changing this forces a new resource to be created.

### Identity Properties

`Type` - (Required) The Managed Service Identity Type of this Virtual Machine. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` (where you can specify the Service Principal ID's) to be used by this Virtual Machine using the `IdentityIds` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.

`IdentityIds` - (Optional) Specifies a list of user managed identity ids to be assigned to the VM. Required if `Type` is `UserAssigned`.

### BootDiagnostics Properties

`Enabled` - (Required) Should Boot Diagnostics be enabled for this Virtual Machine?.

`StorageUri` - (Required) The Storage Account's Blob Endpoint which should hold the virtual machine's diagnostic files.

### Plan Properties

`Product` - (Required) Specifies the product of the image from the marketplace.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Machine.

## See Also

* [azurerm_virtual_machine](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine.html) in the _Terraform Provider Documentation_