# Terraform::Google::OrganizationPolicy

Allows management of Organization policies for a Google Organization. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Etag` - (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

`UpdateTime` - (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".

## See Also

* [google_organization_policy](https://www.terraform.io/docs/providers/google/r/organization_policy.html) in the _Terraform Provider Documentation_