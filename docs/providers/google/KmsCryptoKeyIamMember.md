# Terraform::Google::KmsCryptoKeyIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud KMS crypto key.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_kms_crypto_key_iam_policy` or they will fight over what your policy
   should be. Similarly, roles controlled by `google_kms_crypto_key_iam_binding`
   should not be assigned to using `google_kms_crypto_key_iam_member`.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the project's IAM policy.

## See Also

* [google_kms_crypto_key_iam_member](https://www.terraform.io/docs/providers/google/r/kms_crypto_key_iam_member.html) in the _Terraform Provider Documentation_