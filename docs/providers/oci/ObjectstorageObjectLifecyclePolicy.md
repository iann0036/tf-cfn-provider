# Terraform::OCI::ObjectstorageObjectLifecyclePolicy

This resource provides the Object Lifecycle Policy resource in Oracle Cloud Infrastructure Object Storage service.

Creates or replaces the object lifecycle policy for the bucket.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Rules` - The live lifecycle policy on the bucket.

`Action` - The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the  [Archival Storage tier](https://docs.cloud.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm). Rules using the action 'DELETE' permanently delete objects from buckets. 'ARCHIVE' and 'DELETE' are the only two supported actions at this time.

`IsEnabled` - A boolean that determines whether this rule is currently enabled.

`Name` - The name of the lifecycle rule to be applied.

`ObjectNameFilter` - A filter limiting object names that the rule will apply to.

`InclusionPrefixes` - An array of object name prefixes that the rule will apply to. An empty array means to include all objects.

`TimeAmount` - Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation to each object's Last-Modified time.

`TimeUnit` - The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC. Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.

`TimeCreated` - The date and time the object lifecycle policy was created, as described in [RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

## See Also

* [oci_objectstorage_object_lifecycle_policy](https://www.terraform.io/docs/providers/oci/r/objectstorage_object_lifecycle_policy.html) in the _Terraform Provider Documentation_