# DNSMadeEasy Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dme**. The below arguments may be included as the key/value or JSON properties in the secret:

* `akey` - (Required) The DNSMadeEasy API key.
* `skey` - (Required) The DNSMadeEasy Secret key.
* `usesandbox` - (Optional) If true, the DNSMadeEasy sandbox will be
  used. This can also be specified with the `DME_USESANDBOX` shell environment
  variable.


## Supported Resources

* [Terraform::DME::Record](Record.md)