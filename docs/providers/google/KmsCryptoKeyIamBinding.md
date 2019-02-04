# Terraform::Google::KmsCryptoKeyIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud KMS crypto key.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Properties

`Members` - (Required) A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding.

`Role` - (Required) The role that should be applied. Only one
`Terraform::Google::KmsCryptoKeyIamBinding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

`CryptoKeyId` - (Required) The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`.
In the second form, the provider's project setting will be used as a fallback.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the crypto key's IAM policy.

## See Also

* [google_kms_crypto_key_iam_binding](https://www.terraform.io/docs/providers/google/r/kms_crypto_key_iam_binding.html) in the _Terraform Provider Documentation_