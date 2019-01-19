# Terraform::MySQL::User

The ``mysql_user`` resource creates and manages a user on a MySQL
server.

~> **Note:** The password for the user is provided in plain text, and is
obscured by an unsalted hash in the state
[Read more about sensitive data in state](/docs/state/sensitive-data.html).
Care is required when using this resource, to avoid disclosing the password.

## Properties

TBC

## Return Values

### Fn::GetAtt

`User` - The name of the user.

`Password` - The password of the user.

`Id` - The id of the user created, composed as "username@host".

`Host` - The host where the user was created.

## See Also

* [mysql_user](https://www.terraform.io/docs/providers/mysql/r/user.html) in the _Terraform Provider Documentation_