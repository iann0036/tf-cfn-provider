# Terraform::AWS::ElasticBeanstalkEnvironment

Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

Environments are often things such as `development`, `integration`, or
`production`.

## Properties

`Name` - (Required) A unique name for this Environment. This name is used
in the application URL.

`CnamePrefix` - (Optional) Prefix to use for the fully qualified DNS name of
the Environment.

`Description` - (Optional) Short description of the Environment.

`Tier` - (Optional) Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.

`WaitForReadyTimeout` - (Default: `20m`) The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.

`VersionLabel` - (Optional) The name of the Elastic Beanstalk Application Version
to use in deployment.


## Return Values

### Fn::GetAtt

`Id` - ID of the Elastic Beanstalk Environment.

`Name` - Name of the Elastic Beanstalk Environment.

`Description` - Description of the Elastic Beanstalk Environment.

`Tier` - The environment tier specified.

`Cname` - Fully qualified DNS name for the Environment.

`AutoscalingGroups` - The autoscaling groups used by this environment.

`Instances` - Instances used by this environment.

`LaunchConfigurations` - Launch configurations in use by this environment.

`LoadBalancers` - Elastic load balancers in use by this environment.

`Queues` - SQS queues in use by this environment.

`Triggers` - Autoscaling triggers in use by this environment.

## See Also

* [aws_elastic_beanstalk_environment](https://www.terraform.io/docs/providers/aws/r/elastic_beanstalk_environment.html) in the _Terraform Provider Documentation_