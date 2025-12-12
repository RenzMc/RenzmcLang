# Library UUID

## Overview

Library `uuid` menyediakan fungsi-fungsi untuk generating dan parsing UUID (Universally Unique Identifier) dengan nama fungsi dalam Bahasa Indonesia. Library ini mendukung semua UUID versions (UUID1, UUID3, UUID4, UUID5) dan namespace operations untuk unique identifier generation.

## Import Library

```python
dari renzmc.library.uuid impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.uuid impor buat_uuid4, buat_uuid1, uuid_valid, parse_uuid
```

## UUID Generation Functions

### buat_uuid1(node=None, clock_seq=None)

Membuat UUID berdasarkan host ID dan current time (UUID version 1).

**Parameter:**
- `node` (int): Node ID opsional (default: host MAC address)
- `clock_seq` (int): Clock sequence opsional (default: random)

**Return:**
- `string`: UUID version 1 string

**Contoh:**
```python
// Basic UUID1 generation
uuid1_default itu buat_uuid1()
tampilkan uuid1_default
// Output: "d9b2d3d0-1b3b-11ec-8b3a-0242ac130003"

// Dengan custom node
uuid1_custom itu buat_uuid1(node=123456789)
tampilkan uuid1_custom

// Dengan custom clock sequence
uuid1_clock itu buat_uuid1(clock_seq=12345)
tampilkan uuid1_clock

// Indonesian context - generate untuk transaksi
transaksi_uuid itu buat_uuid1()
tampilkan f"UUID Transaksi: {transaksi_uuid}")
```

### buat_uuid3(namespace, name)

Membuat UUID berdasarkan MD5 hash dari namespace dan name (UUID version 3).

**Parameter:**
- `namespace` (string): Namespace UUID
- `name` (string): String name untuk hash

**Return:**
- `string`: UUID version 3 string

**Contoh:**
```python
// Basic UUID3 dengan DNS namespace
dns_namespace itu dapatkan_namespace_dns()
uuid3_dns itu buat_uuid3(dns_namespace, "example.com")
tampilkan uuid3_dns
// Output: "6fa459ea-ee8a-3ca4-894e-db77e160355e"

// UUID3 dengan URL namespace
url_namespace itu dapatkan_namespace_url()
uuid3_url itu buat_uuid3(url_namespace, "https://www.example.com")
tampilkan uuid3_url

// Indonesian context - UUID untuk produk
namespace_produk itu dapatkan_namespace_dns()
uuid_produk itu buat_uuid3(namespace_produk, "buku.laskar.pelangi")
tampilkan f"UUID Produk: {uuid_produk}")

// UUID untuk user ID
uuid_user itu buat_uuid3(dns_namespace, "user.john.doe@example.com")
tampilkan f"UUID User: {uuid_user}")
```

### buat_uuid4()

Membuat UUID random (UUID version 4).

**Parameter:**
- Tidak ada parameter

**Return:**
- `string`: UUID version 4 string (random)

**Contoh:**
```python
// Basic UUID4 generation
uuid4_default itu buat_uuid4()
tampilkan uuid4_default
// Output: "f5c8d5e2-1b3b-11ec-8b3a-0242ac130003"

// Generate multiple UUID4
uuid_list itu []
untuk i dalam range(5):
    random_uuid itu buat_uuid4()
    uuid_list.tambah(random_uuid)

tampilkan "Multiple UUID4:"
untuk idx, uuid_val dalam enumerate(uuid_list):
    tampilkan f"  {idx + 1}: {uuid_val}")

// Indonesian context - generate untuk session
session_uuid itu buat_uuid4()
tampilkan f"UUID Session: {session_uuid}")

// Generate untuk order ID
order_uuid itu buat_uuid4()
tampilkan f"UUID Order: {order_uuid}")
```

### buat_uuid5(namespace, name)

Membuat UUID berdasarkan SHA-1 hash dari namespace dan name (UUID version 5).

**Parameter:**
- `namespace` (string): Namespace UUID
- `name` (string): String name untuk hash

**Return:**
- `string`: UUID version 5 string

