# Terraform::VCD::CatalogItem

Provides a vCloud Director catalog item resource. This can be used to upload OVA to catalog and delete it.

Supported in provider *v2.0+*

## Properties

`Org` - (Optional) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Catalog` - (Required) The name of the catalog where to upload OVA file.

`Name` - (Required) Item name in catalog.

`Description` - (Optional) - Description of item.

`OvaPath` - (Required) - Absolute or relative path to file to upload.

`UploadPieceSize` - (Optional) - Size in MB for splitting upload size. It can possibly impact upload performance. Default 1MB.

`ShowUploadProgress` - (Optional) - Default false. Allows to see upload progress.


## See Also

* [vcd_catalog_item](https://www.terraform.io/docs/providers/vcd/r/catalog_item.html) in the _Terraform Provider Documentation_