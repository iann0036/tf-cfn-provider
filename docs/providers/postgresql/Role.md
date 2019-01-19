# Terraform::PostgreSQL::Role

The ``Terraform::PostgreSQL::Role`` resource creates and manages a role on a PostgreSQL
server.

When a ``Terraform::PostgreSQL::Role`` resource is removed, the PostgreSQL ROLE will
automatically run a [`REASSIGN
OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html)
and [`DROP
OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html) to
the `CURRENT_USER` (normally the connected user for the provider).  If the
specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
same PostgreSQL Cluster, one PostgreSQL provider per database must be created
and all but the final ``Terraform::PostgreSQL::Role`` must specify a `SkipDropRole`.

~> **Note:** All arguments including role name and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The name of the role. Must be unique on the PostgreSQL server instance where it is configured.

`Superuser` - (Optional) Defines whether the role is a "superuser", and therefore can override all access restrictions within the database.  Default value is `false`.

`CreateDatabase` - (Optional) Defines a role's ability to execute `CREATE DATABASE`.  Default value is `false`.

`CreateRole` - (Optional) Defines a role's ability to execute `CREATE ROLE`. A role with this privilege can also alter and drop other roles.  Default value is `false`.

`Inherit` - (Optional) Defines whether a role "inherits" the privileges of roles it is a member of.  Default value is `true`.

`Login` - (Optional) Defines whether role is allowed to log in.  Roles without this attribute are useful for managing database privileges, but are not users in the usual sense of the word.  Default value is `false`.

`Replication` - (Optional) Defines whether a role is allowed to initiate streaming replication or put the system in and out of backup mode.  Default value is `false`.

`BypassRowLevelSecurity` - (Optional) Defines whether a role bypasses every row-level security (RLS) policy.  Default value is `false`.

`ConnectionLimit` - (Optional) If this role can log in, this specifies how many concurrent connections the role can establish. `-1` (the default) means no limit.

`EncryptedPassword` - (Optional) Defines whether the password is stored encrypted in the system catalogs.  Default value is `true`.  NOTE: this value is always set (to the conservative and safe value), but may interfere with the behavior of [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).

`Password` - (Optional) Sets the role's password. A password is only of use for roles having the `Login` attribute set to true.

`ValidUntil` - (Optional) Defines the date and time after which the role's password is no longer valid.  Established connections past this `valid_time` will have to be manually terminated.  This value corresponds to a PostgreSQL datetime. If omitted or the magic value `NULL` is used, `ValidUntil` will be set to `infinity`.  Default is `NULL`, therefore `infinity`.

`SkipDropRole` - (Optional) When a PostgreSQL ROLE exists in multiple databases and the ROLE is dropped, the [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html) in each of the respective databases must occur before the ROLE can be dropped from the catalog.  Set this option to true when there are multiple databases in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership. This is the third and final step taken when removing a ROLE from a database.

`SkipReassignOwned` - (Optional) When a PostgreSQL ROLE exists in multiple databases and the ROLE is dropped, a [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in must be executed on each of the respective databases before the `DROP ROLE` can be executed to dropped the ROLE from the catalog.  This is the first and second steps taken when removing a ROLE from a database (the second step being an implicit [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).


## See Also

* [postgresql_role](https://www.terraform.io/docs/providers/postgresql/r/role.html) in the _Terraform Provider Documentation_