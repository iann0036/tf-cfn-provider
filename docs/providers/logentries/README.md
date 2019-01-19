# Logentries Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logentries**. The below arguments may be included as the key/value or JSON properties in the secret:

* `account_key` - (Required) The Logentries account key. See the Logentries [account key documentation](https://logentries.com/doc/accountkey/) for more information.

## Supported Resources

* [Terraform::Logentries::Log](Log.md)
* [Terraform::Logentries::Logset](Logset.md)