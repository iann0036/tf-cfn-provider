# Terraform::AzureRM::SharedImageVersion

Manages a Version of a Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

## Properties

`Name` - (Required) The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.

`GalleryName` - (Required) The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.

`ImageName` - (Required) The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.

`Location` - (Required) The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

`ManagedImageId` - (Required) The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.

`TargetRegion` - (Required) One or more `TargetRegion` blocks as documented below.

`ExcludeFromLatest` - (Optional) Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.

`Tags` - (Optional) A collection of tags which should be applied to this resource.

### TargetRegion Properties

`Name` - (Required) The Azure Region in which this Image Version should exist.

`RegionalReplicaCount` - (Required) The number of replicas of the Image Version to be created per region.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Shared Image Version.

## See Also

* [azurerm_shared_image_version](https://www.terraform.io/docs/providers/azurerm/r/shared_image_version.html) in the _Terraform Provider Documentation_