# Terraform::AWS::S3BucketInventory

Provides a S3 bucket [inventory configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) resource.

## Properties

`Name` - (Required) Unique identifier of the inventory configuration for the bucket.

`IncludedObjectVersions` - (Required) Object filtering that accepts a prefix (documented below). Can be `All` or `Current`.

`Schedule` - (Required) Contains the frequency for generating inventory results (documented below).

`Destination` - (Required) Destination bucket where inventory list files are written (documented below).

`Enabled` - (Optional, Default: true) Specifies whether the inventory is enabled or disabled.

`Filter` - (Optional) Object filtering that accepts a prefix (documented below).

`OptionalFields` - (Optional) Contains the optional fields that are included in the inventory results.

### Encryption Properties

`SseKms` - (Optional) Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).

`SseS3` - (Optional) Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.

### Schedule Properties

`Frequency` - (Required) Specifies how frequently inventory results are produced. Can be `Daily` or `Weekly`.

### SseKms Properties

`KeyId` - (Required) The ARN of the KMS customer master key (CMK) used to encrypt the inventory file.

### Destination Properties

`Bucket` - (Required) The S3 bucket configuration where inventory results are published (documented below).

### Bucket Properties

`Prefix` - (Optional) The prefix that is prepended to all inventory results.

`BucketArn` - (Required) The Amazon S3 bucket ARN of the destination.

`Format` - (Required) Specifies the output format of the inventory results. Can be `CSV`, [`ORC`](https://orc.apache.org/) or [`Parquet`](https://parquet.apache.org/).

`AccountId` - (Optional) The ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.

`Encryption` - (Optional) Contains the type of server-side encryption to use to encrypt the inventory (documented below).


## See Also

* [aws_s3_bucket_inventory](https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory.html) in the _Terraform Provider Documentation_