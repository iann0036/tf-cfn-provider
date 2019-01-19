# Terraform::OneAndOne::BlockStorage

Manages a Block Storage on 1&1

## Properties

`Datacenter` - (Optional) Location of desired 1and1 datacenter, where the block storage will be created. Can be `DE`, `GB`, `US` or `ES`.

`Description` - (Optional) Description for the block storage.

`Name` - (Required) The name of the storage.

`ServerId` - (Optional) ID of the server that the block storage will be attached to.

`Size` - (Required) Size of the block storage (`min: 20, max: 500, multipleOf: 10`).


## See Also

* [oneandone_block_storage](https://www.terraform.io/docs/providers/oneandone/r/block_storage.html) in the _Terraform Provider Documentation_