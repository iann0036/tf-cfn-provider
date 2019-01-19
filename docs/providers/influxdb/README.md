# InfluxDB Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/influxdb**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``url`` - (Optional) The root URL of a InfluxDB server. May alternatively be
  set via the ``INFLUXDB_URL`` environment variable. Defaults to
  `http://localhost:8086/`.

* ``username`` - (Optional) The name of the user to use when making requests.
  May alternatively be set via the ``INFLUXDB_USERNAME`` environment variable.

* ``password`` - (Optional) The password to use when making requests.
  May alternatively be set via the ``INFLUXDB_PASSWORD`` environment variable.

* ``ssl_skip_verify`` - (Optional) If HTTPS enabled on server, and TLS/SSL
  certificate is, say, self-signed, can set to true to bypass what this client
  considers insecure server connections. May alternatively be set via the
  environment (i.e., ``INFLUXDB_SSL_SKIP_VERIFY=1``)

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::InfluxDB::ContinuousQuery](docs/providers/influxdb/ContinuousQuery.md)
* [Terraform::InfluxDB::Database](docs/providers/influxdb/Database.md)
* [Terraform::InfluxDB::User](docs/providers/influxdb/User.md)