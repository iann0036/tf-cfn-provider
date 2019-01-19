# Oracle Public Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/opc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `user` - (Optional) The username to use, generally your email address. It can also
  be sourced from the `OPC_USERNAME` environment variable.

* `password` - (Optional) The password associated with the username to use. It can also be sourced from
  the `OPC_PASSWORD` environment variable.

* `identity_domain` - (Optional) The Identity Domain name (for Traditional accounts) or Identity Service ID (for IDCS accounts) of the environment to use. It can also be sourced from the `OPC_IDENTITY_DOMAIN` environment variable.  

* `endpoint` - (Optional) The Compute Classic API endpoint to use, associated with your Oracle Cloud Account. This is known as the `REST Endpoint` within the Oracle portal. It can also be sourced from the `OPC_ENDPOINT` environment variable.

* `storage_endpoint` - (Optional) The Storage Classic API endpoint to use, associated with your Oracle Storage Cloud account. This is known as the `REST Endpoint` within the Oracle portal. Can also be set via the `OPC_STORAGE_ENDPOINT` environment variable.

* `storage_service_id` - (Optional) The Storage Service ID for authentication with the `storage_endpoint`  If not set the `identity_domain` value is used. Can also be set via the `OPC_STORAGE_SERVICE_ID` environment variable.

* `max_retries` - (Optional) The maximum number of tries to make for a successful response when operating on resources. It can also be sourced from the `OPC_MAX_RETRIES` environment variable. Defaults to 1.

* `insecure` - (Optional) Skips TLS Verification for using self-signed certificates. Should only be used if absolutely needed. Can also via setting the `OPC_INSECURE` environment variable to `true`.


## Supported Resources

* [Terraform::OPC::ComputeAcl](docs/providers/opc/ComputeAcl.md)
* [Terraform::OPC::ComputeImageListEntry](docs/providers/opc/ComputeImageListEntry.md)
* [Terraform::OPC::ComputeImageList](docs/providers/opc/ComputeImageList.md)
* [Terraform::OPC::ComputeInstance](docs/providers/opc/ComputeInstance.md)
* [Terraform::OPC::ComputeIpAddressAssociation](docs/providers/opc/ComputeIpAddressAssociation.md)
* [Terraform::OPC::ComputeIpAddressPrefixSet](docs/providers/opc/ComputeIpAddressPrefixSet.md)
* [Terraform::OPC::ComputeIpAddressReservation](docs/providers/opc/ComputeIpAddressReservation.md)
* [Terraform::OPC::ComputeIpAssociation](docs/providers/opc/ComputeIpAssociation.md)
* [Terraform::OPC::ComputeIpNetworkExchange](docs/providers/opc/ComputeIpNetworkExchange.md)
* [Terraform::OPC::ComputeIpNetwork](docs/providers/opc/ComputeIpNetwork.md)
* [Terraform::OPC::ComputeIpReservation](docs/providers/opc/ComputeIpReservation.md)
* [Terraform::OPC::ComputeMachineImage](docs/providers/opc/ComputeMachineImage.md)
* [Terraform::OPC::ComputeOrchestratedInstance](docs/providers/opc/ComputeOrchestratedInstance.md)
* [Terraform::OPC::ComputeRoute](docs/providers/opc/ComputeRoute.md)
* [Terraform::OPC::ComputeSecRule](docs/providers/opc/ComputeSecRule.md)
* [Terraform::OPC::ComputeSecurityApplication](docs/providers/opc/ComputeSecurityApplication.md)
* [Terraform::OPC::ComputeSecurityAssociation](docs/providers/opc/ComputeSecurityAssociation.md)
* [Terraform::OPC::ComputeSecurityIpList](docs/providers/opc/ComputeSecurityIpList.md)
* [Terraform::OPC::ComputeSecurityList](docs/providers/opc/ComputeSecurityList.md)
* [Terraform::OPC::ComputeSecurityProtocol](docs/providers/opc/ComputeSecurityProtocol.md)
* [Terraform::OPC::ComputeSecurityRule](docs/providers/opc/ComputeSecurityRule.md)
* [Terraform::OPC::ComputeSshKey](docs/providers/opc/ComputeSshKey.md)
* [Terraform::OPC::ComputeStorageVolumeAttachment](docs/providers/opc/ComputeStorageVolumeAttachment.md)
* [Terraform::OPC::ComputeStorageVolumeSnapshot](docs/providers/opc/ComputeStorageVolumeSnapshot.md)
* [Terraform::OPC::ComputeStorageVolume](docs/providers/opc/ComputeStorageVolume.md)
* [Terraform::OPC::ComputeVnicSet](docs/providers/opc/ComputeVnicSet.md)
* [Terraform::OPC::ComputeVpnEndpointV2](docs/providers/opc/ComputeVpnEndpointV2.md)
* [Terraform::OPC::LbaasCertificate](docs/providers/opc/LbaasCertificate.md)
* [Terraform::OPC::LbaasListener](docs/providers/opc/LbaasListener.md)
* [Terraform::OPC::LbaasLoadBalancer](docs/providers/opc/LbaasLoadBalancer.md)
* [Terraform::OPC::LbaasPolicy](docs/providers/opc/LbaasPolicy.md)
* [Terraform::OPC::LbaasServerPool](docs/providers/opc/LbaasServerPool.md)
* [Terraform::OPC::StorageContainer](docs/providers/opc/StorageContainer.md)
* [Terraform::OPC::StorageObject](docs/providers/opc/StorageObject.md)