# Terraform::FlexibleEngine::CtsTrackerV1

Allows you to collect, store, and query cloud resource operation records.

## Properties

`BucketName` - (Required) The OBS bucket name for a tracker.

`FilePrefixName` - (Optional) The prefix of a log that needs to be stored in an OBS bucket.


## Return Values

### Fn::GetAtt

`Status` - The status of a tracker. The value is **enabled**.

`TrackerName` - The tracker name. Currently, only tracker **system** is available.

## See Also

* [flexibleengine_cts_tracker_v1](https://www.terraform.io/docs/providers/flexibleengine/r/cts_tracker_v1.html) in the _Terraform Provider Documentation_