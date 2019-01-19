# Terraform::MySQL::Grant

The ``Terraform::MySQL::Grant`` resource creates and manages privileges given to
a user on a MySQL server.

## Properties

`User` - (Optional) The name of the user. Conflicts with `Role`.

`Host` - (Optional) The source host of the user. Defaults to "localhost". Conflicts with `Role`.

`Role` - (Optional) The role to grant `Privileges` to. Conflicts with `User` and `Host`.

`Database` - (Required) The database to grant privileges on.

`Table` - (Optional) Which table to grant `Privileges` on. Defaults to `*`, which is all tables.

`Privileges` - (Optional) A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `Roles`.

`Roles` - (Optional) A list of rols to grant to the user. Conflicts with `Privileges`.

`TlsOption` - (Optional) An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.

`Grant` - (Optional) Whether to also give the user privileges to grant the same privileges to other users.


## See Also

* [mysql_grant](https://www.terraform.io/docs/providers/mysql/r/grant.html) in the _Terraform Provider Documentation_