# Terraform::AzureRM::DataLakeStoreFile

Manage a Azure Data Lake Store File.

~> **Note:** If you want to change the data in the remote file without changing the `local_file_path`, then 
taint the resource so the `azurerm_data_lake_store_file` gets recreated with the new data.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [azurerm_data_lake_store_file](https://www.terraform.io/docs/providers/azurerm/r/data_lake_store_file.html) in the _Terraform Provider Documentation_