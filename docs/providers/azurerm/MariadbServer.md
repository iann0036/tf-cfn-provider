# Terraform::AzureRM::MariadbServer

Manages a MariaDB Server.

-> **NOTE** MariaDB Server is currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-us/updates/mariadb-public-preview/).

## Properties

`Name` - (Required) Specifies the SKU Name for this MariaDB Server. The name of the SKU, follows the `Tier` + `Family` + `cores` pattern (e.g. `B_Gen5_1`, `GP_Gen5_8`). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mariadb/servers/create#sku).

`ResourceGroupName` - (Required) The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`StorageProfile` - (Required) A `StorageProfile` block as defined below.

`AdministratorLogin` - (Required) The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.

`AdministratorLoginPassword` - (Required) The Password associated with the `AdministratorLogin` for the MariaDB Server.

`Version` - (Required) Specifies the version of MariaDB to use. The valid value is `10.2`. Changing this forces a new resource to be created.

`SslEnforcement` - (Required) Specifies if SSL should be enforced on connections. Possible values are `Enabled` and `Disabled`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Capacity` - (Required) The scale up/out capacity, representing server's compute units.

`Tier` - (Required) The tier of the particular SKU. Possible values are `Basic`, `GeneralPurpose`, and `MemoryOptimized`. For more information see the [product documentation](https://docs.microsoft.com/en-us/azure/mariadb/concepts-pricing-tiers).

`Family` - (Required) The `Family` of the hardware (e.g. `Gen5`), before selecting your `Family` check the [product documentation](https://docs.microsoft.com/en-us/azure/mariadb/concepts-pricing-tiers#compute-generations-vcores-and-memory) for availability in your region.

`StorageMb` - (Required) Max storage allowed for a server. Possible values are between `5120` MB (5GB) and `1024000`MB (1TB) for the Basic SKU and between `5120` MB (5GB) and `4096000` MB (4TB) for General Purpose/Memory Optimized SKUs. For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mariadb/servers/create#storageprofile).

`BackupRetentionDays` - (Optional) Backup retention days for the server, supported values are between `7` and `35` days.

`GeoRedundantBackup` - (Optional) Enable Geo-redundant or not for server backup. Valid values for this property are `Enabled` or `Disabled`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MariaDB Server.

`Fqdn` - The FQDN of the MariaDB Server.

## See Also

* [azurerm_mariadb_server](https://www.terraform.io/docs/providers/azurerm/r/mariadb_server.html) in the _Terraform Provider Documentation_