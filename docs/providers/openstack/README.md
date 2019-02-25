# OpenStack Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/openstack** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `auth_url` - (Optional; required if `cloud` is not specified) The Identity
  authentication URL.

* `cloud` - (Optional; required if `auth_url` is not specified) An entry in a
  `clouds.yaml` file. See the OpenStack `os-client-config`
  [documentation](https://docs.openstack.org/os-client-config/latest/user/configuration.html)
  for more information about `clouds.yaml` files.

* `region` - (Optional) The region of the OpenStack cloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region OpenStack environments, but this behavior may vary
  depending on the OpenStack environment being used.

* `user_name` - (Optional) The Username to login with.

* `user_id` - (Optional) The User ID to login with.

* `application_credential_id` - (Optional) (Identity v3 only) The ID of an
    application credential to authenticate with. An
    `application_credential_secret` has to bet set along with this parameter.

* `application_credential_name` - (Optional) (Identity v3 only) The name of an
    application credential to authenticate with. Conflicts with the
    `application_credential_name`, requires `user_id`, or `user_name` and
    `user_domain_name` (or `user_domain_id`) to be set.

* `application_credential_secret` - (Optional) (Identity v3 only) The secret of an
    application credential to authenticate with. Required by
    `application_credential_id` or `application_credential_name`.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `password` - (Optional) The Password to login with.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform. If omitted, the `OS_TOKEN` or `OS_AUTH_TOKEN` environment
  variables are used.

* `user_domain_name` - (Optional) The domain name where the user is located.

* `user_domain_id` - (Optional) The domain ID where the user is located.

* `project_domain_name` - (Optional) The domain name where the project is
  located.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3).

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).

* `default_domain` - (Optional) The ID of the Domain to scope to if no other
  domain is specified (Identity v3).

* `insecure` - (Optional) Trust self-signed SSL certificates.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key.

* `endpoint_type` - (Optional) Specify which type of endpoint to use from the
  service catalog. It can be set using the OS_ENDPOINT_TYPE environment
  variable. If not set, public endpoints is used.

* `endpoint_overrides` - (Optional) A set of key/value pairs that can
  override an endpoint for a specified OpenStack service. Setting an override
  requires you to specify the full and complete endpoint URL. This might
  also invalidate any region you have set, too. Please see below for more details.
  Please use this at your own risk.

* `swauth` - (Optional) Set to `true` to authenticate against Swauth, a
  Swift-native authentication system. If omitted, the `OS_SWAUTH` environment
  variable is used. You must also set `username` to the Swauth/Swift username
  such as `username:project`. Set the `password` to the Swauth/Swift key.
  Finally, set `auth_url` as the location of the Swift service. Note that this
  will only work when used with the OpenStack Object Storage resources.

* `use_octavia` - (Optional) If set to `true`, API requests will go the Load Balancer
  service (Octavia) instead of the Networking service (Neutron).


## Supported Resources

