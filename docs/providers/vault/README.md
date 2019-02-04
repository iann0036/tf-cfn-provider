# Vault Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vault**. The below arguments may be included as the key/value or JSON properties in the secret:

* `cert_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded certificate to present to the server.

* `key_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded private key for which the authentication certificate was issued.


## Supported Resources

* [Terraform::Vault::ApproleAuthBackendLogin](ApproleAuthBackendLogin.md)
* [Terraform::Vault::ApproleAuthBackendRoleSecretId](ApproleAuthBackendRoleSecretId.md)
* [Terraform::Vault::ApproleAuthBackendRole](ApproleAuthBackendRole.md)
* [Terraform::Vault::Audit](Audit.md)
* [Terraform::Vault::AuthBackend](AuthBackend.md)
* [Terraform::Vault::AwsAuthBackendCert](AwsAuthBackendCert.md)
* [Terraform::Vault::AwsAuthBackendClient](AwsAuthBackendClient.md)
* [Terraform::Vault::AwsAuthBackendIdentityWhitelist](AwsAuthBackendIdentityWhitelist.md)
* [Terraform::Vault::AwsAuthBackendLogin](AwsAuthBackendLogin.md)
* [Terraform::Vault::AwsAuthBackendRoleTag](AwsAuthBackendRoleTag.md)
* [Terraform::Vault::AwsAuthBackendRole](AwsAuthBackendRole.md)
* [Terraform::Vault::AwsAuthBackendRoletagBlacklist](AwsAuthBackendRoletagBlacklist.md)
* [Terraform::Vault::AwsAuthBackendStsRole](AwsAuthBackendStsRole.md)
* [Terraform::Vault::AwsSecretBackendRole](AwsSecretBackendRole.md)
* [Terraform::Vault::AwsSecretBackend](AwsSecretBackend.md)
* [Terraform::Vault::AzureAuthBackendConfig](AzureAuthBackendConfig.md)
* [Terraform::Vault::AzureAuthBackendRole](AzureAuthBackendRole.md)
* [Terraform::Vault::CertAuthBackendRole](CertAuthBackendRole.md)
* [Terraform::Vault::ConsulSecretBackend](ConsulSecretBackend.md)
* [Terraform::Vault::DatabaseSecretBackendConnection](DatabaseSecretBackendConnection.md)
* [Terraform::Vault::DatabaseSecretBackendRole](DatabaseSecretBackendRole.md)
* [Terraform::Vault::EgpPolicy](EgpPolicy.md)
* [Terraform::Vault::GcpAuthBackendRole](GcpAuthBackendRole.md)
* [Terraform::Vault::GcpAuthBackend](GcpAuthBackend.md)
* [Terraform::Vault::GcpSecretBackend](GcpSecretBackend.md)
* [Terraform::Vault::GenericSecret](GenericSecret.md)
* [Terraform::Vault::GithubAuthBackend](GithubAuthBackend.md)
* [Terraform::Vault::GithubTeam](GithubTeam.md)
* [Terraform::Vault::GithubUser](GithubUser.md)
* [Terraform::Vault::IdentityEntityAlias](IdentityEntityAlias.md)
* [Terraform::Vault::IdentityEntity](IdentityEntity.md)
* [Terraform::Vault::JwtAuthBackendRole](JwtAuthBackendRole.md)
* [Terraform::Vault::JwtAuthBackend](JwtAuthBackend.md)
* [Terraform::Vault::KubernetesAuthBackendConfig](KubernetesAuthBackendConfig.md)
* [Terraform::Vault::KubernetesAuthBackendRole](KubernetesAuthBackendRole.md)
* [Terraform::Vault::LdapAuthBackendGroup](LdapAuthBackendGroup.md)
* [Terraform::Vault::LdapAuthBackendUser](LdapAuthBackendUser.md)
* [Terraform::Vault::LdapAuthBackend](LdapAuthBackend.md)
* [Terraform::Vault::Mount](Mount.md)
* [Terraform::Vault::OktaAuthBackendGroup](OktaAuthBackendGroup.md)
* [Terraform::Vault::OktaAuthBackendUser](OktaAuthBackendUser.md)
* [Terraform::Vault::OktaAuthBackend](OktaAuthBackend.md)
* [Terraform::Vault::PkiSecretBackendCert](PkiSecretBackendCert.md)
* [Terraform::Vault::PkiSecretBackendConfigCa](PkiSecretBackendConfigCa.md)
* [Terraform::Vault::PkiSecretBackendIntermediateCertRequest](PkiSecretBackendIntermediateCertRequest.md)
* [Terraform::Vault::PkiSecretBackendIntermediateSetSigned](PkiSecretBackendIntermediateSetSigned.md)
* [Terraform::Vault::PkiSecretBackendRole](PkiSecretBackendRole.md)
* [Terraform::Vault::PkiSecretBackendRootCert](PkiSecretBackendRootCert.md)
* [Terraform::Vault::PkiSecretBackendRootSignIntermediate](PkiSecretBackendRootSignIntermediate.md)
* [Terraform::Vault::PkiSecretBackendSign](PkiSecretBackendSign.md)
* [Terraform::Vault::PkiSecretBackend](PkiSecretBackend.md)
* [Terraform::Vault::Policy](Policy.md)
* [Terraform::Vault::RabbitmqSecretBackendRole](RabbitmqSecretBackendRole.md)
* [Terraform::Vault::RabbitmqSecretBackend](RabbitmqSecretBackend.md)
* [Terraform::Vault::RgpPolicy](RgpPolicy.md)
* [Terraform::Vault::SshSecretBackendCa](SshSecretBackendCa.md)
* [Terraform::Vault::SshSecretBackendRole](SshSecretBackendRole.md)
* [Terraform::Vault::TokenAuthBackendRole](TokenAuthBackendRole.md)