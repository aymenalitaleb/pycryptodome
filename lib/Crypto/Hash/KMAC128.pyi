from typing import Union
from types import ModuleType

Buffer = Union[bytes, bytearray, memoryview]

class KMAC_Hash(object):

    def __init__(self,
                 data: Buffer,
                 key: Buffer,
                 digest_bytes: int,
                 custom: Buffer,
                 oid_variant: str,
                 cshake: ModuleType,
                 rate: int) -> None: ...

    def update(self, data: Buffer) -> KMAC_Hash: ...

    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def verify(self, mac_tag: Buffer) -> None: ...
    def hexverify(self, hex_mac_tag: str) -> None: ...
    def new(self,
            data: Buffer = ...,
    	    digest_bytes: int = ...,
	        digest_bits: int = ...,
	        key: Buffer = ...,
            custom: Buffer = ...) -> KMAC_Hash: ...


def new(key: Buffer,
        data: Buffer = ...,
	    digest_bytes: int = ...,
	    digest_bits: int = ...,
        custom: Buffer = ...) -> KMAC_Hash: ...
