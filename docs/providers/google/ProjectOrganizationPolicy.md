# Terraform::Google::ProjectOrganizationPolicy

Allows management of Organization policies for a Google Project. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).

## Properties

`Project` - (Required) The project id of the project to set the policy for.

`Constraint` - (Required) The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

`Version` - (Optional) Version of the Policy. Default version is 0.

`BooleanPolicy` - (Optional) A boolean policy is a constraint that is either enforced or not. Structure is documented below.

`ListPolicy` - (Optional) A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.

`RestorePolicy` - (Optional) A restore policy is a constraint to restore the default policy. Structure is documented below.

`Enforced` - (Required) If true, then the Policy is enforced. If false, then any configuration is acceptable.

`SuggestedValues` - (Optional) The Google Cloud Console will try to default to a configuration that matches the value specified in this field.

`InheritFromParent` - (Optional) If set to true, the values from the effective Policy of the parent resource are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.

`All` - (Optional) The policy allows or denies all values.

`Values` - (Optional) The policy can define specific values that are allowed or denied.

`Default` - (Required) May only be set to true. If set, then the default Policy is restored.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

`UpdateTime` - (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

## See Also

* [google_project_organization_policy](https://www.terraform.io/docs/providers/google/r/project_organization_policy.html) in the _Terraform Provider Documentation_