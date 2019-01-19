# Terraform::OpenStack::DbInstanceV1

Manages a V1 DB instance resource within OpenStack.

## Properties

`Region` - (Required) The region in which to create the db instance. Changing this creates a new instance.

`Name` - (Required) A unique name for the resource.

`FlavorId` - (Required) The flavor ID of the desired flavor for the instance. Changing this creates new instance.

`ConfigurationId` - (Optional) Configuration ID to be attached to the instance. Database instance will be rebooted when configuration is detached.

`Size` - (Required) Specifies the volume size in GB. Changing this creates new instance.

`Datastore` - (Required) An array of database engine type and version. The datastore object structure is documented below. Changing this creates a new instance.

`Network` - (Optional) An array of one or more networks to attach to the instance. The network object structure is documented below. Changing this creates a new instance.

`User` - (Optional) An array of username, password, host and databases. The user object structure is documented below.

`Database` - (Optional) An array of database name, charset and collate. The database object structure is documented below.

### Datastore Properties

`Type` - (Required) Database engine type to be used in new instance. Changing this creates a new instance.

`Version` - (Required) Version of database engine type to be used in new instance. Changing this creates a new instance.

### Network Properties

`Uuid` - (Required unless `Port` is provided) The network UUID to attach to the instance. Changing this creates a new instance.

`Port` - (Required unless `Uuid` is provided) The port UUID of a network to attach to the instance. Changing this creates a new instance.

`FixedIpV4` - (Optional) Specifies a fixed IPv4 address to be used on this network. Changing this creates a new instance.

`FixedIpV6` - (Optional) Specifies a fixed IPv6 address to be used on this network. Changing this creates a new instance.

### User Properties

`Name` - (Optional) Username to be created on new instance. Changing this creates a new instance.

`Password` - (Optional) User's password. Changing this creates a new instance.

`Host` - (Optional) An ip address or % sign indicating what ip addresses can connect with this user credentials. Changing this creates a new instance.

`Databases` - (Optional) A list of databases that user will have access to. If not specified, user has access to all databases on th einstance. Changing this creates a new instance.

### Database Properties

`Name` - (Optional) Database to be created on new instance. Changing this creates a new instance.

`Collate` - (Optional) Database collation. Changing this creates a new instance.

`Charset` - (Optional) Database character set. Changing this creates a new instance.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Size` - See Properties above.

`FlavorId` - See Properties above.

`ConfigurationId` - See Properties above.

`Datastore/type` - See Properties above.

`Datastore/version` - See Properties above.

`Network/uuid` - See Properties above.

`Network/port` - See Properties above.

`Network/fixedIpV4` - The Fixed IPv4 address of the Instance on that.

`Network/fixedIpV6` - The Fixed IPv6 address of the Instance on that.

`Database/name` - See Properties above.

`Database/collate` - See Properties above.

`Database/charset` - See Properties above.

`User/name` - See Properties above.

`User/password` - See Properties above.

`User/databases` - See Properties above.

`User/host` - See Properties above.

## See Also

* [openstack_db_instance_v1](https://www.terraform.io/docs/providers/openstack/r/db_instance_v1.html) in the _Terraform Provider Documentation_