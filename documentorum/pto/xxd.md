> **`xxd`** is a command-line utility that creates a hexadecimal (hex) dump of a binary file or converts a hex dump back to binary.
> 

> **`xxd`** stands for **"hex dump"** (where "xx" represents hexadecimal notation, and "d" stands for "dump").
> 

> Useful Way:  `echo 'a' | xxd`
> 

QA:

- How to print the content in hex; and not it’s representation in **ASCII or EBCDIC? `-p`**

## List of Flags

| Flag | Description |
| --- | --- |
| `-b` | Binary dump (bits instead of hex). |
| `-c <cols>` | Format `<cols>` octets per line (default: 16). |
| `-E` | Use **EBCDIC** instead of **ASCII** for character display. |
| `-e` | Little-endian dump (forces 4-byte grouping). |
| `-g <n>` | Group output by `<n>` bytes (default: 2, or 4 for `-e`). |
| `-h` | Display help message and exit. |
| `-i` | Output in C include file style (as a byte array). |
| `-l <len>` | Stop after `<len>` octets. |
| `-o <offset>` | Add `<offset>` to displayed file position. |
| `-p` | Plain hexdump (no line numbers or ASCII). |
| `-r` | Reverse operation (convert hex dump back to binary). |
| `-s <seek>` | Start at `<seek>` bytes from the beginning (or end if negative). |
| `-u` | Use uppercase hex letters (default lowercase). |
| `-v` | Verbose (show all input, even if redundant). |

## References

- https://linux.die.net/man/1/xxd