# Terraform::Vault::PkiSecretBackendRole

Creates a role on an PKI Secret Backend for Vault.

## Properties

`Backend` - (Required) The path the PKI secret backend is mounted at, with no leading or trailing `/`s.

`Name` - (Required) The name to identify this role within the backend. Must be unique within the backend.

`Ttl` - (Optional) The TTL.

`MaxTtl` - (Optional) The maximum TTL.

`AllowLocalhost` - (Optional) Flag to allow certificates for localhost.

`AllowedDomains` - (Optional) List of allowed domains for certificates.

`AllowBareDomains` - (Optional) Flag to allow certificates matching the actual domain.

`AllowSubdomains` - (Optional) Flag to allow certificates matching subdomains.

`AllowGlobDomains` - (Optional) Flag to allow names containing glob patterns.

`AllowAnyName` - (Optional) Flag to allow any name.

`EnforceHostnames` - (Optional) Flag to allow only valid host names.

`AllowIpSans` - (Optional) Flag to allow IP SANs.

`AllowedUriSans` - (Optional) Defines allowed URI SANs.

`AllowedOtherSans` - (Optional) Defines allowed custom SANs.

`ServerFlag` - (Optional) Flag to specify certificates for server use.

`ClientFlag` - (Optional) Flag to specify certificates for client use.

`CodeSigningFlag` - (Optional) Flag to specify certificates for code signing use.

`EmailProtectionFlag` - (Optional) Flag to specify certificates for email protection use.

`KeyType` - (Optional) The type of generated keys.

`KeyBits` - (Optional) The number of bits of generated keys.

`KeyUsage` - (Optional) Specify the allowed key usage constraint on issued certificates.

`ExtKeyUsage` - (Optional) Specify the allowed extended key usage constraint on issued certificates.

`UseCsrCommonName` - (Optional) Flag to use the CN in the CSR.

`UseCsrSans` - (Optional) Flag to use the SANs in the CSR.

`Ou` - (Optional) The organization unit of generated certificates.

`Organization` - (Optional) The organization of generated certificates.

`Country` - (Optional) The country of generated certificates.

`Locality` - (Optional) The locality of generated certificates.

`Province` - (Optional) The province of generated certificates.

`StreetAddress` - (Optional) The street address of generated certificates.

`PostalCode` - (Optional) The postal code of generated certificates.

`GenerateLease` - (Optional) Flag to generate leases with certificates.

`NoStore` - (Optional) Flag to not store certificates in the storage backend.

`RequireCn` - (Optional) Flag to force CN usage.

`PolicyIdentifiers` - (Optional) Specify the list of allowed policies IODs.

`BasicConstraintsValidForNonCa` - (Optional) Flag to mark basic constraints valid when issuing non-CA certificates.


## See Also

* [vault_pki_secret_backend_role](https://www.terraform.io/docs/providers/vault/r/pki_secret_backend_role.html) in the _Terraform Provider Documentation_