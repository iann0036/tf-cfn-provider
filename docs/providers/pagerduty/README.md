# PagerDuty Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/pagerduty**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The v2 authorization token. See [API Documentation](https://v2.developer.pagerduty.com/docs/authentication) for more information.
* `skip_credentials_validation` - (Optional) Skip validation of the token against the PagerDuty API.


## Supported Resources

* [Terraform::PagerDuty::Addon](Addon.md)
* [Terraform::PagerDuty::EscalationPolicy](EscalationPolicy.md)
* [Terraform::PagerDuty::Extension](Extension.md)
* [Terraform::PagerDuty::MaintenanceWindow](MaintenanceWindow.md)
* [Terraform::PagerDuty::Schedule](Schedule.md)
* [Terraform::PagerDuty::ServiceIntegration](ServiceIntegration.md)
* [Terraform::PagerDuty::Service](Service.md)
* [Terraform::PagerDuty::TeamMembership](TeamMembership.md)
* [Terraform::PagerDuty::Team](Team.md)
* [Terraform::PagerDuty::UserContactMethod](UserContactMethod.md)
* [Terraform::PagerDuty::User](User.md)