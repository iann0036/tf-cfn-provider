# Terraform::AzureRM::Snapshot

Manages a Disk Snapshot.

## Properties

`Name` - (Required) Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`CreateOption` - (Required) Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

`SourceUri` - (Optional) Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

`SourceResourceId` - (Optional) Specifies a reference to an existing snapshot, when `CreateOption` is `Copy`. Changing this forces a new resource to be created.

`StorageAccountId` - (Optional) Specifies the ID of an storage account. Used with `SourceUri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

`DiskSizeGb` - (Optional) The size of the Snapshotted Disk in GB.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Snapshot ID.

`DiskSizeGb` - The Size of the Snapshotted Disk in GB.

## See Also

* [azurerm_snapshot](https://www.terraform.io/docs/providers/azurerm/r/snapshot.html) in the _Terraform Provider Documentation_