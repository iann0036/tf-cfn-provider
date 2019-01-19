# Terraform::Google::SqlDatabase

Creates a new Google SQL Database on a Google SQL Database Instance. For more information, see
the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/databases).

## Properties

`Name` - (Required) The name of the database.

`Instance` - (Required) The name of containing instance.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Charset` - (Optional) The charset value. See MySQL's [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html) and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html) for more details and supported values. Postgres databases are in beta and have limited `Charset` support; they only support a value of `UTF8` at creation time.

`Collation` - (Optional) The collation value. See MySQL's [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html) and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html) for more details and supported values. Postgres databases are in beta and have limited `Collation` support; they only support a value of `en_US.UTF8` at creation time.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_sql_database](https://www.terraform.io/docs/providers/google/r/sql_database.html) in the _Terraform Provider Documentation_