# Terraform::AWS::OrganizationsPolicyAttachment

Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.

## Properties

`PolicyId` - (Required) The unique identifier (ID) of the policy that you want to attach to the target.

`TargetId` - (Required) The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.


## See Also

* [aws_organizations_policy_attachment](https://www.terraform.io/docs/providers/aws/r/organizations_policy_attachment.html) in the _Terraform Provider Documentation_