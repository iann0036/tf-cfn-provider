# Oracle Cloud Platform Provider

##Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/oraclepaas**. The below arguments may be included as the key/value or JSON properties in the secret:

* `user` - (Optional) The username to use, generally your email address. It can also
  be sourced from the `OPC_USERNAME` environment variable.

* `password` - (Optional) The password associated with the username to use. It can also be sourced from
  the `OPC_PASSWORD` environment variable.

* `identity_domain` - (Optional) The Identity Domain or Service Instance ID of the environment to use. It can also be sourced from the `OPC_IDENTITY_DOMAIN` environment variable.  

* `database_endpoint` - (Optional) The database API endpoint to use, associated with your Oracle Cloud Platform account.
This is known as the `REST Endpoint` within the Oracle portal. It can also be sourced from the
`ORACLEPAAS_DATABASE_ENDPOINT` environment variable.

* `java_endpoint` - (Optional) The java API endpoint to use, associated with your Oracle Cloud Platform Account.
This is known as the `REST Endpoint` within the Oracle portal. It can also be sourced from the
`ORACLEPAAS_JAVA_ENDPOINT` environment variable.

* `mysql_endpoint` - (Optional) The MySQL API endpoint to use, associated with your Oracle Cloud Platform Account. This is known as the `REST Endpoint` within the Oracle portal. It can also be sourced from the `ORACLEPAAS_MYSQL_ENDPOINT` environment variable.

* `max_retries` - (Optional) The maximum number of tries to make for a successful response when operating on
resources within Oracle Cloud Platform. It can also be sourced from the `OPC_MAX_RETRIES` environment variable.
Defaults to 1.

* `insecure` - (Optional) Skips TLS Verification for using self-signed certificates. Should only be used if
absolutely needed. Can also via setting the `OPC_INSECURE` environment variable to `true`.


## Supported Resources

* [Terraform::OraclePaaS::ApplicationContainer](docs/providers/oraclepaas/ApplicationContainer.md)
* [Terraform::OraclePaaS::DatabaseAccessRule](docs/providers/oraclepaas/DatabaseAccessRule.md)
* [Terraform::OraclePaaS::DatabaseServiceInstance](docs/providers/oraclepaas/DatabaseServiceInstance.md)
* [Terraform::OraclePaaS::JavaAccessRule](docs/providers/oraclepaas/JavaAccessRule.md)
* [Terraform::OraclePaaS::JavaServiceInstance](docs/providers/oraclepaas/JavaServiceInstance.md)
* [Terraform::OraclePaaS::MysqlAccessRule](docs/providers/oraclepaas/MysqlAccessRule.md)
* [Terraform::OraclePaaS::MysqlServiceInstance](docs/providers/oraclepaas/MysqlServiceInstance.md)