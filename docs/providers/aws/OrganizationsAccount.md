# Terraform::AWS::OrganizationsAccount

Provides a resource to create a member account in the current organization.

~> **Note:** Account management must be done from the organization's master account.

!> **WARNING:** Deleting this Terraform resource will only remove an AWS account from an organization. Terraform will not close the account. The member account must be prepared to be a standalone account beforehand. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The ARN for this account.

`Id` - The AWS account id.

## See Also

* [aws_organizations_account](https://www.terraform.io/docs/providers/aws/r/organizations_account.html) in the _Terraform Provider Documentation_