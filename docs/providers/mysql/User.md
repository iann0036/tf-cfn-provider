# Terraform::MySQL::User

The ``Terraform::MySQL::User`` resource creates and manages a user on a MySQL
server.

~> **Note:** The password for the user is provided in plain text, and is
obscured by an unsalted hash in the state
[Read more about sensitive data in state](/docs/state/sensitive-data.html).
Care is required when using this resource, to avoid disclosing the password.

## Properties

`User` - (Required) The name of the user.

`Host` - (Optional) The source host of the user. Defaults to "localhost".

`PlaintextPassword` - (Optional) The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `AuthPlugin`.

`Password` - (Optional) Deprecated alias of `PlaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `PlaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `AuthPlugin`.

`AuthPlugin` - (Optional) Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `Password` and `PlaintextPassword`.

`TlsOption` - (Optional) An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.

`AWSAuthenticationPlugin` - Allows the use of IAM authentication with [Amazon Aurora][ref-amazon-aurora]. For more details on how to use IAM auth with Aurora, see [here][ref-aurora-using-iam].

`MysqlNoLogin` - Uses the MySQL No-Login Authentication Plugin. The No-Login Authentication Plugin must be active in MySQL. For more information, see [here][ref-mysql-no-login].


## Return Values

### Fn::GetAtt

`User` - The name of the user.

`Password` - The password of the user.

`Id` - The id of the user created, composed as "username@host".

`Host` - The host where the user was created.

## See Also

* [mysql_user](https://www.terraform.io/docs/providers/mysql/r/user.html) in the _Terraform Provider Documentation_