**Contoh:**
```python
// Basic UUID5 dengan DNS namespace
dns_namespace itu dapatkan_namespace_dns()
uuid5_dns itu buat_uuid5(dns_namespace, "example.com")
tampilkan uuid5_dns
// Output: "2ed6657d-e927-568b-95e1-2665a8aea6a2"

// UUID5 dengan URL namespace
url_namespace itu dapatkan_namespace_url()
uuid5_url itu buat_uuid5(url_namespace, "https://www.example.com")
tampilkan uuid5_url

// Indonesian context - UUID untuk dokumen
namespace_dokumen itu dapatkan_namespace_dns()
uuid_dokumen itu buat_uuid5(namespace_dokumen, "dokumen.surat.keterangan.2023")
tampilkan f"UUID Dokumen: {uuid_dokumen}")

// UUID untuk kategori produk
uuid_kategori itu buat_uuid5(dns_namespace, "kategori.elektronik.smartphone")
tampilkan f"UUID Kategori: {uuid_kategori}")
```

## UUID Parsing dan Validation

### parse_uuid(uuid_string)

Meng-parse UUID string ke UUID object.

**Parameter:**
- `uuid_string` (string): UUID string untuk di-parse

**Return:**
- `string`: UUID object sebagai string (normalized format)

**Contoh:**
```python
// Parse valid UUID
valid_uuid itu "550e8400-e29b-41d4-a716-446655440000"
parsed_uuid itu parse_uuid(valid_uuid)
tampilkan parsed_uuid  // "550e8400-e29b-41d4-a716-446655440000"

// Parse UUID dalam format berbeda
uppercase_uuid itu "550E8400-E29B-41D4-A716-446655440000"
parsed_uppercase itu parse_uuid(uppercase_uuid)
tampilkan parsed_uppercase  // Normalized ke lowercase

// Parse dengan braces
braced_uuid itu "{550e8400-e29b-41d4-a716-446655440000}"
parsed_braced itu parse_uuid(braced_uuid)
tampilkan parsed_braced  // Tanpa braces

// Indonesian context
indonesian_uuid itu "123e4567-e89b-12d3-a456-426614174000"
parsed_indo itu parse_uuid(indonesian_uuid)
tampilkan f"UUID Indonesia: {parsed_indo}")
```

### uuid_valid(uuid_string)

Mengecek apakah UUID string valid.

**Parameter:**
- `uuid_string` (string): UUID string untuk dicek

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
// Valid UUIDs
valid1 itu uuid_valid("550e8400-e29b-41d4-a716-446655440000")
valid2 itu uuid_valid("{550e8400-e29b-41d4-a716-446655440000}")
valid3 itu uuid_valid("550E8400-E29B-41D4-A716-446655440000")

tampilkan f"Valid 1: {valid1}")  // True
tampilkan f"Valid 2: {valid2}")  // True
tampilkan f"Valid 3: {valid3}")  // True

// Invalid UUIDs
invalid1 itu uuid_valid("not-a-uuid")
invalid2 itu uuid_valid("550e8400-e29b-41d4-a716-44665544")    // Terlalu pendek
invalid3 itu uuid_valid("550e8400-e29b-41d4-a716-4466554400000")  // Terlalu panjang
invalid4 itu uuid_valid("g50e8400-e29b-41d4-a716-446655440000")  // Invalid hex

tampilkan f"Invalid 1: {invalid1}")  // False
tampilkan f"Invalid 2: {invalid2}")  // False
tampilkan f"Invalid 3: {invalid3}")  // False
tampilkan f"Invalid 4: {invalid4}")  // False

// Indonesian validation
test_uuids itu [
    "123e4567-e89b-12d3-a456-426614174000",  // Valid
    "user-session-123",                       // Invalid
    "{abc12345-def6-7890-abcd-ef1234567890}",  // Valid dengan braces
    "indonesia-uuid-12345"                   // Invalid
]

untuk test_uuid dalam test_uuids:
    is_valid itu uuid_valid(test_uuid)
    status itu "✓ Valid" jika is_valid lainnya "✗ Invalid"
    tampilkan f"{test_uuid}: {status}")
