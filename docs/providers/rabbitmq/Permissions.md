# Terraform::RabbitMQ::Permissions

The ``Terraform::RabbitMQ::Permissions`` resource creates and manages a user's set of
permissions.

## Properties

`User` - (Required) The user to apply the permissions to.

`Vhost` - (Required) The vhost to create the resource in.

`Permissions` - (Required) The settings of the permissions. The structure is
described below.

### Permissions Properties

`Configure` - (Required) The "configure" ACL.

`Write` - (Required) The "write" ACL.

`Read` - (Required) The "read" ACL.


## See Also

* [rabbitmq_permissions](https://www.terraform.io/docs/providers/rabbitmq/r/permissions.html) in the _Terraform Provider Documentation_