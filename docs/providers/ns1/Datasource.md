# Terraform::NS1::Datasource

Provides a NS1 Data Source resource. This can be used to create, modify, and delete data sources.

## Properties

`Name` - (Required) The free form name of the data source.

`Sourcetype` - (Required) The data sources type, listed in API endpoint https://api.nsone.net/v1/data/sourcetypes.

`Config` - (Optional) The data source configuration, determined by its type.


## See Also

* [ns1_datasource](https://www.terraform.io/docs/providers/ns1/r/datasource.html) in the _Terraform Provider Documentation_