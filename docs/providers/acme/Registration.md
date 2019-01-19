# Terraform::ACME::Registration

The `acme_registration` resource can be used to create and manage accounts on an
ACME server. Once registered, the same private key that has been used for
registration can be used to request authorizations for certificates.

-> This resource is named `acme_registration` for historical reasons - in the
ACME v1 spec, a _registration_ referred to the account entity.  This resource
name is stable and more than likely will not change until a later major version
of the provider, if at all.

## Properties

TBC

## See Also

* [acme_registration](https://www.terraform.io/docs/providers/acme/r/registration.html) in the _Terraform Provider Documentation_