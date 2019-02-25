# Cloudflare Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudflare** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

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

* [Terraform::Cloudflare::AccessApplication](AccessApplication.md)
* [Terraform::Cloudflare::AccessPolicy](AccessPolicy.md)
* [Terraform::Cloudflare::AccessRule](AccessRule.md)
* [Terraform::Cloudflare::AccountMember](AccountMember.md)
* [Terraform::Cloudflare::CustomPages](CustomPages.md)
* [Terraform::Cloudflare::Filter](Filter.md)
* [Terraform::Cloudflare::FirewallRule](FirewallRule.md)
* [Terraform::Cloudflare::LoadBalancerMonitor](LoadBalancerMonitor.md)
* [Terraform::Cloudflare::LoadBalancerPool](LoadBalancerPool.md)
* [Terraform::Cloudflare::LoadBalancer](LoadBalancer.md)
* [Terraform::Cloudflare::PageRule](PageRule.md)
* [Terraform::Cloudflare::RateLimit](RateLimit.md)
* [Terraform::Cloudflare::Record](Record.md)
* [Terraform::Cloudflare::SpectrumApplication](SpectrumApplication.md)
* [Terraform::Cloudflare::WafRule](WafRule.md)
* [Terraform::Cloudflare::WorkerRoute](WorkerRoute.md)
* [Terraform::Cloudflare::WorkerScript](WorkerScript.md)
* [Terraform::Cloudflare::ZoneLockdown](ZoneLockdown.md)
* [Terraform::Cloudflare::ZoneSettingsOverride](ZoneSettingsOverride.md)
* [Terraform::Cloudflare::Zone](Zone.md)