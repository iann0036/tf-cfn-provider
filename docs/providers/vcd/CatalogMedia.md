# Terraform::VCD::CatalogMedia

Provides a vCloud Director resource for inserting or ejecting media (ISO) file for the VM. Create this resource for inserting the media, and destroy it for ejecting.

Supported in provider *v2.0+*

## Properties

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.

`Catalog` - (Required) The name of the catalog where to find media file.

`Name` - (Required) Media file name in catalog which will be inserted to VM.

`VappName` - (Required) - The name of vApp to find.

`VmName` - (Required) - The name of VM to be used to insert media file.


## See Also

* [vcd_catalog_media](https://www.terraform.io/docs/providers/vcd/r/catalog_media.html) in the _Terraform Provider Documentation_