```

## Namespace Constants

### dapatkan_namespace_dns()

Mendapatkan DNS namespace.

**Return:**
- `string`: DNS namespace UUID

**Contoh:**
```python
dns_ns itu dapatkan_namespace_dns()
tampilkan dns_ns  // "6ba7b810-9dad-11d1-80b4-00c04fd430c8"

// Gunakan untuk UUID3/UUID5
uuid3_dns itu buat_uuid3(dns_ns, "example.com")
uuid5_dns itu buat_uuid5(dns_ns, "example.com")

tampilkan f"UUID3 with DNS: {uuid3_dns}")
tampilkan f"UUID5 with DNS: {uuid5_dns}")
```

### dapatkan_namespace_url()

Mendapatkan URL namespace.

**Return:**
- `string`: URL namespace UUID

**Contoh:**
```python
url_ns itu dapatkan_namespace_url()
tampilkan url_ns  // "6ba7b811-9dad-11d1-80b4-00c04fd430c8"

// Indonesian website
website_url itu "https://perpusnas.go.id"
uuid3_website itu buat_uuid3(url_ns, website_url)
tampilkan f"UUID Website: {uuid3_website}")
```

### dapatkan_namespace_oid()

Mendapatkan OID namespace.

**Return:**
- `string`: OID namespace UUID

**Contoh:**
```python
oid_ns itu dapatkan_namespace_oid()
tampilkan oid_ns  // "6ba7b812-9dad-11d1-80b4-00c04fd430c8"

// Untuk object identifiers
object_id itu "1.2.840.113556.1.4.321"
uuid3_oid itu buat_uuid3(oid_ns, object_id)
tampilkan f"UUID OID: {uuid3_oid}")
```

### dapatkan_namespace_x500()

Mendapatkan X500 namespace.

**Return:**
- `string`: X500 namespace UUID

**Contoh:**
```python
x500_ns itu dapatkan_namespace_x500()
tampilkan x500_ns  // "6ba7b814-9dad-11d1-80b4-00c04fd430c8"

// Untuk X.500 distinguished names
distinguished_name itu "CN=John Doe, OU=IT, O=Company, C=ID"
uuid3_x500 itu buat_uuid3(x500_ns, distinguished_name)
tampilkan f"UUID X500: {uuid3_x500}")
```

## Namespace Constants (Direct Access)

Library juga menyediakan akses langsung ke namespace constants:

```python
// Direct access constants
tampilkan NAMESPACE_DNS   // "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
tampilkan NAMESPACE_URL   // "6ba7b811-9dad-11d1-80b4-00c04fd430c8"
tampilkan NAMESPACE_OID   // "6ba7b812-9dad-11d1-80b4-00c04fd430c8"
tampilkan NAMESPACE_X500  // "6ba7b814-9dad-11d1-80b4-00c04fd430c8"

// Usage example
uuid_ns_example itu buat_uuid3(NAMESPACE_DNS, "namespace.example.com")
tampilkan uuid_ns_example
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.uuid impor *

tampilkan "=== Demo UUID Library ===")

// 1. Generate semua UUID versions
tampilkan "\n1. UUID Version Generation:")

// UUID1 (timestamp-based)
uuid1 itu buat_uuid1()
tampilkan f"UUID1 (Timestamp): {uuid1}")

// UUID3 (MD5 namespace-based)
dns_ns itu dapatkan_namespace_dns()
uuid3 itu buat_uuid3(dns_ns, "example.com")
tampilkan f"UUID3 (MD5): {uuid3}")

// UUID4 (random)
uuid4 itu buat_uuid4()
tampilkan f"UUID4 (Random): {uuid4}")

// UUID5 (SHA-1 namespace-based)
uuid5 itu buat_uuid5(dns_ns, "example.com")
tampilkan f"UUID5 (SHA-1): {uuid5}")

// 2. UUID validation
tampilkan "\n2. UUID Validation:")

