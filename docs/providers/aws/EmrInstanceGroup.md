# Terraform::AWS::EmrInstanceGroup

Provides an Elastic MapReduce Cluster Instance Group configuration.
See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/emr/) for more information.

~> **NOTE:** At this time, Instance Groups cannot be destroyed through the API nor
web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
Terraform will resize any Instance Group to zero when destroying the resource.

## Properties

### EbsConfig Properties

`Iops` - (Optional) The number of I/O operations per second (IOPS) that the volume supports.

`Size` - (Optional) The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

`Type` - (Optional) The volume type. Valid options are 'gp2', 'io1' and 'standard'.

`VolumesPerInstance` - (Optional) The number of EBS Volumes to attach per instance.


## Return Values

### Fn::GetAtt

`Id` - The EMR Instance ID.

## See Also

* [aws_emr_instance_group](https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html) in the _Terraform Provider Documentation_