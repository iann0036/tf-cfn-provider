# Terraform::AWS::OrganizationsAccount

Provides a resource to create a member account in the current organization.

~> **Note:** Account management must be done from the organization's master account.

!> **WARNING:** Deleting this Terraform resource will only remove an AWS account from an organization. Terraform will not close the account. The member account must be prepared to be a standalone account beforehand. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) for more information.

## Properties

`Name` - (Required) A friendly name for the member account.

`Email` - (Required) The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

`IamUserAccessToBilling` - (Optional) If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

`RoleName` - (Optional) The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.


## Return Values

### Fn::GetAtt

`Id` - The AWS account id.

`Arn` - The ARN for this account.

## See Also

* [aws_organizations_account](https://www.terraform.io/docs/providers/aws/r/organizations_account.html) in the _Terraform Provider Documentation_