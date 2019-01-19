# Terraform::AzureRM::CosmosdbAccount

Manages a CosmosDB (formally DocumentDB) Account.

## Properties

`Name` - (Required) The capability to enable - Possible values are `EnableTable`, `EnableCassandra`, and `EnableGremlin`.

`ResourceGroupName` - (Required) The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

`Location` - (Required) The name of the Azure region to host replicated data.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`OfferType` - (Required) Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

`Kind` - (Optional) Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

`ConsistencyPolicy` - (Required) Specifies a `ConsistencyPolicy` resource, used to define the consistency policy for this CosmosDB account.

`GeoLocation` - (Required) Specifies a `GeoLocation` resource, used to define where data should be replicated with the `FailoverPriority` 0 specifying the primary location.

`IpRangeFilter` - (Optional) CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

`EnableAutomaticFailover` - (Optional) Enable automatic fail over for this Cosmos DB account.

`Capabilities` - (Optional) Enable capabilities for this Cosmos DB account.

`IsVirtualNetworkFilterEnabled` - (Optional) Enables virtual network filtering for this Cosmos DB account.

`VirtualNetworkRule` - (Optional) Specifies a `virtual_network_rules` resource, used to define which subnets are allowed to access this CosmosDB account.

`EnableMultipleWriteLocations` - (Optional) Enable multi-master support for this Cosmos DB account.

`ConsistencyLevel` - (Required) The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.

`MaxIntervalInSeconds` - (Optional) When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `ConsistencyLevel` is set to `BoundedStaleness`.

`MaxStalenessPrefix` - (Optional) When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `ConsistencyLevel` is set to `BoundedStaleness`.

`Prefix` - (Optional) The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.

`FailoverPriority` - (Required) The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.

`Id` - (Required) The ID of the virtual network subnet.


## Return Values

### Fn::GetAtt

`Id` - The CosmosDB Account ID.

`Endpoint` - The endpoint used to connect to the CosmosDB account.

`ReadEndpoints` - A list of read endpoints available for this CosmosDB account.

`WriteEndpoints` - A list of write endpoints available for this CosmosDB account.

`PrimaryMasterKey` - The Primary master key for the CosmosDB Account.

`SecondaryMasterKey` - The Secondary master key for the CosmosDB Account.

`PrimaryReadonlyMasterKey` - The Primary read-only master Key for the CosmosDB Account.

`SecondaryReadonlyMasterKey` - The Secondary read-only master key for the CosmosDB Account.

`ConnectionStrings` - A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.

## See Also

* [azurerm_cosmosdb_account](https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account.html) in the _Terraform Provider Documentation_