# OpenStack Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/openstack**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_url` - (Optional; required if `cloud` is not specified) The Identity
  authentication URL. If omitted, the `OS_AUTH_URL` environment variable is used.

* `cloud` - (Optional; required if `auth_url` is not specified) An entry in a
  `clouds.yaml` file. See the OpenStack `os-client-config`
  [documentation](https://docs.openstack.org/os-client-config/latest/user/configuration.html)
  for more information about `clouds.yaml` files. If omitted, the `OS_CLOUD`
  environment variable is used.

* `region` - (Optional) The region of the OpenStack cloud to use. If omitted,
  the `OS_REGION_NAME` environment variable is used. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region OpenStack environments, but this behavior may vary
  depending on the OpenStack environment being used.

* `user_name` - (Optional) The Username to login with. If omitted, the
  `OS_USERNAME` environment variable is used.

* `user_id` - (Optional) The User ID to login with. If omitted, the
  `OS_USER_ID` environment variable is used.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_ID` or
  `OS_PROJECT_ID` environment variables are used.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_NAME` or
  `OS_PROJECT_NAME` environment variable are used.

* `password` - (Optional) The Password to login with. If omitted, the
  `OS_PASSWORD` environment variable is used.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform. If omitted, the `OS_TOKEN` or `OS_AUTH_TOKEN` environment
  variables are used.

* `user_domain_name` - (Optional) The domain name where the user is located. If
  omitted, the `OS_USER_DOMAIN_NAME` environment variable is checked.

* `user_domain_id` - (Optional) The domain ID where the user is located. If
  omitted, the `OS_USER_DOMAIN_ID` environment variable is checked.

* `project_domain_name` - (Optional) The domain name where the project is
  located. If omitted, the `OS_PROJECT_DOMAIN_NAME` environment variable is
  checked.

* `project_domain_id` - (Optional) The domain ID where the project is located
  If omitted, the `OS_PROJECT_DOMAIN_ID` environment variable is checked.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3). If
  omitted, the `OS_DOMAIN_ID` environment variable is checked.

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).
  If omitted, the following environment variables are checked (in this order):
  `OS_DOMAIN_NAME`.

* `default_domain` - (Optional) The ID of the Domain to scope to if no other
  domain is specified (Identity v3). If omitted, the environment variable
  `OS_DEFAULT_DOMAIN` is checked or a default value of "default" will be
  used.

* `insecure` - (Optional) Trust self-signed SSL certificates. If omitted, the
  `OS_INSECURE` environment variable is used.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate. If omitted, the `OS_CACERT` environment variable is used.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate. If omitted the `OS_CERT` environment variable is used.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key. If omitted the `OS_KEY` environment variable is used.

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