test_uuids itu [
    "550e8400-e29b-41d4-a716-446655440000",  // Valid
    "{123e4567-e89b-12d3-a456-426614174000}", // Valid dengan braces
    "not-a-uuid",                               // Invalid
    "550e8400-e29b-41d4-a716-44665544",       // Invalid (too short)
    "g50e8400-e29b-41d4-a716-446655440000"    // Invalid (invalid hex)
]

untuk test_uuid dalam test_uuids:
    is_valid itu uuid_valid(test_uuid)
    status itu "✓ Valid" jika is_valid lainnya "✗ Invalid"
    tampilkan f"{test_uuid}: {status}")

// 3. UUID parsing
tampilkan "\n3. UUID Parsing:")

uuid_formats itu [
    "550e8400-e29b-41d4-a716-446655440000",    // Standard
    "{550e8400-e29b-41d4-a716-446655440000}",  // With braces
    "550E8400-E29B-41D4-A716-446655440000"      // Uppercase
]

untuk format_uuid dalam uuid_formats:
    coba
        parsed itu parse_uuid(format_uuid)
        tampilkan f"Original: {format_uuid}")
        tampilkan f"Parsed:   {parsed}")
    tangkap e:
        tampilkan f"Error parsing {format_uuid}: {e}")
    selesai
    tampilkan "")

// 4. Namespace operations
tampilkan "\n4. Namespace Operations:")

// Generate namespace-based UUIDs untuk Indonesian entities
indonesian_entities itu [
    ("website", "https://katalog.perpusnas.go.id"),
    ("email", "info@perpusnas.go.id"),
    ("produk", "buku.laskar.pelangi.andrea.hirata"),
    ("layanan", "perpustakaan.digital.nasional")
]

dns_ns itu dapatkan_namespace_dns()
url_ns itu dapatkan_namespace_url()

tampilkan "UUID3 (MD5) dengan DNS namespace:")
untuk entity_type, identifier dalam indonesian_entities:
    uuid3_result itu buat_uuid3(dns_ns, identifier)
    tampilkan f"  {entity_type} ({identifier}): {uuid3_result}")

tampilkan "\nUUID5 (SHA-1) dengan URL namespace:")
untuk entity_type, identifier dalam indonesian_entities:
    uuid5_result itu buat_uuid5(url_ns, identifier)
    tampilkan f"  {entity_type} ({identifier}): {uuid5_result}")

// 5. Consistent UUID generation
tampilkan "\n5. Consistent UUID Generation:")

// Same input should produce same UUID3/UUID5
identifier itu "user.john.doe@example.com"
uuid3_first itu buat_uuid3(dns_ns, identifier)
uuid3_second itu buat_uuid3(dns_ns, identifier)

uuid5_first itu buat_uuid5(dns_ns, identifier)
uuid5_second itu buat_uuid5(dns_ns, identifier)

tampilkan f"Identifier: {identifier}")
tampilkan f"UUID3 #1: {uuid3_first}")
tampilkan f"UUID3 #2: {uuid3_second}")
tampilkan f"UUID3 consistent: {uuid3_first == uuid3_second}")
tampilkan f"UUID5 #1: {uuid5_first}")
tampilkan f"UUID5 #2: {uuid5_second}")
tampilkan f"UUID5 consistent: {uuid5_first == uuid5_second}")

// 6. Different namespaces
tampilkan "\n6. Different Namespaces:")

identifier itu "test.example.com"

// Generate dengan berbagai namespaces
uuid3_dns itu buat_uuid3(NAMESPACE_DNS, identifier)
uuid3_url itu buat_uuid3(NAMESPACE_URL, identifier)
uuid3_oid itu buat_uuid3(NAMESPACE_OID, identifier)
uuid3_x500 itu buat_uuid3(NAMESPACE_X500, identifier)

tampilkan f"Identifier: {identifier}")
tampilkan f"DNS namespace:  {uuid3_dns}")
tampilkan f"URL namespace:  {uuid3_url}")
tampilkan f"OID namespace:  {uuid3_oid}")
tampilkan f"X500 namespace: {uuid3_x500}")

// 7. Batch UUID generation
tampilkan "\n7. Batch UUID Generation:")

