# Terraform::OpenStack::VpnaasIkePolicyV2

Manages a V2 Neutron IKE policy resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create a VPN service. If omitted, the `Region` argument of the provider is used. Changing this creates a new service.

`Name` - (Optional) The name of the policy. Changing this updates the name of the existing policy.

`TenantId` - (Optional) The owner of the policy. Required if admin wants to create a service for another policy. Changing this creates a new policy.

`Description` - (Optional) The human-readable description for the policy. Changing this updates the description of the existing policy.

`AuthAlgorithm` - (Optional) The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512. Default is sha1. Changing this updates the algorithm of the existing policy.

`EncryptionAlgorithm` - (Optional) The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on. The default value is aes-128. Changing this updates the existing policy.

`Pfs` - (Optional) The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5. Changing this updates the existing policy.

`Phase1NegotiationMode` - (Optional) The IKE mode. A valid value is main, which is the default. Changing this updates the existing policy.

`IkeVersion` - (Optional) The IKE mode. A valid value is v1 or v2. Default is v1. Changing this updates the existing policy.

`Lifetime` - (Optional) The lifetime of the security association. Consists of Unit and Value. - `Unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes. Default is seconds. - `Value` - (Optional) The value for the lifetime of the security association. Must be a positive integer. Default is 3600.

`Unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes. Default is seconds. - `Value` - (Optional) The value for the lifetime of the security association. Must be a positive integer. Default is 3600.

`Value` - (Optional) The value for the lifetime of the security association. Must be a positive integer. Default is 3600.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`TenantId` - See Properties above.

`Description` - See Properties above.

`AuthAlgorithm` - See Properties above.

`EncapsulationMode` - See Properties above.

`EncryptionAlgorithm` - See Properties above.

`Pfs` - See Properties above.

`TransformProtocol` - See Properties above.

`Lifetime` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [openstack_vpnaas_ike_policy_v2](https://www.terraform.io/docs/providers/openstack/r/vpnaas_ike_policy_v2.html) in the _Terraform Provider Documentation_