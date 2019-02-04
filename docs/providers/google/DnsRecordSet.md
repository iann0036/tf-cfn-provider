# Terraform::Google::DnsRecordSet

Manages a set of DNS records within Google Cloud DNS. For more information see [the official documentation](https://cloud.google.com/dns/records/) and
[API](https://cloud.google.com/dns/api/v1/resourceRecordSets).

~> **Note:** The Google Cloud DNS API requires NS records be present at all
times. To accommodate this, when creating NS records, the default records
Google automatically creates will be silently overwritten.  Also, when
destroying NS records, Terraform will not actually remove NS records, but will
report that it did.

## Properties

`ManagedZone` - (Required) The name of the zone in which this record set will
reside.

`Name` - (Required) The DNS name this record set will apply to.

`Rrdatas` - (Required) The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding `\"` if you don't want your string to get split on spaces.

`Ttl` - (Required) The time-to-live of this record set (seconds).

`Type` - (Required) The DNS record set type.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.


## See Also

* [google_dns_record_set](https://www.terraform.io/docs/providers/google/r/dns_record_set.html) in the _Terraform Provider Documentation_