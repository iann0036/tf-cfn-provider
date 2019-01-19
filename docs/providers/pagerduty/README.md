# PagerDuty Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/pagerduty**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The v2 authorization token. It can also be sourced from the PAGERDUTY_TOKEN environment variable. See [API Documentation](https://v2.developer.pagerduty.com/docs/authentication) for more information.
* `skip_credentials_validation` - (Optional) Skip validation of the token against the PagerDuty API.


## Supported Resources

* [Terraform::PagerDuty::Addon](docs/providers/pagerduty/Addon.md)
* [Terraform::PagerDuty::EscalationPolicy](docs/providers/pagerduty/EscalationPolicy.md)
* [Terraform::PagerDuty::Extension](docs/providers/pagerduty/Extension.md)
* [Terraform::PagerDuty::MaintenanceWindow](docs/providers/pagerduty/MaintenanceWindow.md)
* [Terraform::PagerDuty::Schedule](docs/providers/pagerduty/Schedule.md)
* [Terraform::PagerDuty::ServiceIntegration](docs/providers/pagerduty/ServiceIntegration.md)
* [Terraform::PagerDuty::Service](docs/providers/pagerduty/Service.md)
* [Terraform::PagerDuty::TeamMembership](docs/providers/pagerduty/TeamMembership.md)
* [Terraform::PagerDuty::Team](docs/providers/pagerduty/Team.md)
* [Terraform::PagerDuty::UserContactMethod](docs/providers/pagerduty/UserContactMethod.md)
* [Terraform::PagerDuty::User](docs/providers/pagerduty/User.md)