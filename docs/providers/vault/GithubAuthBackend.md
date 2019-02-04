# Terraform::Vault::GithubAuthBackend

Manages a Github Auth mount in a Vault server. See the [Vault 
documentation](https://www.vaultproject.io/docs/auth/github.html) for more
information.

## Properties

`Path` - (Optional) Path where the auth backend is mounted. Defaults to `auth/github`
if not specified.

`Organization` - (Required) The organization configured users must be part of.

`BaseUrl` - (Optional) The API endpoint to use. Useful if you
are running GitHub Enterprise or an API-compatible authentication server.

`Description` - (Optional) Specifies the description of the mount.
This overrides the current stored value, if any.

`Ttl` - (Optional) Duration after which authentication will be expired.
This must be a valid [duration string](https://golang.org/pkg/time/#ParseDuration).

`MaxTtl` - (Optional) Maximum duration after which authentication will be expired.
This must be a valid [duration string](https://golang.org/pkg/time/#ParseDuration).

`DefaultLeaseTtl` - (Optional) Specifies the default time-to-live.
If set, this overrides the global default.
Must be a valid [duration string](https://golang.org/pkg/time/#ParseDuration).

`MaxLeaseTtl` - (Optional) Specifies the maximum time-to-live.
If set, this overrides the global default.
Must be a valid [duration string](https://golang.org/pkg/time/#ParseDuration).

`AuditNonHmacResponseKeys` - (Optional) Specifies the list of keys that will
not be HMAC'd by audit devices in the response data object.

`AuditNonHmacRequestKeys` - (Optional) Specifies the list of keys that will
not be HMAC'd by audit devices in the request data object.

`ListingVisibility` - (Optional) Specifies whether to show this mount in
the UI-specific listing endpoint. Valid values are "unauth" or "hidden".

`PassthroughRequestHeaders` - (Optional) List of headers to whitelist and
pass from the request to the backend.


## See Also

* [vault_github_auth_backend](https://www.terraform.io/docs/providers/vault/r/github_auth_backend.html) in the _Terraform Provider Documentation_