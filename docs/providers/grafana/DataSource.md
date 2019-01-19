# Terraform::Grafana::DataSource

The data source resource allows a data source to be created on a Grafana server.

## Properties

`Type` - (Required) The data source type. Must be one of the data source keywords supported by the Grafana server.

`Name` - (Required) A unique name for the data source within the Grafana server.

`Url` - (Optional) The URL for the data source. The type of URL required varies depending on the chosen data source type.

`IsDefault` - (Optional) If true, the data source will be the default source used by the Grafana server. Only one data source on a server can be the default.

`BasicAuthEnabled` - (Optional) - If true, HTTP basic authentication will be used to make requests.

`BasicAuthUsername` - (Required if `BasicAuthEnabled` is true) The username to use for basic auth.

`BasicAuthPassword` - (Required if `BasicAuthEnabled` is true) The password to use for basic auth.

`Username` - (Required by some data source types) The username to use to authenticate to the data source.

`Password` - (Required by some data source types) The password to use to authenticate to the data source.

`JsonData` - (Required by some data source types) The default region and authentication type to access the data source. `JsonData` is documented in more detail below.

`SecureJsonData` - (Required by some data source types) The access and secret keys required to access the data source. `SecureJsonData` is documented in more detail below.

`DatabaseName` - (Required by some data source types) The name of the database to use on the selected data source server.

`AccessMode` - (Optional) The method by which the browser-based Grafana application will access the data source. The default is "proxy", which means that the application will make requests via a proxy endpoint on the Grafana server.

### SecureJsonData Properties

`AccessKey` - (Required by some data source types) The access key required to access the data source.

`SecretKey` - (Required by some data source types) The secret key required to access the data source.

### JsonData Properties

`AuthType` - (Required by some data source types) The authentication type type used to access the data source.

`Default` - (Required by some data source types) The default region for the data source.

`CustomMetricsNamespaces` - (Optional, for the CloudWatch data source type) A comma-separated list of custom namespaces to be queried by the CloudWatch data source.

`AssumeRoleArn` - (Optional, for the CloudWatch data source type) The role ARN to be assumed by Grafana when using the CloudWatch data source.


## Return Values

### Fn::GetAtt

`Id` - The opaque unique id assigned to the data source by the Grafana.

## See Also

* [grafana_data_source](https://www.terraform.io/docs/providers/grafana/r/data_source.html) in the _Terraform Provider Documentation_