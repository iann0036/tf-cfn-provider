# Terraform::OCI::DnsRecord

This resource provides the Record resource in Oracle Cloud Infrastructure Dns service.

Replaces records in the specified zone with the records specified in the
request body. If a specified record does not exist, it will be created.
If the record exists, then it will be updated to represent the record in
the body of the request. If a record in the zone does not exist in the
request body, the record will be removed from the zone.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment the resource belongs to.

`Domain` - The fully qualified domain name where the record can be located.

`IsProtected` - A Boolean flag indicating whether or not parts of the record are unable to be explicitly managed.

`Rdata` - The record's data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see [Supported DNS Resource Record Types](https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm).

`RecordHash` - A unique identifier for the record within its zone.

`RrsetVersion` - The latest version of the record's zone in which its RRSet differs from the preceding version.

`Rtype` - The canonical name for the record's type, such as A or CNAME. For more information, see [Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

`Ttl` - The Time To Live for the record, in seconds.

`ZoneNameOrId` - The name or OCID of the target zone.

## See Also

* [oci_dns_record](https://www.terraform.io/docs/providers/oci/r/dns_record.html) in the _Terraform Provider Documentation_