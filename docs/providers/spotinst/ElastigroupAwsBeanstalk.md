# Terraform::Spotinst::ElastigroupAwsBeanstalk

Provides a Spotinst AWS group resource using Elastic Beanstalk.

## Properties

`Name` - (Required) The group name.

`Region` - (Required) The AWS region your group will be created in. Cannot be changed after the group has been created.

`Description` - (Optional) The group description.

`Product` - (Required) Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.

`MaxSize` - (Required) The maximum number of instances the group should have at any time.

`MinSize` - (Required) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Required) The desired number of instances the group should have at any time.

`BeanstalkEnvironmentName` - (Required) The name of an existing Beanstalk environment.

`InstanceTypesSpot` - (Required) One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.


## See Also

* [spotinst_elastigroup_aws_beanstalk](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk.html) in the _Terraform Provider Documentation_