# DNSimple Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dnsimple** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) The DNSimple API v2 token. Please note that this must be an [API v2 token](https://support.dnsimple.com/articles/api-access-token/). You can use either an User or Account token, but an Account token is recommended.
* `account` - (Required) The ID of the account associated with the token.


## Supported Resources

* [Terraform::DNSimple::Record](Record.md)