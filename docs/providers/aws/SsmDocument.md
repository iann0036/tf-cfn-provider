# Terraform::AWS::SsmDocument

Provides an SSM Document resource

~> **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
schema version you must recreate the resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CreatedDate` - The date the document was created.

`Description` - The description of the document.

`SchemaVersion` - The schema version of the document.

`DefaultVersion` - The default version of the document.

`Hash` - The sha1 or sha256 of the document content.

`HashType` - "Sha1" "Sha256". The hashing algorithm used when hashing the content.

`LatestVersion` - The latest version of the document.

`Owner` - The AWS user account of the person who created the document.

`Status` - "Creating", "Active" or "Deleting". The current status of the document.

`Parameter` - The parameters that are available to this document.

`PlatformTypes` - A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".

## See Also

* [aws_ssm_document](https://www.terraform.io/docs/providers/aws/r/ssm_document.html) in the _Terraform Provider Documentation_