* [Terraform::OpenStack::BlockstorageVolumeAttachV2](docs/providers/openstack/BlockstorageVolumeAttachV2.md)
* [Terraform::OpenStack::BlockstorageVolumeAttachV3](docs/providers/openstack/BlockstorageVolumeAttachV3.md)
* [Terraform::OpenStack::BlockstorageVolumeV1](docs/providers/openstack/BlockstorageVolumeV1.md)
* [Terraform::OpenStack::BlockstorageVolumeV2](docs/providers/openstack/BlockstorageVolumeV2.md)
* [Terraform::OpenStack::BlockstorageVolumeV3](docs/providers/openstack/BlockstorageVolumeV3.md)
* [Terraform::OpenStack::ComputeFlavorAccessV2](docs/providers/openstack/ComputeFlavorAccessV2.md)
* [Terraform::OpenStack::ComputeFlavorV2](docs/providers/openstack/ComputeFlavorV2.md)
* [Terraform::OpenStack::ComputeFloatingipAssociateV2](docs/providers/openstack/ComputeFloatingipAssociateV2.md)
* [Terraform::OpenStack::ComputeFloatingipV2](docs/providers/openstack/ComputeFloatingipV2.md)
* [Terraform::OpenStack::ComputeInstanceV2](docs/providers/openstack/ComputeInstanceV2.md)
* [Terraform::OpenStack::ComputeInterfaceAttachV2](docs/providers/openstack/ComputeInterfaceAttachV2.md)
* [Terraform::OpenStack::ComputeKeypairV2](docs/providers/openstack/ComputeKeypairV2.md)
* [Terraform::OpenStack::ComputeSecgroupV2](docs/providers/openstack/ComputeSecgroupV2.md)
* [Terraform::OpenStack::ComputeServergroupV2](docs/providers/openstack/ComputeServergroupV2.md)
* [Terraform::OpenStack::ComputeVolumeAttachV2](docs/providers/openstack/ComputeVolumeAttachV2.md)
* [Terraform::OpenStack::ContainerinfraClusterV1](docs/providers/openstack/ContainerinfraClusterV1.md)
* [Terraform::OpenStack::ContainerinfraClustertemplateV1](docs/providers/openstack/ContainerinfraClustertemplateV1.md)
* [Terraform::OpenStack::DbConfigurationV1](docs/providers/openstack/DbConfigurationV1.md)
* [Terraform::OpenStack::DbDatabaseV1](docs/providers/openstack/DbDatabaseV1.md)
* [Terraform::OpenStack::DbInstanceV1](docs/providers/openstack/DbInstanceV1.md)
* [Terraform::OpenStack::DbUserV1](docs/providers/openstack/DbUserV1.md)
* [Terraform::OpenStack::DnsRecordsetV2](docs/providers/openstack/DnsRecordsetV2.md)
* [Terraform::OpenStack::DnsZoneV2](docs/providers/openstack/DnsZoneV2.md)
* [Terraform::OpenStack::FwFirewallV1](docs/providers/openstack/FwFirewallV1.md)
* [Terraform::OpenStack::FwPolicyV1](docs/providers/openstack/FwPolicyV1.md)
* [Terraform::OpenStack::FwRuleV1](docs/providers/openstack/FwRuleV1.md)
* [Terraform::OpenStack::IdentityProjectV3](docs/providers/openstack/IdentityProjectV3.md)
* [Terraform::OpenStack::IdentityRoleAssignmentV3](docs/providers/openstack/IdentityRoleAssignmentV3.md)
* [Terraform::OpenStack::IdentityRoleV3](docs/providers/openstack/IdentityRoleV3.md)
* [Terraform::OpenStack::IdentityUserV3](docs/providers/openstack/IdentityUserV3.md)
* [Terraform::OpenStack::ImagesImageV2](docs/providers/openstack/ImagesImageV2.md)
* [Terraform::OpenStack::LbL7policyV2](docs/providers/openstack/LbL7policyV2.md)
* [Terraform::OpenStack::LbL7ruleV2](docs/providers/openstack/LbL7ruleV2.md)
* [Terraform::OpenStack::LbListenerV2](docs/providers/openstack/LbListenerV2.md)
* [Terraform::OpenStack::LbLoadbalancerV2](docs/providers/openstack/LbLoadbalancerV2.md)
* [Terraform::OpenStack::LbMemberV1](docs/providers/openstack/LbMemberV1.md)
* [Terraform::OpenStack::LbMemberV2](docs/providers/openstack/LbMemberV2.md)
* [Terraform::OpenStack::LbMonitorV1](docs/providers/openstack/LbMonitorV1.md)
* [Terraform::OpenStack::LbMonitorV2](docs/providers/openstack/LbMonitorV2.md)
* [Terraform::OpenStack::LbPoolV1](docs/providers/openstack/LbPoolV1.md)
* [Terraform::OpenStack::LbPoolV2](docs/providers/openstack/LbPoolV2.md)
* [Terraform::OpenStack::LbVipV1](docs/providers/openstack/LbVipV1.md)
* [Terraform::OpenStack::NetworkingFloatingipAssociateV2](docs/providers/openstack/NetworkingFloatingipAssociateV2.md)
* [Terraform::OpenStack::NetworkingFloatingipV2](docs/providers/openstack/NetworkingFloatingipV2.md)
* [Terraform::OpenStack::NetworkingNetworkV2](docs/providers/openstack/NetworkingNetworkV2.md)
* [Terraform::OpenStack::NetworkingPortV2](docs/providers/openstack/NetworkingPortV2.md)
* [Terraform::OpenStack::NetworkingRouterInterfaceV2](docs/providers/openstack/NetworkingRouterInterfaceV2.md)
* [Terraform::OpenStack::NetworkingRouterRouteV2](docs/providers/openstack/NetworkingRouterRouteV2.md)
* [Terraform::OpenStack::NetworkingRouterV2](docs/providers/openstack/NetworkingRouterV2.md)
* [Terraform::OpenStack::NetworkingSecgroupRuleV2](docs/providers/openstack/NetworkingSecgroupRuleV2.md)
* [Terraform::OpenStack::NetworkingSecgroupV2](docs/providers/openstack/NetworkingSecgroupV2.md)
* [Terraform::OpenStack::NetworkingSubnetRouteV2](docs/providers/openstack/NetworkingSubnetRouteV2.md)
* [Terraform::OpenStack::NetworkingSubnetV2](docs/providers/openstack/NetworkingSubnetV2.md)
* [Terraform::OpenStack::NetworkingSubnetpoolV2](docs/providers/openstack/NetworkingSubnetpoolV2.md)
* [Terraform::OpenStack::NetworkingTrunkV2](docs/providers/openstack/NetworkingTrunkV2.md)
* [Terraform::OpenStack::ObjectstorageContainerV1](docs/providers/openstack/ObjectstorageContainerV1.md)
* [Terraform::OpenStack::ObjectstorageObjectV1](docs/providers/openstack/ObjectstorageObjectV1.md)
* [Terraform::OpenStack::ObjectstorageTempurlV1](docs/providers/openstack/ObjectstorageTempurlV1.md)
* [Terraform::OpenStack::SharedfilesystemShareAccessV2](docs/providers/openstack/SharedfilesystemShareAccessV2.md)
* [Terraform::OpenStack::SharedfilesystemShareV2](docs/providers/openstack/SharedfilesystemShareV2.md)
* [Terraform::OpenStack::VpnaasEndpointGroupV2](docs/providers/openstack/VpnaasEndpointGroupV2.md)
* [Terraform::OpenStack::VpnaasIkePolicyV2](docs/providers/openstack/VpnaasIkePolicyV2.md)
* [Terraform::OpenStack::VpnaasIpsecPolicyV2](docs/providers/openstack/VpnaasIpsecPolicyV2.md)
* [Terraform::OpenStack::VpnaasServiceV2](docs/providers/openstack/VpnaasServiceV2.md)
* [Terraform::OpenStack::VpnaasSiteConnectionV2](docs/providers/openstack/VpnaasSiteConnectionV2.md)