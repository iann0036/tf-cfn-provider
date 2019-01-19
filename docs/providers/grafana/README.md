# Grafana Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/grafana**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``url`` - (Required) The root URL of a Grafana server. May alternatively be
  set via the ``GRAFANA_URL`` environment variable.

* ``auth`` - (Required) The API token or username/password to use to
  authenticate to the Grafana server. If username/password is used, they
  are provided in a single string and separated by a colon. May alternatively
  be set via the ``GRAFANA_AUTH`` environment variable.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::Grafana::AlertNotification](docs/providers/grafana/AlertNotification.md)
* [Terraform::Grafana::Dashboard](docs/providers/grafana/Dashboard.md)
* [Terraform::Grafana::DataSource](docs/providers/grafana/DataSource.md)
* [Terraform::Grafana::Organization](docs/providers/grafana/Organization.md)