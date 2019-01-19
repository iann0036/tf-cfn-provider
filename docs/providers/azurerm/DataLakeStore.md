# Terraform::AzureRM::DataLakeStore

Manage an Azure Data Lake Store.

## Properties

`Name` - (Required) Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Data Lake Store.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tier` - (Optional) The monthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

`EncryptionState` - (Optional) Is Encryption enabled on this Data Lake Store Account? Possible values are `Enabled` or `Disabled`. Defaults to `Enabled`.

`EncryptionType` - (Optional) The Encryption Type used for this Data Lake Store Account. Currently can be set to `SystemManaged` when `EncryptionState` is `Enabled` - and must be a blank string when it's Disabled.

`FirewallAllowAzureIps` - are Azure Service IP's allowed through the firewall? Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`.

`FirewallState` - the state of the Firewall. Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Date Lake Store ID.

`Endpoint` - The Endpoint for the Data Lake Store.

## See Also

* [azurerm_data_lake_store](https://www.terraform.io/docs/providers/azurerm/r/data_lake_store.html) in the _Terraform Provider Documentation_