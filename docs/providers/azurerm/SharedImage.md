# Terraform::AzureRM::SharedImage

Manages a Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

## Properties

`Name` - (Required) Specifies the name of the Shared Image. Changing this forces a new resource to be created.

`GalleryName` - (Required) Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.

`Identity` - (Required) An `Identity` block as defined below.

`OsType` - (Required) The type of Operating System present in this Shared Image. Possible values are `Linux` and `Windows`.

`Description` - (Optional) A description of this Shared Image.

`Eula` - (Optional) The End User Licence Agreement for the Shared Image.

`PrivacyStatementUri` - (Optional) The URI containing the Privacy Statement associated with this Shared Image.

`ReleaseNoteUri` - (Optional) The URI containing the Release Notes associated with this Shared Image.

`Tags` - (Optional) A mapping of tags to assign to the Shared Image.

`Offer` - (Required) The Offer Name for this Shared Image.

`Publisher` - (Required) The Publisher Name for this Gallery Image.

`Sku` - (Required) The Name of the SKU for this Gallery Image.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Shared Image.

## See Also

* [azurerm_shared_image](https://www.terraform.io/docs/providers/azurerm/r/shared_image.html) in the _Terraform Provider Documentation_