# Terraform::AWS::CloudwatchDashboard

Provides a CloudWatch Dashboard resource.

## Properties

`DashboardName` - (Required) The name of the dashboard.

`DashboardBody` - (Required) The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).


## See Also

* [aws_cloudwatch_dashboard](https://www.terraform.io/docs/providers/aws/r/cloudwatch_dashboard.html) in the _Terraform Provider Documentation_