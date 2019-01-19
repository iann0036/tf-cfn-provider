# Terraform::Google::DnsRecordSet

Manages a set of DNS records within Google Cloud DNS. For more information see [the official documentation](https://cloud.google.com/dns/records/) and
[API](https://cloud.google.com/dns/api/v1/resourceRecordSets).

~> **Note:** The Google Cloud DNS API requires NS records be present at all
times. To accommodate this, when creating NS records, the default records
Google automatically creates will be silently overwritten.  Also, when
destroying NS records, Terraform will not actually remove NS records, but will
report that it did.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [google_dns_record_set](https://www.terraform.io/docs/providers/google/r/dns_record_set.html) in the _Terraform Provider Documentation_