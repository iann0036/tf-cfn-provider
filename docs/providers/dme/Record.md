# Terraform::DME::Record

Provides a DNSMadeEasy record resource.

## Properties

`Domainid` - (String, Required) The domain id to add the
record to.

`Name` - (Required) The name of the record `type` - (Required) The type of.

`Value` - (Required) The value of the record; its usage
will depend on the `type` (see below).

`Ttl` - (Integer, Optional) The TTL of the record.

`GtdLocation` - (String, Optional) The GTD Location of the record on Global Traffic Director enabled
domains; Unless GTD is enabled this should either be omitted or set to
"DEFAULT".


## Return Values

### Fn::GetAtt

`Name` - The name of the record.

`Type` - The type of the record.

`Value` - The value of the record.

`Ttl` - The TTL of the record.

`GtdLocation` - The GTD Location of the record on GTD enabled domains.

## See Also

* [dme_record](https://www.terraform.io/docs/providers/dme/r/record.html) in the _Terraform Provider Documentation_