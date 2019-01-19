# OVH Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ovh**. The below arguments may be included as the key/value or JSON properties in the secret:

* `endpoint` - (Required) Specify which API  endpoint to use.
  It can be set using the `OVH_ENDPOINT` environment
  variable. Value can be set to either "ovh-eu" or "ovh-ca".

* `application_key` - (Optional) The API Application Key. If omitted,
  the `OVH_APPLICATION_KEY` environment variable is used.

* `application_secret` - (Optional) The API Application Secret. If omitted,
  the `OVH_APPLICATION_SECRET` environment variable is used.

* `consumer_key` - (Optional) The API Consumer key. If omitted,
  the `OVH_CONSUMER_KEY` environment variable is used.


## Supported Resources

* [Terraform::OVH::CloudNetworkPrivateSubnet](docs/providers/ovh/CloudNetworkPrivateSubnet.md)
* [Terraform::OVH::CloudNetworkPrivate](docs/providers/ovh/CloudNetworkPrivate.md)
* [Terraform::OVH::CloudUser](docs/providers/ovh/CloudUser.md)
* [Terraform::OVH::DomainZoneRecord](docs/providers/ovh/DomainZoneRecord.md)
* [Terraform::OVH::DomainZoneRedirection](docs/providers/ovh/DomainZoneRedirection.md)
* [Terraform::OVH::IpReverse](docs/providers/ovh/IpReverse.md)
* [Terraform::OVH::IploadbalancingHttpRouteRule](docs/providers/ovh/IploadbalancingHttpRouteRule.md)
* [Terraform::OVH::IploadbalancingHttpRoute](docs/providers/ovh/IploadbalancingHttpRoute.md)
* [Terraform::OVH::IploadbalancingRefresh](docs/providers/ovh/IploadbalancingRefresh.md)
* [Terraform::OVH::IploadbalancingTcpFarmServer](docs/providers/ovh/IploadbalancingTcpFarmServer.md)
* [Terraform::OVH::IploadbalancingTcpFarm](docs/providers/ovh/IploadbalancingTcpFarm.md)
* [Terraform::OVH::IploadbalancingTcpFrontend](docs/providers/ovh/IploadbalancingTcpFrontend.md)
* [Terraform::OVH::PubliccloudPrivateNetworkSubnet](docs/providers/ovh/PubliccloudPrivateNetworkSubnet.md)
* [Terraform::OVH::PubliccloudPrivateNetwork](docs/providers/ovh/PubliccloudPrivateNetwork.md)
* [Terraform::OVH::PubliccloudUser](docs/providers/ovh/PubliccloudUser.md)
* [Terraform::OVH::VrackCloudproject](docs/providers/ovh/VrackCloudproject.md)
* [Terraform::OVH::VrackPubliccloudAttachment](docs/providers/ovh/VrackPubliccloudAttachment.md)