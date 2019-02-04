# Terraform::GitHub::UserGpgKey

Provides a GitHub user's GPG key resource.

This resource allows you to add/remove GPG keys from your user account.

## Properties

`ArmoredPublicKey` - (Required) Your public GPG key, generated in ASCII-armored format.
See [Generating a new GPG key](https://help.github.com/articles/generating-a-new-gpg-key/) for help on creating a GPG key.


## Return Values

### Fn::GetAtt

`Id` - The GitHub ID of the GPG key, e.g. `401586`.

`KeyId` - The key ID of the GPG key, e.g. `3262EFF25BA0D270`.

## See Also

* [github_user_gpg_key](https://www.terraform.io/docs/providers/github/r/user_gpg_key.html) in the _Terraform Provider Documentation_