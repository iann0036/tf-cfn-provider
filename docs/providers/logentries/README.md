# Logentries Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logentries**. The below arguments may be included as the key/value or JSON properties in the secret:

* `account_key` - (Required) The Logentries account key. This can also be specified with the `LOGENTRIES_ACCOUNT_KEY` environment variable. See the Logentries [account key documentation](https://logentries.com/doc/accountkey/) for more information.

## Supported Resources

* [Terraform::Logentries::Log](docs/providers/logentries/Log.md)
* [Terraform::Logentries::Logset](docs/providers/logentries/Logset.md)