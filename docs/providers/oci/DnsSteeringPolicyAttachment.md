# Terraform::OCI::DnsSteeringPolicyAttachment

This resource provides the Steering Policy Attachment resource in Oracle Cloud Infrastructure Dns service.

Creates a new attachment between a steering policy and a domain.
For the purposes of access control, the attachment is automatically placed
into the same compartment as the containing zone of the domain.

## Properties

`DisplayName` - (Optional) (Updatable) A user-friendly name for the steering policy attachment. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DomainName` - (Required) The attached domain within the attached zone.

`SteeringPolicyId` - (Required) The OCID of the attached steering policy.

`ZoneId` - (Required) The OCID of the attached zone.


## Return Values

### Fn::GetAtt

`DisplayName` - A user-friendly name for the steering policy attachment. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`ZoneId` - The OCID of the attached zone.

`CompartmentId` - The OCID of the compartment containing the steering policy attachment.

`Self` - The canonical absolute URL of the resource.

`DomainName` - The attached domain within the attached zone.

`TimeCreated` - The date and time the resource was created in "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.

`State` - The current state of the resource.

`Rtypes` - The record types covered by the attachment at the domain. The set of record types is determined by aggregating the record types from the answers defined in the steering policy.

`SteeringPolicyId` - The OCID of the attached steering policy.

`Id` - The OCID of the resource.

## See Also

* [oci_dns_steering_policy_attachment](https://www.terraform.io/docs/providers/oci/r/dns_steering_policy_attachment.html) in the _Terraform Provider Documentation_