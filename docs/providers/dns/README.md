# DNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dns** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `server` - (Required) The IPv4 address of the DNS server to send updates to.
* `port` - (Optional) The target UDP port on the server where updates are sent to. Defaults to `53`.
* `transport` - (Optional) Transport to use for DNS queries. Valid values are `udp`, `udp4`, `udp6`, `tcp`, `tcp4`, or `tcp6`. Any UDP transport will retry automatically with the equivalent TCP transport in the event of a truncated response. Defaults to `udp`.
* `timeout` - (Optional) Timeout for DNS queries. Valid values are durations expressed as `500ms`, etc. or a plain number which is treated as whole seconds.
* `retries` - (Optional) How many times to retry on connection timeout. Defaults to `3`.
* `key_name` - (Optional) The name of the TSIG key used to sign the DNS update messages.
* `key_algorithm` - (Optional; Required if `key_name` is set) When using TSIG authentication, the algorithm to use for HMAC. Valid values are `hmac-md5`, `hmac-sha1`, `hmac-sha256` or `hmac-sha512`.
* `key_secret` - (Optional; Required if `key_name` is set)
    A Base64-encoded string containing the shared secret to be used for TSIG.


## Supported Resources

* [Terraform::DNS::ARecordSet](ARecordSet.md)
* [Terraform::DNS::AaaaRecordSet](AaaaRecordSet.md)
* [Terraform::DNS::CnameRecord](CnameRecord.md)
* [Terraform::DNS::MxRecordSet](MxRecordSet.md)
* [Terraform::DNS::NsRecordSet](NsRecordSet.md)
* [Terraform::DNS::PtrRecord](PtrRecord.md)
* [Terraform::DNS::TxtRecordSet](TxtRecordSet.md)