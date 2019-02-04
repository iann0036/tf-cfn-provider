# Terraform::RabbitMQ::User

The ``Terraform::RabbitMQ::User`` resource creates and manages a user.

~> **Note:** All arguments including username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The name of the user.

`Password` - (Required) The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.

`Tags` - (Optional) Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.


## See Also

* [rabbitmq_user](https://www.terraform.io/docs/providers/rabbitmq/r/user.html) in the _Terraform Provider Documentation_