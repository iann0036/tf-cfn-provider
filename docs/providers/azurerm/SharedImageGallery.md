# Terraform::AzureRM::SharedImageGallery

Manages a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

## Properties

`Name` - (Required) Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Description` - (Optional) A description for this Shared Image Gallery.

`Tags` - (Optional) A mapping of tags to assign to the Shared Image Gallery.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Shared Image Gallery.

## See Also

* [azurerm_shared_image_gallery](https://www.terraform.io/docs/providers/azurerm/r/shared_image_gallery.html) in the _Terraform Provider Documentation_