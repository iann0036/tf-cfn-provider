# Terraform::PostgreSQL::Database

The ``Terraform::PostgreSQL::Database`` resource creates and manages [database
objects](https://www.postgresql.org/docs/current/static/managing-databases.html)
within a PostgreSQL server instance.

## Properties

`Name` - (Required) The name of the database. Must be unique on the PostgreSQL server instance where it is configured.

`Owner` - (Optional) The role name of the user who will own the database, or `DEFAULT` to use the default (namely, the user executing the command). To create a database owned by another role or to change the owner of an existing database, you must be a direct or indirect member of the specified role, or the username in the provider is a superuser.

`TablespaceName` - (Optional) The name of the tablespace that will be associated with the database, or `DEFAULT` to use the template database's tablespace.  This tablespace will be the default tablespace used for objects created in this database.

`ConnectionLimit` - (Optional) How many concurrent connections can be established to this database. `-1` (the default) means no limit.

`AllowConnections` - (Optional) If `false` then no one can connect to this database. The default is `true`, allowing connections (except as restricted by other mechanisms, such as `GRANT` or `REVOKE CONNECT`).

`IsTemplate` - (Optional) If `true`, then this database can be cloned by any user with `CREATEDB` privileges; if `false` (the default), then only superusers or the owner of the database can clone it.

`Template` - (Optional) The name of the template database from which to create the database, or `DEFAULT` to use the default template (`template0`).  NOTE: the default in Terraform is `template0`, not `template1`.  Changing this value will force the creation of a new resource as this value can only be changed when a database is created.

`Encoding` - (Optional) Character set encoding to use in the database. Specify a string constant (e.g. `UTF8` or `SQL_ASCII`), or an integer encoding number.  If unset or set to an empty string the default encoding is set to `UTF8`.  If set to `DEFAULT` Terraform will use the same encoding as the template database.  Changing this value will force the creation of a new resource as this value can only be changed when a database is created.

`LcCollate` - (Optional) Collation order (`LC_COLLATE`) to use in the database.  This affects the sort order applied to strings, e.g. in queries with `ORDER BY`, as well as the order used in indexes on text columns. If unset or set to an empty string the default collation is set to `C`.  If set to `DEFAULT` Terraform will use the same collation order as the specified `Template` database.  Changing this value will force the creation of a new resource as this value can only be changed when a database is created.

`LcCtype` - (Optional) Character classification (`LC_CTYPE`) to use in the database. This affects the categorization of characters, e.g. lower, upper and digit. If unset or set to an empty string the default character classification is set to `C`.  If set to `DEFAULT` Terraform will use the character classification of the specified `Template` database.  Changing this value will force the creation of a new resource as this value can only be changed when a database is created.


## See Also

* [postgresql_database](https://www.terraform.io/docs/providers/postgresql/r/database.html) in the _Terraform Provider Documentation_