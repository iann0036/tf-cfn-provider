# Terraform::OpenStack::DbUserV1

Manages a V1 DB user resource within OpenStack.

## Properties

`Name` - (Required) A unique name for the resource.

`Instance` - (Required) The ID for the database instance.

`Password` - (Required) User's password.

`Databases` - (Optional) A list of database user should have access to.


## Return Values

### Fn::GetAtt

`Region` - Openstack region resource is created in.

`Name` - See Properties above.

`Instance` - See Properties above.

`Password` - See Properties above.

`Databases` - See Properties above.

## See Also

* [openstack_db_user_v1](https://www.terraform.io/docs/providers/openstack/r/db_user_v1.html) in the _Terraform Provider Documentation_