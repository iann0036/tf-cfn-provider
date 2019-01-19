# Terraform::OpenStack::DbConfigurationV1

Manages a V1 DB configuration resource within OpenStack.

## Properties

`Region` - (Required) The region in which to create the db instance. Changing this creates a new instance.

`Name` - (Required) A unique name for the resource.

`Description` - (Optional) Description of the resource.

`Datastore` - (Required) An array of database engine type and version. The datastore object structure is documented below. Changing this creates resource.

`Configuration` - (Optional) An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

### Datastore Properties

`Type` - (Required) Database engine type to be used with this configuration. Changing this creates a new resource.

`Version` - (Required) Version of database engine type to be used with this configuration. Changing this creates a new resource.

### Configuration Properties

`Name` - (Optional) Configuration parameter name. Changing this creates a new resource.

`Value` - (Optional) Configuration parameter value. Changing this creates a new resource.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Datastore/type` - See Properties above.

`Datastore/version` - See Properties above.

`Configuration/name` - See Properties above.

`Configuration/value` - See Properties above.

## See Also

* [openstack_db_configuration_v1](https://www.terraform.io/docs/providers/openstack/r/db_configuration_v1.html) in the _Terraform Provider Documentation_