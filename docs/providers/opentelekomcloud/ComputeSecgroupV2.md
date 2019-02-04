# Terraform::OpenTelekomCloud::ComputeSecgroupV2

Manages a V2 security group resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
security group.

`Name` - (Required) A unique name for the security group. Changing this
updates the `Name` of an existing security group.

`Description` - (Required) A description for the security group. Changing this
updates the `Description` of an existing security group.

`Rule` - (Optional) A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.

### Rule Properties

`FromPort` - (Required) An integer representing the lower bound of the port
range to open. Changing this creates a new security group rule.

`ToPort` - (Required) An integer representing the upper bound of the port
range to open. Changing this creates a new security group rule.

`IpProtocol` - (Required) The protocol type that will be allowed. Changing
this creates a new security group rule.

`Cidr` - (Optional) Required if `FromGroupId` or `Self` is empty. The IP range
that will be the source of network traffic to the security group. Use 0.0.0.0/0
to allow all IP addresses. Changing this creates a new security group rule. Cannot
be combined with `FromGroupId` or `Self`.

`FromGroupId` - (Optional) Required if `Cidr` or `Self` is empty. The ID of a
group from which to forward traffic to the parent group. Changing this creates a
new security group rule. Cannot be combined with `Cidr` or `Self`.

`Self` - (Optional) Required if `Cidr` and `FromGroupId` is empty. If true,
the security group itself will be added as a source to this ingress rule. Cannot
be combined with `Cidr` or `FromGroupId`.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Rule` - See Properties above.

## See Also

* [opentelekomcloud_compute_secgroup_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_secgroup_v2.html) in the _Terraform Provider Documentation_