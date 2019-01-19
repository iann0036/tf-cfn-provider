# Terraform::Google::ServiceAccountKey

Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Name` - The name used for this key pair.

`PublicKey` - The public key, base64 encoded.

`PrivateKey` - The private key in JSON format, base64 encoded. This is what you normally get as a file when creating.

`PrivateKeyFingerprint` - The MD5 public key fingerprint for the encrypted.

`ValidAfter` - The key can be used after this timestamp. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".

`ValidBefore` - The key can be used before this timestamp.

## See Also

* [google_service_account_key](https://www.terraform.io/docs/providers/google/r/service_account_key.html) in the _Terraform Provider Documentation_