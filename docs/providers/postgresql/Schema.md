# Terraform::PostgreSQL::Schema

The ``Terraform::PostgreSQL::Schema`` resource creates and manages [schema
objects](https://www.postgresql.org/docs/current/static/ddl-schemas.html) within
a PostgreSQL database.

## Properties

`Name` - (Required) The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.

`Owner` - (Optional) The ROLE who owns the schema.

`IfNotExists` - (Optional) When true, use the existing schema if it exists. (Default: true).

`Policy` - (Optional) Can be specified multiple times for each policy.  Each
policy block supports fields documented below.

### Policy Properties

`Create` - (Optional) Should the specified ROLE have CREATE privileges to the specified SCHEMA.

`CreateWithGrant` - (Optional) Should the specified ROLE have CREATE privileges to the specified SCHEMA and the ability to GRANT the CREATE privilege to other ROLEs.

`Role` - (Optional) The ROLE who is receiving the policy.  If this value is empty or not specified it implies the policy is referring to the [`PUBLIC` role](https://www.postgresql.org/docs/current/static/sql-grant.html).

`Usage` - (Optional) Should the specified ROLE have USAGE privileges to the specified SCHEMA.

`UsageWithGrant` - (Optional) Should the specified ROLE have USAGE privileges to the specified SCHEMA and the ability to GRANT the USAGE privilege to other ROLEs.


## See Also

* [postgresql_schema](https://www.terraform.io/docs/providers/postgresql/r/schema.html) in the _Terraform Provider Documentation_