// Generate multiple UUID4 untuk testing
batch_size itu 5
uuid_batch itu []

tampilkan f"Generating {batch_size} UUID4s:")
untuk i dalam range(batch_size):
    random_uuid itu buat_uuid4()
    uuid_batch.tambah(random_uuid)
    tampilkan f"  UUID {i+1}: {random_uuid}")

// Check uniqueness (all UUID4 should be unique)
unique_uuids itu set(uuid_batch)
tampilkan f"Total generated: {panjang(uuid_batch)}")
tampilkan f"Unique count: {panjang(unique_uuids)}")
tampilkan f"All unique: {panjang(uuid_batch) == panjang(unique_uuids)}")

// 8. UUID untuk aplikasi nyata
tampilkan "\n8. Real-world Application Scenarios:")

// E-commerce context
order_id itu buat_uuid4()
customer_id itu buat_uuid5(dns_ns, "customer.john.doe@email.com")
product_id itu buat_uuid3(dns_ns, "product.laptop.asus.rog")

tampilkan "E-commerce IDs:")
tampilkan f"Order ID:    {order_id}")
tampilkan f"Customer ID: {customer_id}")
tampilkan f"Product ID:  {product_id}")

// Document management
doc_namespace itu "dokumen.surat.keterangan"
doc_version itu "v1.2.3"
doc_id itu buat_uuid5(dns_ns, f"{doc_namespace}.{doc_version}")

tampilkan f"\nDocument ID: {doc_id}")

// Session management
user_email itu "session.user@example.com"
session_id itu buat_uuid5(url_ns, f"session.{user_email}.{getcwd()}")

tampilkan f"Session ID: {session_id}")

// 9. UUID format handling
tampilkan "\n9. UUID Format Handling:")

original_uuid itu buat_uuid4()

// Different representations
std_format itu parse_uuid(original_uuid)
uppercase_fmt itu huruf_besar(original_uuid)
with_braces itu f"{{{original_uuid}}}"

tampilkan f"Original:   {original_uuid}")
tampilkan f"Standard:   {std_format}")
tampilkan f"Uppercase:  {uppercase_fmt}")
tampilkan f"Braced:     {with_braces}")

// All should be valid
formats itu [std_format, uppercase_fmt, with_braces]
untuk idx, fmt dalam enumerate(formats):
    is_valid itu uuid_valid(fmt)
    tampilkan f"Format {idx+1} valid: {is_valid}")

// 10. Indonesian government context
tampilkan "\n10. Indonesian Government Context:")

// Generate UUIDs untuk government services
gov_services itu [
    ("e-ktp", "citizen.3201011234567890"),
    ("npwp", "tax.12.345.678.9-123.456.789"),
    ("sim", "license.driving.a.123456.dc.2023"),
    ("passport", "passport.a12345678.indonesia")
]

gov_ns itu dapatkan_namespace_dns()

tampilkan "Government Service UUIDs:"
untuk service_type, identifier dalam gov_services:
    service_uuid itu buat_uuid5(gov_ns, f"go.id.{service_type}.{identifier}")
    tampilkan f"  {service_type.upper()}: {service_uuid}")

// 11. Error handling
tampilkan "\n11. Error Handling:")

// Test invalid UUIDs
invalid_uuids itu [
    "",
    "not-a-uuid",
    "12345678-1234-1234-1234-123456789ab",  // Invalid hex
    "12345678-1234-1234-1234-123456789abcd", // Too long
    "g2345678-1234-1234-1234-123456789abc"  // Invalid hex g
]

tampilkan "Testing invalid UUIDs:")
untuk invalid_uuid dalam invalid_uuids:
    coba
        parsed_uuid itu parse_uuid(invalid_uuid)
        tampilkan f"  '{invalid_uuid}' -> {parsed_uuid} (unexpected!)")
    tangkap e:
        tampilkan f"  '{invalid_uuid}' -> Error: {str(e)}")
    selesai

// 12. Performance considerations
tampilkan "\n12. Performance Considerations:")

import time

// Benchmark UUID generation
start_time itu time.time()
iterations itu 1000

