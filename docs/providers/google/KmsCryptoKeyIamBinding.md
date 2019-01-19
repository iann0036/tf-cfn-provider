# Terraform::Google::KmsCryptoKeyIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud KMS crypto key.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Etag` - (Computed) The etag of the crypto key's IAM policy.

## See Also

* [google_kms_crypto_key_iam_binding](https://www.terraform.io/docs/providers/google/r/kms_crypto_key_iam_binding.html) in the _Terraform Provider Documentation_