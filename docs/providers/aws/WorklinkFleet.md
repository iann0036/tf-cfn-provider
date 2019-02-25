# Terraform::AWS::WorklinkFleet



## Properties

`Name` - (Required) A region-unique name for the AMI.

`AuditStreamArn` - (Optional) The ARN of the Amazon Kinesis data stream that receives the audit events.

`DeviceCaCertificate` - (Optional) The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.

`IdentityProvider` - (Optional) Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.

`DisplayName` - (Optional) The name of the fleet.

`Network` - (Optional) Provide this to allow manage the company network configuration for the fleet. Fields documented below.

`OptimizeForEndUserLocation` - (Optional) The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to `true`.

`VpcId` - (Required) The VPC ID with connectivity to associated websites.

`SubnetIds` - (Required) A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.

`SecurityGroupIds` - (Required) A list of security group IDs associated with access to the provided subnets.

`Type` - (Required) The type of identity provider.

`SamlMetadata` - (Required) The SAML metadata document provided by the customer’s identity provider.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the created WorkLink Fleet.

`Arn` - The ARN of the created WorkLink Fleet.

`CompanyCode` - The identifier used by users to sign in to the Amazon WorkLink app.

`CreatedTime` - The time that the fleet was created.

`LastUpdatedTime` - The time that the fleet was last updated.

## See Also

* [aws_worklink_fleet](https://www.terraform.io/docs/providers/aws/r/worklink_fleet.html) in the _Terraform Provider Documentation_