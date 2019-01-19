# MySQL Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/mysql**. The below arguments may be included as the key/value or JSON properties in the secret:

* `endpoint` - (Required) The address of the MySQL server to use. Most often a "hostname:port" pair, but may also be an absolute path to a Unix socket when the host OS is Unix-compatible.
* `username` - (Required) Username to use to authenticate with the server.
* `password` - (Optional) Password for the given user, if that user has a password.
* `tls` - (Optional) The TLS configuration. One of `false`, `true`, or `skip-verify`. Defaults to `false`.


## Supported Resources

* [Terraform::MySQL::Database](Database.md)
* [Terraform::MySQL::Grant](Grant.md)
* [Terraform::MySQL::Role](Role.md)
* [Terraform::MySQL::UserPassword](UserPassword.md)
* [Terraform::MySQL::User](User.md)