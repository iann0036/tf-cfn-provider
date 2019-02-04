# Terraform::Vault::PkiSecretBackendRootSignIntermediate

Creates an PKI certificate.

## Properties

`Backend` - (Required) The PKI secret backend the resource belongs to.

`Csr` - (Required) The CSR.

`CommonName` - (Required) CN of intermediate to create.

`AltNames` - (Optional) List of alternative names.

`IpSans` - (Optional) List of alternative IPs.

`UriSans` - (Optional) List of alternative URIs.

`OtherSans` - (Optional) List of other SANs.

`Ttl` - (Optional) Time to leave.

`Format` - (Optional) The format of data.

`PrivateKeyFormat` - (Optional) The private key format.

`KeyType` - (Optional) The desired key type.

`KeyBits` - (Optional) The number of bits to use.

`MaxPathLength` - (Optional) The maximum path length to encode in the generated certificate.

`ExcludeCnFromSans` - (Optional) Flag to exclude CN from SANs.

`UseCsrValues` - (Optional) Preserve CSR values.

`PermittedDnsDomains` - (Optional) List of domains for which certificates are allowed to be issued.

`Ou` - (Optional) The organization unit.

`Organization` - (Optional) The organization.

`Country` - (Optional) The country.

`Locality` - (Optional) The locality.

`Province` - (Optional) The province.

`StreetAddress` - (Optional) The street address.

`PostalCode` - (Optional) The postal code.


## Return Values

### Fn::GetAtt

`Certificate` - The certificate.

`IssuingCa` - The issuing CA.

`CaChain` - The CA chain.

`Serial` - The serial.

## See Also

* [vault_pki_secret_backend_root_sign_intermediate](https://www.terraform.io/docs/providers/vault/r/pki_secret_backend_root_sign_intermediate.html) in the _Terraform Provider Documentation_