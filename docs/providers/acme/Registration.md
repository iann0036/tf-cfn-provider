# Terraform::ACME::Registration

The `Terraform::ACME::Registration` resource can be used to create and manage accounts on an
ACME server. Once registered, the same private key that has been used for
registration can be used to request authorizations for certificates.

-> This resource is named `Terraform::ACME::Registration` for historical reasons - in the
ACME v1 spec, a _registration_ referred to the account entity.  This resource
name is stable and more than likely will not change until a later major version
of the provider, if at all.

-> Keep in mind that when using this resource along with
[`Terraform::ACME::Certificate`][resource-acme-certificate] within the same configuration, a
change in the provider-level `server_url` (example: from the Let's Encrypt
staging to production environment) within the same Terraform state will result
in a resource failure, as Terraform will attempt to look for the account in the
wrong CA. Consider different workspaces per environment, and/or using [multiple
provider instances][multiple-provider-instances].

[resource-acme-certificate]: /docs/providers/acme/r/certificate.html
[multiple-provider-instances]: /docs/configuration/providers.html#multiple-provider-instances

## Properties


## See Also

* [acme_registration](https://www.terraform.io/docs/providers/acme/r/registration.html) in the _Terraform Provider Documentation_