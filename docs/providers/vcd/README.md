# VMware vCloud Director Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vcd** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Required) This is the username for vCloud Director API operations.  
  *v2.0+* `user` may be "administrator" (set `org` or `sysorg` to "System" in this case).
  
* `password` - (Required) This is the password for vCloud Director API operations.
  
* `org` - (Required) This is the vCloud Director Org on which to run API
  operations. Can also be specified with the `VCD_ORG` environment
  variable.  
  *v2.0+* `org` may be set to "System" when connection as Sys Admin is desired
  (set `user` to "administrator" in this case).  
  Note: `org` value is case sensitive.
  
* `sysorg` - (Optional; *v2.0+*) - Organization for user authentication. Set `sysorg` to "System" and
   `user` to "administrator" to free up `org` argument for setting a default organization
   for resources to use.
   
* `url` - (Required) This is the URL for the vCloud Director API endpoint. e.g.
  https://server.domain.com/api.
  
* `vdc` - (Optional) This is the virtual datacenter within vCloud Director to run
  API operations against. If not set the plugin will select the first virtual
  datacenter available to your Org. Can also be specified with the `VCD_VDC` environment
  variable.
  
* `max_retry_timeout` - (Optional) This provides you with the ability to specify the maximum
  amount of time (in seconds) you are prepared to wait for interactions on resources managed
  by vCloud Director to be successful. If a resource action fails, the action will be retried
  (as long as it is still within the `max_retry_timeout` value) to try and ensure success.
  Defaults to 60 seconds if not set.
  
* `maxRetryTimeout` - (Deprecated) Use `max_retry_timeout` instead.

* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is false.

* `logging` - (Optional; *v2.0+*) Boolean that enables API calls logging from upstream library `go-vcloud-director`. 
   The logging file will record all API requests and responses, plus some debug information that is part of this 
   provider.

* `logging_file` - (Optional; *v2.0+*) The name of the log file (when `logging` is enabled).


## Supported Resources

* [Terraform::VCD::CatalogItem](CatalogItem.md)
* [Terraform::VCD::CatalogMedia](CatalogMedia.md)
* [Terraform::VCD::Catalog](Catalog.md)
* [Terraform::VCD::Dnat](Dnat.md)
* [Terraform::VCD::EdgegatewayVpn](EdgegatewayVpn.md)
* [Terraform::VCD::FirewallRules](FirewallRules.md)
* [Terraform::VCD::Network (Deprecated)](Network (Deprecated).md)
* [Terraform::VCD::NetworkDirect](NetworkDirect.md)
* [Terraform::VCD::NetworkIsolated](NetworkIsolated.md)
* [Terraform::VCD::NetworkRouted](NetworkRouted.md)
* [Terraform::VCD::Org](Org.md)
* [Terraform::VCD::Snat](Snat.md)
* [Terraform::VCD::VappVm](VappVm.md)
* [Terraform::VCD::Vapp](Vapp.md)