tampilkan f"Generating {iterations} UUID4s...")
untuk i dalam range(iterations):
    test_uuid itu buat_uuid4()

end_time itu time.time()
duration itu end_time - start_time

tampilkan f"Time taken: {duration:.4f} seconds")
tampilkan f"UUIDs per second: {iterations/duration:.0f}")

// Compare UUID3/UUID5 consistency
tampilkan "\nConsistency test:")
test_identifier itu "consistency.test.identifier"

uuid3_consistency_tests itu [buat_uuid3(dns_ns, test_identifier) untuk i dalam range(3)]
uuid5_consistency_tests itu [buat_uuid5(dns_ns, test_identifier) untuk i dalam range(3)]

uuid3_consistent itu panjang(set(uuid3_consistency_tests)) == 1
uuid5_consistent itu panjang(set(uuid5_consistency_tests)) == 1

tampilkan f"UUID3 consistency: {uuid3_consistent}")
tampilkan f"UUID5 consistency: {uuid5_consistent}")

tampilkan "\n=== Demo Selesai ===")
```

## Use Cases Umum

1. **Database Primary Keys**: UUID sebagai primary keys yang globally unique
2. **Distributed Systems**: Unique identifiers across multiple systems
3. **E-commerce**: Order IDs, customer IDs, transaction IDs
4. **Document Management**: Document versioning dan tracking
5. **Session Management**: User session identifiers
6. **API Authentication**: API keys dan token generation
7. **File Systems**: Unique filenames untuk prevent conflicts
8. **Government Services**: Citizen IDs, document numbers
9. **Microservices**: Correlation IDs untuk distributed tracing
10. **Caching**: Cache keys untuk distributed caching

## UUID Version Comparison

| Version | Generation Method | Uniqueness | Use Case |
|---------|-------------------|------------|----------|
| UUID1 | Timestamp + Host ID | Time-based | Ordered IDs, logging |
| UUID3 | MD5 Hash + Namespace | Deterministic | Consistent IDs from names |
| UUID4 | Random | Highest uniqueness | General purpose |
| UUID5 | SHA-1 Hash + Namespace | Deterministic | Consistent IDs from names |

## Security Considerations

- **UUID1**: Contains timestamp dan host MAC address (privacy concerns)
- **UUID4**: Most secure for random generation
- **UUID3**: Uses MD5 (not recommended for new systems)
- **UUID5**: Uses SHA-1 (more secure than UUID3)
- Never use UUIDs for security-critical purposes like passwords

## Performance Tips

- **UUID4**: Fastest untuk generation
- **UUID3/UUID5**: Slower but deterministic
- **UUID1**: Good untuk ordered requirements
- Use batch generation untuk multiple UUIDs
- Cache namespace UUIDs untuk repeated operations

## Indonesian Context

Library ini dirancang dengan dukungan penuh konteks Indonesia:
- Examples dengan Indonesian government services
- Support untuk Indonesian identifiers (KTP, NPWP, SIM)
- Integration patterns dengan Indonesian systems
- Namespace examples dengan .go.id domains
- Cultural context dalam use cases

## Best Practices

1. **Use UUID4** untuk general-purpose unique IDs
2. **Use UUID5** untuk deterministic IDs dari names
3. **Avoid UUID1** untuk privacy-sensitive applications
4. **Always validate** UUIDs dari external sources
5. **Use consistent namespaces** untuk UUID3/UUID5
6. **Store as string** untuk database compatibility
7. **Document namespace strategy** untuk team collaboration

## Error Handling

- Gunakan `coba...tangkap...selesai` untuk UUID operations
- `ValueError` untuk invalid UUID formats
- Validate UUIDs sebelum database operations
- Handle namespace generation errors
- Graceful fallback untuk invalid inputs

## Database Integration

```python
// PostgreSQL
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL
);

// MySQL
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

// SQLite
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);
```

## Standard Compliance

Library ini mengikuti RFC 4122 standards:
- Proper UUID format validation
- Correct namespace handling
- Standard version implementations
- Cross-platform compatibility
- RFC-compliant string representations