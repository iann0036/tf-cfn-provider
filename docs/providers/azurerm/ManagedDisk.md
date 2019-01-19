# Terraform::AzureRM::ManagedDisk

Manage a managed disk.

## Properties

`Name` - (Required) Specifies the name of the managed disk. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the managed disk.

`Location` - (Required) Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`StorageAccountType` - (Required) The type of storage to use for the managed disk. Allowable values are `Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS` or `UltraSSD_LRS`.

`CreateOption` - (Required) The method to use when creating the managed disk. Possible values include: * `Import` - Import a VHD file in to the managed disk (VHD specified with `SourceUri`). * `Empty` - Create an empty managed disk. * `Copy` - Copy an existing managed disk or snapshot (specified with `SourceResourceId`). * `FromImage` - Copy a Platform Image (specified with `ImageReferenceId`).

`Import` - Import a VHD file in to the managed disk (VHD specified with `SourceUri`). * `Empty` - Create an empty managed disk. * `Copy` - Copy an existing managed disk or snapshot (specified with `SourceResourceId`). * `FromImage` - Copy a Platform Image (specified with `ImageReferenceId`).

`Empty` - Create an empty managed disk. * `Copy` - Copy an existing managed disk or snapshot (specified with `SourceResourceId`). * `FromImage` - Copy a Platform Image (specified with `ImageReferenceId`).

`Copy` - Copy an existing managed disk or snapshot (specified with `SourceResourceId`). * `FromImage` - Copy a Platform Image (specified with `ImageReferenceId`).

`FromImage` - Copy a Platform Image (specified with `ImageReferenceId`).

`SourceUri` - (Optional) URI to a valid VHD file to be used when `CreateOption` is `Import`.

`SourceResourceId` - (Optional) ID of an existing managed disk to copy when `CreateOption` is `Copy`.

`ImageReferenceId` - (Optional) ID of an existing platform/marketplace disk image to copy when `CreateOption` is `FromImage`.

`OsType` - (Optional) Specify a value when the source of an `Import` or `Copy` operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`.

`DiskSizeGb` - (Optional, Required for a new managed disk) Specifies the size of the managed disk to create in gigabytes. If `CreateOption` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

`EncryptionSettings` - (Optional) an `EncryptionSettings` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Zones` - (Optional) A collection containing the availability zone to allocate the Managed Disk in.

`Enabled` - (Required) Is Encryption enabled on this Managed Disk? Changing this forces a new resource to be created.

`DiskEncryptionKey` - (Optional) A `DiskEncryptionKey` block as defined below.

`KeyEncryptionKey` - (Optional) A `KeyEncryptionKey` block as defined below.

`SecretUrl` - (Required) The URL to the Key Vault Secret used as the Disk Encryption Key. This can be found as `id` on the `Terraform::AzureRM::KeyVaultSecret` resource.

`SourceVaultId` - (Required) The URL of the Key Vault. This can be found as `vault_uri` on the `Terraform::AzureRM::KeyVault` resource.

`KeyUrl` - (Required) The URL to the Key Vault Key used as the Key Encryption Key. This can be found as `id` on the `Terraform::AzureRM::KeyVaultSecret` resource.


## Return Values

### Fn::GetAtt

`Id` - The managed disk ID.

## See Also

* [azurerm_managed_disk](https://www.terraform.io/docs/providers/azurerm/r/managed_disk.html) in the _Terraform Provider Documentation_