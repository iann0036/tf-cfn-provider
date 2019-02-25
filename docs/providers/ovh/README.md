# OVH Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ovh** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `endpoint` - (Required) Specify which API  endpoint to use.
  It can be set using the `OVH_ENDPOINT` environment
  variable. Value can be set to either "ovh-eu" or "ovh-ca".

* `application_key` - (Optional) The API Application Key.

* `application_secret` - (Optional) The API Application Secret.

* `consumer_key` - (Optional) The API Consumer key.


## Supported Resources

* [Terraform::OVH::CloudNetworkPrivateSubnet](CloudNetworkPrivateSubnet.md)
* [Terraform::OVH::CloudNetworkPrivate](CloudNetworkPrivate.md)
* [Terraform::OVH::CloudUser](CloudUser.md)
* [Terraform::OVH::DomainZoneRecord](DomainZoneRecord.md)
* [Terraform::OVH::DomainZoneRedirection](DomainZoneRedirection.md)
* [Terraform::OVH::IpReverse](IpReverse.md)
* [Terraform::OVH::IploadbalancingHttpRouteRule](IploadbalancingHttpRouteRule.md)
* [Terraform::OVH::IploadbalancingHttpRoute](IploadbalancingHttpRoute.md)
* [Terraform::OVH::IploadbalancingRefresh](IploadbalancingRefresh.md)
* [Terraform::OVH::IploadbalancingTcpFarmServer](IploadbalancingTcpFarmServer.md)
* [Terraform::OVH::IploadbalancingTcpFarm](IploadbalancingTcpFarm.md)
* [Terraform::OVH::IploadbalancingTcpFrontend](IploadbalancingTcpFrontend.md)
* [Terraform::OVH::PubliccloudPrivateNetworkSubnet](PubliccloudPrivateNetworkSubnet.md)
* [Terraform::OVH::PubliccloudPrivateNetwork](PubliccloudPrivateNetwork.md)
* [Terraform::OVH::PubliccloudUser](PubliccloudUser.md)
* [Terraform::OVH::VrackCloudproject](VrackCloudproject.md)
* [Terraform::OVH::VrackPubliccloudAttachment](VrackPubliccloudAttachment.md)