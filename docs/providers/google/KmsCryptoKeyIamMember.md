# Terraform::Google::KmsCryptoKeyIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud KMS crypto key.

~> **Note:** This resource _must not_ be used in conjunction with
   `Terraform::Google::KmsCryptoKeyIamPolicy` or they will fight over what your policy
   should be. Similarly, roles controlled by `Terraform::Google::KmsCryptoKeyIamBinding`
   should not be assigned to using `Terraform::Google::KmsCryptoKeyIamMember`.

## Properties

`Member` - (Required) The user that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding.

`Role` - (Required) The role that should be applied. Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.

`CryptoKeyId` - (Required) The key ring ID, in the form `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form, the provider's project setting will be used as a fallback.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the project's IAM policy.

## See Also

* [google_kms_crypto_key_iam_member](https://www.terraform.io/docs/providers/google/r/kms_crypto_key_iam_member.html) in the _Terraform Provider Documentation_