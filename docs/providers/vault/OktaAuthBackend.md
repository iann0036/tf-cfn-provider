# Terraform::Vault::OktaAuthBackend

Provides a resource for managing an
[Okta auth backend within Vault](https://www.vaultproject.io/docs/auth/okta.html).

## Properties

`Path` - (Required) Path to mount the Okta auth backend.

`Description` - (Optional) The description of the auth backend.

`Organization` - (Required) The Okta organization. This will be the first part of the url `https://XXX.okta.com`.

`Token` - (Optional) The Okta API token. This is required to query Okta for user group membership.
If this is not supplied only locally configured groups will be enabled.

`BaseUrl` - (Optional) The Okta url. Examples: oktapreview.com, okta.com.

`BypassOktaMfa` - (Optional) When true, requests by Okta for a MFA check will be bypassed. This also disallows certain status checks on the account, such as whether the password is expired.

`Ttl` - (Optional) Duration after which authentication will be expired.
[See the documentation for info on valid duration formats](https://golang.org/pkg/time/#ParseDuration).

`MaxTtl` - (Optional) Maximum duration after which authentication will be expired
[See the documentation for info on valid duration formats](https://golang.org/pkg/time/#ParseDuration).

`Group` - (Optional) Associate Okta groups with policies within Vault.
[See below for more details](#okta-group).

`User` - (Optional) Associate Okta users with groups or policies within Vault.
[See below for more details](#okta-user).


## See Also

* [vault_okta_auth_backend](https://www.terraform.io/docs/providers/vault/r/okta_auth_backend.html) in the _Terraform Provider Documentation_