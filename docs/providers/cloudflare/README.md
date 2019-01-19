# Cloudflare Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudflare**. The below arguments may be included as the key/value or JSON properties in the secret:

* `email` - (Required) The email associated with the account.
* `token` - (Required) The Cloudflare API token.
* `rps` - (Optional) RPS limit to apply when making calls to the API. Default: 4.
* `retries` - (Optional) Maximum number of retries to perform when an API request fails. Default: 3.
* `min_backoff` - (Optional) Minimum backoff period in seconds after failed API calls. Default: 1.
* `max_backoff` - (Optional) Maximum backoff period in seconds after failed API calls Default: 30.
* `api_client_logging` - (Optional) Whether to print logs from the API client (using the default log library logger). Default: false.
* `org_id` - (Optional) Configure API client with this organisation ID, so calls use the organization API rather than the (default) user API.
  This is required for other users in your organization to have access to the resources you manage.
* `use_org_from_zone` - (Optional) Takes a zone name value. This is used to lookup the organization ID that owns this zone, 
  which will be used to configure the API client. If `org_id` is also specified, this field will be ignored.



## Supported Resources

* [Terraform::Cloudflare::AccessApplication](docs/providers/cloudflare/AccessApplication.md)
* [Terraform::Cloudflare::AccessPolicy](docs/providers/cloudflare/AccessPolicy.md)
* [Terraform::Cloudflare::AccessRule](docs/providers/cloudflare/AccessRule.md)
* [Terraform::Cloudflare::AccountMember](docs/providers/cloudflare/AccountMember.md)
* [Terraform::Cloudflare::CustomPages](docs/providers/cloudflare/CustomPages.md)
* [Terraform::Cloudflare::Filter](docs/providers/cloudflare/Filter.md)
* [Terraform::Cloudflare::FirewallRule](docs/providers/cloudflare/FirewallRule.md)
* [Terraform::Cloudflare::LoadBalancerMonitor](docs/providers/cloudflare/LoadBalancerMonitor.md)
* [Terraform::Cloudflare::LoadBalancerPool](docs/providers/cloudflare/LoadBalancerPool.md)
* [Terraform::Cloudflare::LoadBalancer](docs/providers/cloudflare/LoadBalancer.md)
* [Terraform::Cloudflare::PageRule](docs/providers/cloudflare/PageRule.md)
* [Terraform::Cloudflare::RateLimit](docs/providers/cloudflare/RateLimit.md)
* [Terraform::Cloudflare::Record](docs/providers/cloudflare/Record.md)
* [Terraform::Cloudflare::SpectrumApplication](docs/providers/cloudflare/SpectrumApplication.md)
* [Terraform::Cloudflare::WafRule](docs/providers/cloudflare/WafRule.md)
* [Terraform::Cloudflare::WorkerRoute](docs/providers/cloudflare/WorkerRoute.md)
* [Terraform::Cloudflare::WorkerScript](docs/providers/cloudflare/WorkerScript.md)
* [Terraform::Cloudflare::ZoneLockdown](docs/providers/cloudflare/ZoneLockdown.md)
* [Terraform::Cloudflare::ZoneSettingsOverride](docs/providers/cloudflare/ZoneSettingsOverride.md)
* [Terraform::Cloudflare::Zone](docs/providers/cloudflare/Zone.md)