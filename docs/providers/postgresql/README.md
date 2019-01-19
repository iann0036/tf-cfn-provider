# PostgreSQL Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/postgresql**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (Required) The address for the postgresql server connection.
* `port` - (Optional) The port for the postgresql server connection. The default is `5432`.
* `database` - (Optional) Database to connect to. The default is `postgres`.
* `username` - (Required) Username for the server connection.
* `password` - (Optional) Password for the server connection.
* `sslmode` - (Optional) Set the priority for an SSL connection to the server.
  Valid values for `sslmode` are (note: `prefer` is not supported by Go's
  [`lib/pq`](https://godoc.org/github.com/lib/pq)):
    * disable - No SSL
    * require - Always SSL (the default, also skip verification)
    * verify-ca - Always SSL (verify that the certificate presented by the server was signed by a trusted CA)
    * verify-full - Always SSL (verify that the certification presented by the server was signed by a trusted CA and the server host name matches the one in the certificate)
  Additional information on the options and their implications can be seen
  [in the `libpq(3)` SSL guide](http://www.postgresql.org/docs/current/static/libpq-ssl.html#LIBPQ-SSL-PROTECTION).
* `connect_timeout` - (Optional) Maximum wait for connection, in seconds. The
  default is `180s`.  Zero or not specified means wait indefinitely.
* `max_connections` - (Optional) Set the maximum number of open connections to
  the database. The default is `4`.  Zero means unlimited open connections.
* `expected_version` - (Optional) Specify a hint to Terraform regarding the
  expected version that the provider will be talking with.  This is a required
  hint in order for Terraform to talk with an ancient version of PostgreSQL.
  This parameter is expected to be a [PostgreSQL
  Version](https://www.postgresql.org/support/versioning/) or `current`.  Once a
  connection has been established, Terraform will fingerprint the actual
  version.  Default: `9.0.0`.


## Supported Resources

* [Terraform::PostgreSQL::Database](docs/providers/postgresql/Database.md)
* [Terraform::PostgreSQL::Extension](docs/providers/postgresql/Extension.md)
* [Terraform::PostgreSQL::Role](docs/providers/postgresql/Role.md)
* [Terraform::PostgreSQL::Schema](docs/providers/postgresql/Schema.md)