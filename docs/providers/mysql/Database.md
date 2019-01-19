# Terraform::MySQL::Database

The ``mysql_database`` resource creates and manages a database on a MySQL
server.

~> **Caution:** The ``mysql_database`` resource can completely delete your
database just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your database resources as an extra safety measure.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Name` - The name of the database.

`Id` - The id of the database.

`DefaultCharacterSet` - The default_character_set of the database.

`DefaultCollation` - The default_collation of the database.

## See Also

* [mysql_database](https://www.terraform.io/docs/providers/mysql/r/database.html) in the _Terraform Provider Documentation_