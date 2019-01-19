# Terraform::AWS::OrganizationsOrganization

Provides a resource to create an organization.

## Properties

`AwsServiceAccessPrincipals` - (Optional) List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `FeatureSet` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

`FeatureSet` - (Optional) Specify "ALL" (default) or "CONSOLIDATED_BILLING".


## Return Values

### Fn::GetAtt

`Arn` - ARN of the organization.

`Id` - Identifier of the organization.

`MasterAccountArn` - ARN of the master account.

`MasterAccountEmail` - Email address of the master account.

`MasterAccountId` - Identifier of the master account.

## See Also

* [aws_organizations_organization](https://www.terraform.io/docs/providers/aws/r/organizations_organization.html) in the _Terraform Provider Documentation_