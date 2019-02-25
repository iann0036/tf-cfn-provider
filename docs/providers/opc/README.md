# Oracle Public Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/opc** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Optional) The username to use, generally your email address.

* `password` - (Optional) The password associated with the username to use.

* `identity_domain` - (Optional) The Identity Domain name (for Traditional accounts) or Identity Service ID (for IDCS accounts) of the environment to use.  

* `endpoint` - (Optional) The Compute Classic API endpoint to use, associated with your Oracle Cloud Account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_endpoint` - (Optional) The Storage Classic API endpoint to use, associated with your Oracle Storage Cloud account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_service_id` - (Optional) The Storage Service ID for authentication with the `storage_endpoint`  If not set the `identity_domain` value is used.

* `max_retries` - (Optional) The maximum number of tries to make for a successful response when operating on resources. Defaults to 1.

* `insecure` - (Optional) Skips TLS Verification for using self-signed certificates. Should only be used if absolutely needed.


## Supported Resources

* [Terraform::OPC::ComputeAcl](ComputeAcl.md)
* [Terraform::OPC::ComputeImageListEntry](ComputeImageListEntry.md)
* [Terraform::OPC::ComputeImageList](ComputeImageList.md)
* [Terraform::OPC::ComputeInstance](ComputeInstance.md)
* [Terraform::OPC::ComputeIpAddressAssociation](ComputeIpAddressAssociation.md)
* [Terraform::OPC::ComputeIpAddressPrefixSet](ComputeIpAddressPrefixSet.md)
* [Terraform::OPC::ComputeIpAddressReservation](ComputeIpAddressReservation.md)
* [Terraform::OPC::ComputeIpAssociation](ComputeIpAssociation.md)
* [Terraform::OPC::ComputeIpNetworkExchange](ComputeIpNetworkExchange.md)
* [Terraform::OPC::ComputeIpNetwork](ComputeIpNetwork.md)
* [Terraform::OPC::ComputeIpReservation](ComputeIpReservation.md)
* [Terraform::OPC::ComputeMachineImage](ComputeMachineImage.md)
* [Terraform::OPC::ComputeOrchestratedInstance](ComputeOrchestratedInstance.md)
* [Terraform::OPC::ComputeRoute](ComputeRoute.md)
* [Terraform::OPC::ComputeSecRule](ComputeSecRule.md)
* [Terraform::OPC::ComputeSecurityApplication](ComputeSecurityApplication.md)
* [Terraform::OPC::ComputeSecurityAssociation](ComputeSecurityAssociation.md)
* [Terraform::OPC::ComputeSecurityIpList](ComputeSecurityIpList.md)
* [Terraform::OPC::ComputeSecurityList](ComputeSecurityList.md)
* [Terraform::OPC::ComputeSecurityProtocol](ComputeSecurityProtocol.md)
* [Terraform::OPC::ComputeSecurityRule](ComputeSecurityRule.md)
* [Terraform::OPC::ComputeSshKey](ComputeSshKey.md)
* [Terraform::OPC::ComputeStorageVolumeAttachment](ComputeStorageVolumeAttachment.md)
* [Terraform::OPC::ComputeStorageVolumeSnapshot](ComputeStorageVolumeSnapshot.md)
* [Terraform::OPC::ComputeStorageVolume](ComputeStorageVolume.md)
* [Terraform::OPC::ComputeVnicSet](ComputeVnicSet.md)
* [Terraform::OPC::ComputeVpnEndpointV2](ComputeVpnEndpointV2.md)
* [Terraform::OPC::LbaasCertificate](LbaasCertificate.md)
* [Terraform::OPC::LbaasListener](LbaasListener.md)
* [Terraform::OPC::LbaasLoadBalancer](LbaasLoadBalancer.md)
* [Terraform::OPC::LbaasPolicy](LbaasPolicy.md)
* [Terraform::OPC::LbaasServerPool](LbaasServerPool.md)
* [Terraform::OPC::StorageContainer](StorageContainer.md)
* [Terraform::OPC::StorageObject](StorageObject.md)