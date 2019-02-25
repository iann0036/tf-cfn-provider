# Logentries Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logentries** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `account_key` - (Required) The Logentries account key. See the Logentries [account key documentation](https://logentries.com/doc/accountkey/) for more information.

## Supported Resources

* [Terraform::Logentries::Log](Log.md)
* [Terraform::Logentries::Logset](Logset.md)