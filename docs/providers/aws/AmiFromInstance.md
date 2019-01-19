# Terraform::AWS::AmiFromInstance

The "AMI from instance" resource allows the creation of an Amazon Machine
Image (AMI) modelled after an existing EBS-backed EC2 instance.

The created AMI will refer to implicitly-created snapshots of the instance's
EBS volumes and mimick its assigned block device configuration at the time
the resource is created.

This resource is best applied to an instance that is stopped when this instance
is created, so that the contents of the created image are predictable. When
applied to an instance that is running, *the instance will be stopped before taking
the snapshots and then started back up again*, resulting in a period of
downtime.

Note that the source instance is inspected only at the initial creation of this
resource. Ongoing updates to the referenced instance will not be propagated into
the generated AMI. Users may taint or otherwise recreate the resource in order
to produce a fresh snapshot.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the created AMI.

## See Also

* [aws_ami_from_instance](https://www.terraform.io/docs/providers/aws/r/ami_from_instance.html) in the _Terraform Provider Documentation_