* [Terraform::OpenStack::BlockstorageVolumeAttachV2](BlockstorageVolumeAttachV2.md)
* [Terraform::OpenStack::BlockstorageVolumeAttachV3](BlockstorageVolumeAttachV3.md)
* [Terraform::OpenStack::BlockstorageVolumeV1](BlockstorageVolumeV1.md)
* [Terraform::OpenStack::BlockstorageVolumeV2](BlockstorageVolumeV2.md)
* [Terraform::OpenStack::BlockstorageVolumeV3](BlockstorageVolumeV3.md)
* [Terraform::OpenStack::ComputeFlavorAccessV2](ComputeFlavorAccessV2.md)
* [Terraform::OpenStack::ComputeFlavorV2](ComputeFlavorV2.md)
* [Terraform::OpenStack::ComputeFloatingipAssociateV2](ComputeFloatingipAssociateV2.md)
* [Terraform::OpenStack::ComputeFloatingipV2](ComputeFloatingipV2.md)
* [Terraform::OpenStack::ComputeInstanceV2](ComputeInstanceV2.md)
* [Terraform::OpenStack::ComputeInterfaceAttachV2](ComputeInterfaceAttachV2.md)
* [Terraform::OpenStack::ComputeKeypairV2](ComputeKeypairV2.md)
* [Terraform::OpenStack::ComputeSecgroupV2](ComputeSecgroupV2.md)
* [Terraform::OpenStack::ComputeServergroupV2](ComputeServergroupV2.md)
* [Terraform::OpenStack::ComputeVolumeAttachV2](ComputeVolumeAttachV2.md)
* [Terraform::OpenStack::ContainerinfraClusterV1](ContainerinfraClusterV1.md)
* [Terraform::OpenStack::ContainerinfraClustertemplateV1](ContainerinfraClustertemplateV1.md)
* [Terraform::OpenStack::DbConfigurationV1](DbConfigurationV1.md)
* [Terraform::OpenStack::DbDatabaseV1](DbDatabaseV1.md)
* [Terraform::OpenStack::DbInstanceV1](DbInstanceV1.md)
* [Terraform::OpenStack::DbUserV1](DbUserV1.md)
* [Terraform::OpenStack::DnsRecordsetV2](DnsRecordsetV2.md)
* [Terraform::OpenStack::DnsZoneV2](DnsZoneV2.md)
* [Terraform::OpenStack::FwFirewallV1](FwFirewallV1.md)
* [Terraform::OpenStack::FwPolicyV1](FwPolicyV1.md)
* [Terraform::OpenStack::FwRuleV1](FwRuleV1.md)
* [Terraform::OpenStack::IdentityApplicationCredentialV3](IdentityApplicationCredentialV3.md)
* [Terraform::OpenStack::IdentityProjectV3](IdentityProjectV3.md)
* [Terraform::OpenStack::IdentityRoleAssignmentV3](IdentityRoleAssignmentV3.md)
* [Terraform::OpenStack::IdentityRoleV3](IdentityRoleV3.md)
* [Terraform::OpenStack::IdentityUserV3](IdentityUserV3.md)
* [Terraform::OpenStack::ImagesImageV2](ImagesImageV2.md)
* [Terraform::OpenStack::LbL7policyV2](LbL7policyV2.md)
* [Terraform::OpenStack::LbL7ruleV2](LbL7ruleV2.md)
* [Terraform::OpenStack::LbListenerV2](LbListenerV2.md)
* [Terraform::OpenStack::LbLoadbalancerV2](LbLoadbalancerV2.md)
* [Terraform::OpenStack::LbMemberV1](LbMemberV1.md)
* [Terraform::OpenStack::LbMemberV2](LbMemberV2.md)
* [Terraform::OpenStack::LbMonitorV1](LbMonitorV1.md)
* [Terraform::OpenStack::LbMonitorV2](LbMonitorV2.md)
* [Terraform::OpenStack::LbPoolV1](LbPoolV1.md)
* [Terraform::OpenStack::LbPoolV2](LbPoolV2.md)
* [Terraform::OpenStack::LbVipV1](LbVipV1.md)
* [Terraform::OpenStack::NetworkingAddressscopeV2](NetworkingAddressscopeV2.md)
* [Terraform::OpenStack::NetworkingFloatingipAssociateV2](NetworkingFloatingipAssociateV2.md)
* [Terraform::OpenStack::NetworkingFloatingipV2](NetworkingFloatingipV2.md)
* [Terraform::OpenStack::NetworkingNetworkV2](NetworkingNetworkV2.md)
* [Terraform::OpenStack::NetworkingPortSecgroupAssociateV2](NetworkingPortSecgroupAssociateV2.md)
* [Terraform::OpenStack::NetworkingPortV2](NetworkingPortV2.md)
* [Terraform::OpenStack::NetworkingRouterInterfaceV2](NetworkingRouterInterfaceV2.md)
* [Terraform::OpenStack::NetworkingRouterRouteV2](NetworkingRouterRouteV2.md)
* [Terraform::OpenStack::NetworkingRouterV2](NetworkingRouterV2.md)
* [Terraform::OpenStack::NetworkingSecgroupRuleV2](NetworkingSecgroupRuleV2.md)
* [Terraform::OpenStack::NetworkingSecgroupV2](NetworkingSecgroupV2.md)
* [Terraform::OpenStack::NetworkingSubnetRouteV2](NetworkingSubnetRouteV2.md)
* [Terraform::OpenStack::NetworkingSubnetV2](NetworkingSubnetV2.md)
* [Terraform::OpenStack::NetworkingSubnetpoolV2](NetworkingSubnetpoolV2.md)
* [Terraform::OpenStack::NetworkingTrunkV2](NetworkingTrunkV2.md)
* [Terraform::OpenStack::ObjectstorageContainerV1](ObjectstorageContainerV1.md)
* [Terraform::OpenStack::ObjectstorageObjectV1](ObjectstorageObjectV1.md)
* [Terraform::OpenStack::ObjectstorageTempurlV1](ObjectstorageTempurlV1.md)
* [Terraform::OpenStack::SharedfilesystemShareAccessV2](SharedfilesystemShareAccessV2.md)
* [Terraform::OpenStack::SharedfilesystemShareV2](SharedfilesystemShareV2.md)
* [Terraform::OpenStack::VpnaasEndpointGroupV2](VpnaasEndpointGroupV2.md)
* [Terraform::OpenStack::VpnaasIkePolicyV2](VpnaasIkePolicyV2.md)
* [Terraform::OpenStack::VpnaasIpsecPolicyV2](VpnaasIpsecPolicyV2.md)
* [Terraform::OpenStack::VpnaasServiceV2](VpnaasServiceV2.md)
* [Terraform::OpenStack::VpnaasSiteConnectionV2](VpnaasSiteConnectionV2.md)