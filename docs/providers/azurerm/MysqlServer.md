# Terraform::AzureRM::MysqlServer

Manages a MySQL Server.

## Properties

`Name` - (Required) Specifies the name of the MySQL Server. Changing this forces a new resource to be created. This needs to be globally unique within Azure.

`ResourceGroupName` - (Required) The name of the resource group in which to create the MySQL Server. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`StorageProfile` - (Required) A `StorageProfile` block as defined below.

`AdministratorLogin` - (Required) The Administrator Login for the MySQL Server. Changing this forces a new resource to be created.

`AdministratorLoginPassword` - (Required) The Password associated with the `AdministratorLogin` for the MySQL Server.

`Version` - (Required) Specifies the version of MySQL to use. Valid values are `5.6` and `5.7`. Changing this forces a new resource to be created.

`SslEnforcement` - (Required) Specifies if SSL should be enforced on connections. Possible values are `Enabled` and `Disabled`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Required) Specifies the SKU Name for this MySQL Server. The name of the SKU, follows the `Tier` + `Family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#sku).

`Capacity` - (Required) The scale up/out capacity, representing server's compute units.

`Tier` - (Required) The tier of the particular SKU. Possible values are `Basic`, `GeneralPurpose`, and `MemoryOptimized`. For more information see the [product documentation](https://docs.microsoft.com/en-us/azure/mysql/concepts-pricing-tiers).

`Family` - (Required) The `Family` of hardware `Gen4` or `Gen5`, before selecting your `Family` check the [product documentation](https://docs.microsoft.com/en-us/azure/mysql/concepts-pricing-tiers#compute-generations-vcores-and-memory) for availability in your region.

### StorageProfile Properties

`StorageMb` - (Required) Max storage allowed for a server. Possible values are between `5120` MB(5GB) and `1048576` MB(1TB) for the Basic SKU and between `5120` MB(5GB) and `4194304` MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#StorageProfile).

`BackupRetentionDays` - (Optional) Backup retention days for the server, supported values are between `7` and `35` days.

`GeoRedundantBackup` - (Optional) Enable Geo-redundant or not for server backup. Valid values for this property are `Enabled` or `Disabled`, not supported for the `basic` tier.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MySQL Server.

`Fqdn` - The FQDN of the MySQL Server.

## See Also

* [azurerm_mysql_server](https://www.terraform.io/docs/providers/azurerm/r/mysql_server.html) in the _Terraform Provider Documentation_