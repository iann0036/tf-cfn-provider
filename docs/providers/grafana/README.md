# Grafana Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/grafana**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``url`` - (Required) The root URL of a Grafana server.

* ``auth`` - (Required) The API token or username/password to use to
  authenticate to the Grafana server. If username/password is used, they
  are provided in a single string and separated by a colon.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::Grafana::AlertNotification](AlertNotification.md)
* [Terraform::Grafana::Dashboard](Dashboard.md)
* [Terraform::Grafana::DataSource](DataSource.md)
* [Terraform::Grafana::Organization](Organization.md)