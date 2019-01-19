# Terraform::MySQL::Database

The ``Terraform::MySQL::Database`` resource creates and manages a database on a MySQL
server.

~> **Caution:** The ``Terraform::MySQL::Database`` resource can completely delete your
database just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your database resources as an extra safety measure.

## Properties

`Name` - (Required) The name of the database. This must be unique within a given MySQL server and may or may not be case-sensitive depending on the operating system on which the MySQL server is running.

`DefaultCharacterSet` - (Optional) The default character set to use when a table is created without specifying an explicit character set. Defaults to "utf8".

`DefaultCollation` - (Optional) The default collation to use when a table is created without specifying an explicit collation. Defaults to ``utf8_general_ci``. Each character set has its own set of collations, so changing the character set requires also changing the collation.


## Return Values

### Fn::GetAtt

`Name` - The name of the database.

`Id` - The id of the database.

`DefaultCharacterSet` - The default_character_set of the database.

`DefaultCollation` - The default_collation of the database.

## See Also

* [mysql_database](https://www.terraform.io/docs/providers/mysql/r/database.html) in the _Terraform Provider Documentation_