# Terraform::AzureRM::DataLakeAnalyticsAccount

Manage an Azure Data Lake Analytics Account.

## Properties

`Name` - (Required) Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Data Lake Analytics Account.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`DefaultStoreAccountName` - (Required) Specifies the data lake store to use by default. Changing this forces a new resource to be created.

`Tier` - (Optional) The monthly commitment tier for Data Lake Analytics Account. Accepted values are `Consumption`, `Commitment_100000AUHours`, `Commitment_10000AUHours`, `Commitment_1000AUHours`, `Commitment_100AUHours`, `Commitment_500000AUHours`, `Commitment_50000AUHours`, `Commitment_5000AUHours`, or `Commitment_500AUHours`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Date Lake Store ID.

## See Also

* [azurerm_data_lake_analytics_account](https://www.terraform.io/docs/providers/azurerm/r/data_lake_analytics_account.html) in the _Terraform Provider Documentation_