# Dyn Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dyn**. The below arguments may be included as the key/value or JSON properties in the secret:

* `customer_name` - (Required) The Dyn customer name. It must be provided, but it can also be sourced from the `DYN_CUSTOMER_NAME` environment variable.
* `username` - (Required) The Dyn username. It must be provided, but it can also be sourced from the `DYN_USERNAME` environment variable.
* `password` - (Required) The Dyn password. It must be provided, but it can also be sourced from the `DYN_PASSWORD` environment variable.


## Supported Resources

* [Terraform::Dyn::Record](docs/providers/dyn/Record.md)