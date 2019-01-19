# Terraform::MySQL::UserPassword

The `mysql_user_password` resource sets and manages a passwordd for a given 
user on a MySQL server.

~> **NOTE on MySQL Passwords:** This resource conflicts with the `password` 
   argument for `mysql_user`. This resource uses PGP encryption to avoid 
   storing unencrypted passwords in Terraform state.
   
~> **NOTE on How Passwords are Created:** This resource **automatically**
   generates a **random** password. The password will be a random UUID.

## Properties

TBC

## Return Values

### Fn::GetAtt

`KeyFingerprint` - The fingerprint of the PGP key used to encrypt the password.

`EncryptedPassword` - The encrypted password, base64 encoded.

## See Also

* [mysql_user_password](https://www.terraform.io/docs/providers/mysql/r/user_password.html) in the _Terraform Provider Documentation_