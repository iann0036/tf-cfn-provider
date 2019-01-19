# Terraform::Google::SqlUser

Creates a new Google SQL User on a Google SQL User Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/users).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html). Passwords will not be retrieved when running
"terraform import".

## Properties

`Instance` - (Required) The name of the Cloud SQL instance. Changing this forces a new resource to be created.

`Name` - (Required) The name of the user. Changing this forces a new resource to be created.

`Password` - (Optional) The password for the user. Can be updated.

`Host` - (Optional) The host the user can connect from. This is only supported for MySQL instances. Don't set this field for PostgreSQL instances. Can be an IP address. Changing this forces a new resource to be created.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.


## See Also

* [google_sql_user](https://www.terraform.io/docs/providers/google/r/sql_user.html) in the _Terraform Provider Documentation_