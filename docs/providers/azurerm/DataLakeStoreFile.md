# Terraform::AzureRM::DataLakeStoreFile

Manage a Azure Data Lake Store File.

~> **Note:** If you want to change the data in the remote file without changing the `LocalFilePath`, then 
taint the resource so the `Terraform::AzureRM::DataLakeStoreFile` gets recreated with the new data.

## Properties

`AccountName` - (Required) Specifies the name of the Data Lake Store for which the File should created.

`LocalFilePath` - (Required) The path to the local file to be added to the Data Lake Store.

`RemoteFilePath` - (Required) The path created for the file on the Data Lake Store.


## See Also

* [azurerm_data_lake_store_file](https://www.terraform.io/docs/providers/azurerm/r/data_lake_store_file.html) in the _Terraform Provider Documentation_