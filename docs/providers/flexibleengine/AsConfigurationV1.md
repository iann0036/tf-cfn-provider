# Terraform::FlexibleEngine::AsConfigurationV1

Manages a V1 AS Configuration resource within flexibleengine.

## Properties

`Region` - (Optional) The region in which to create the AS configuration. If omitted, the `Region` argument of the provider is used. Changing this creates a new AS configuration.

`ScalingConfigurationName` - (Required) The name of the AS configuration. The name can contain letters, digits, underscores(_), and hyphens(-), and cannot exceed 64 characters.

`InstanceConfig` - (Required) The information about instance configurations. The instance_config dictionary data structure is documented below.

`InstanceId` - (Optional) When using the existing instance specifications as the template to create AS configurations, specify this argument. In this case, flavor, image, and disk arguments do not take effect. If the instance_id argument is not specified, flavor, image, and disk arguments are mandatory.

`Flavor` - (Optional) The flavor ID.

`Image` - (Optional) The image ID.

`Disk` - (Optional) The disk group information. System disks are mandatory and data disks are optional. The dick structure is described below.

`KeyName` - (Required) The name of the SSH key pair used to log in to the instance.

`UserData` - (Optional) The user data to provide when launching the instance. The file content must be encoded with Base64.

`Personality` - (Optional) Customize the personality of an instance by defining one or more files and their contents. The personality structure is described below.

`PublicIp` - (Optional) The elastic IP address of the instance. The public_ip structure is described below.

`Metadata` - (Optional) Metadata key/value pairs to make available from within the instance.

`Size` - (Required) The bandwidth (Mbit/s). The value range is 1 to 300.

`VolumeType` - (Required) The disk type, which must be the same as the disk type available in the system. The options include `SATA` (common I/O disk type) and `SSD` (ultra-high I/O disk type).

`DiskType` - (Required) Whether the disk is a system disk or a data disk. Option `DATA` indicates a data disk. option `SYS` indicates a system disk.

`Path` - (Required) The absolute path of the destination file.

`Contents` - (Required) The content of the injected file, which must be encoded with base64.

`Eip` - (Required) The configuration parameter for creating an elastic IP address that will be automatically assigned to the instance. The eip structure is described below.

`IpType` - (Required) The IP address type. The system only supports `5_bgp` (indicates dynamic BGP).

`Bandwidth` - (Required) The bandwidth information. The structure is described below.

`ShareType` - (Required) The bandwidth sharing type. The system only supports `PER` (indicates exclusive bandwidth).

`ChargingMode` - (Required) The bandwidth charging mode. The system only supports `traffic`.


## See Also

* [flexibleengine_as_configuration_v1](https://www.terraform.io/docs/providers/flexibleengine/r/as_configuration_v1.html) in the _Terraform Provider Documentation_