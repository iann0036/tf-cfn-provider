# Terraform::AzureRM::CosmosdbAccount

Manages a CosmosDB (formally DocumentDB) Account.

## Properties

TBC

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