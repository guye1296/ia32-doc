from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
The extended page-table mechanism (EPT) is a feature that can be used to support the virtualization of physical
memory. When EPT is in use, certain addresses that would normally be treated as physical addresses (and used to
access memory) are instead treated as guest-physical addresses. Guest-physical addresses are translated by
traversing a set of EPT paging structures to produce physical addresses that are used to access memory.
"""
class Eptp(with_metaclass(BitFieldMeta, BitField)):
    """The extended-page-table pointer (EPTP) contains the address of the base of EPT PML4 table,
as well as other EPT configuration information."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    TYPE = BitFieldMember(
        "TYPE",
        """
        EPT paging-structure memory type:

- 0 = Uncacheable (UC)

- 6 = Write-back (WB)

Other values are reserved:
        EPT paging-structure memory type:

- 0 = Uncacheable (UC)

- 6 = Write-back (WB)

Other values are reserved.
        """,
        0,
        3
    )

    
    PAGE_WALK_LENGTH = BitFieldMember(
        "PAGE_WALK_LENGTH",
        """
        This value is 1 less than the EPT page-walk length:
        This value is 1 less than the EPT page-walk length.
        """,
        3,
        3
    )

    
    ENABLE_ACCESS_AND_DIRTY_FLAGS = BitFieldMember(
        "ENABLE_ACCESS_AND_DIRTY_FLAGS",
        """
        Setting this control to 1 enables accessed and dirty flags for EPT:
        Setting this control to 1 enables accessed and dirty flags for EPT.
        """,
        6,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Bits N1:12 of the physical address of the 4-KByte aligned EPT PML4 table:
        Bits N1:12 of the physical address of the 4-KByte aligned EPT PML4 table.
        """,
        12,
        36
    )

    

class Epml4e(with_metaclass(BitFieldMeta, BitField)):
    """A 4-KByte naturally aligned EPT PML4 table is located at the physical address specified in bits 51:12 of the
extended-page-table pointer (EPTP), a VM-execution control field. An EPT
PML4 table comprises 512 64-bit entries (EPT PML4Es). An EPT PML4E is selected using the physical address
defined as follows:

- Bits 63:52 are all 0.

- Bits 51:12 are from the EPTP.

- Bits 11:3 are bits 47:39 of the guest-physical address.

- Bits 2:0 are all 0.

Because an EPT PML4E is identified using bits 47:39 of the guest-physical address, it controls access to a 512-
GByte region of the guest-physical-address space."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 512-GByte region controlled by this entry:
        Read access; indicates whether reads are allowed from the 512-GByte region controlled by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 512-GByte region controlled by this entry:
        Write access; indicates whether writes are allowed from the 512-GByte region controlled by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 512-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 512-GByte region controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 512-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 512-GByte region controlled by this entry.
        """,
        2,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 512-GByte region
controlled by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 512-GByte region
controlled by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 512-GByte region
controlled by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 512-GByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry:
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,
        12,
        36
    )

    

class EptPdpte1gb(with_metaclass(BitFieldMeta, BitField)):
    """Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 1-GByte page referenced by this entry:
        Read access; indicates whether reads are allowed from the 1-GByte page referenced by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 1-GByte page referenced by this entry:
        Write access; indicates whether writes are allowed from the 1-GByte page referenced by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 1-GByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte page controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 1-GByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte page controlled by this entry.
        """,
        2,
        1
    )

    
    TYPE = BitFieldMember(
        "TYPE",
        """
        EPT memory type for this 1-GByte page:
        EPT memory type for this 1-GByte page.
        """,
        3,
        3
    )

    
    IGNORE_PAT = BitFieldMember(
        "IGNORE_PAT",
        """
        Ignore PAT memory type for this 1-GByte page:
        Ignore PAT memory type for this 1-GByte page.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Must be 1 (otherwise, this entry references an EPT page directory):
        Must be 1 (otherwise, this entry references an EPT page directory).
        """,
        7,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    DIRTY = BitFieldMember(
        "DIRTY",
        """
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 1-GByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 1-GByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.
        """,
        9,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte page controlled
by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry:
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,
        30,
        18
    )

    
    SUPPRESS_VE = BitFieldMember(
        "SUPPRESS_VE",
        """
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored:
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.
        """,
        63,
        1
    )

    

class EptPdpte(with_metaclass(BitFieldMeta, BitField)):
    """Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that References an EPT Page Directory."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 1-GByte region controlled by this entry:
        Read access; indicates whether reads are allowed from the 1-GByte region controlled by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 1-GByte region controlled by this entry:
        Write access; indicates whether writes are allowed from the 1-GByte region controlled by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 1-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte region controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 1-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte region controlled by this entry.
        """,
        2,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte region
controlled by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry:
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,
        12,
        36
    )

    

class EptPde2mb(with_metaclass(BitFieldMeta, BitField)):
    """Format of an EPT Page-Directory Entry (PDE) that Maps a 2-MByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 2-MByte page referenced by this entry:
        Read access; indicates whether reads are allowed from the 2-MByte page referenced by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 2-MByte page referenced by this entry:
        Write access; indicates whether writes are allowed from the 2-MByte page referenced by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte page controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte page controlled by this entry.
        """,
        2,
        1
    )

    
    TYPE = BitFieldMember(
        "TYPE",
        """
        EPT memory type for this 2-MByte page:
        EPT memory type for this 2-MByte page.
        """,
        3,
        3
    )

    
    IGNORE_PAT = BitFieldMember(
        "IGNORE_PAT",
        """
        Ignore PAT memory type for this 2-MByte page:
        Ignore PAT memory type for this 2-MByte page.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Must be 1 (otherwise, this entry references an EPT page table):
        Must be 1 (otherwise, this entry references an EPT page table).
        """,
        7,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    DIRTY = BitFieldMember(
        "DIRTY",
        """
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 2-MByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 2-MByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.
        """,
        9,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte page controlled
by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry:
        Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,
        21,
        27
    )

    
    SUPPRESS_VE = BitFieldMember(
        "SUPPRESS_VE",
        """
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored:
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.
        """,
        63,
        1
    )

    

class EptPde(with_metaclass(BitFieldMeta, BitField)):
    """Format of an EPT Page-Directory Entry (PDE) that References an EPT Page Table."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 2-MByte region controlled by this entry:
        Read access; indicates whether reads are allowed from the 2-MByte region controlled by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 2-MByte region controlled by this entry:
        Write access; indicates whether writes are allowed from the 2-MByte region controlled by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte region controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte region controlled by this entry.
        """,
        2,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte region
controlled by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned EPT page table referenced by this entry:
        Physical address of 4-KByte aligned EPT page table referenced by this entry.
        """,
        12,
        36
    )

    

class EptPte(with_metaclass(BitFieldMeta, BitField)):
    """Format of an EPT Page-Table Entry that Maps a 4-KByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        Read access; indicates whether reads are allowed from the 4-KByte page referenced by this entry:
        Read access; indicates whether reads are allowed from the 4-KByte page referenced by this entry.
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        Write access; indicates whether writes are allowed from the 4-KByte page referenced by this entry:
        Write access; indicates whether writes are allowed from the 4-KByte page referenced by this entry.
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 4-KByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 4-KByte page controlled by this entry:
        If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 4-KByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 4-KByte page controlled by this entry.
        """,
        2,
        1
    )

    
    TYPE = BitFieldMember(
        "TYPE",
        """
        EPT memory type for this 4-KByte page:
        EPT memory type for this 4-KByte page.
        """,
        3,
        3
    )

    
    IGNORE_PAT = BitFieldMember(
        "IGNORE_PAT",
        """
        Ignore PAT memory type for this 4-KByte page:
        Ignore PAT memory type for this 4-KByte page.
        """,
        6,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 4-KByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 4-KByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.
        """,
        8,
        1
    )

    
    DIRTY = BitFieldMember(
        "DIRTY",
        """
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 4-KByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0:
        If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 4-KByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.
        """,
        9,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 4-KByte page controlled
by this entry. If that control is 0, this bit is ignored:
        Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 4-KByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of the 4-KByte page referenced by this entry:
        Physical address of the 4-KByte page referenced by this entry.
        """,
        12,
        36
    )

    
    SUPPRESS_VE = BitFieldMember(
        "SUPPRESS_VE",
        """
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored:
        Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.
        """,
        63,
        1
    )

    

class EptEntry(with_metaclass(BitFieldMeta, BitField)):
    """Format of a common EPT Entry."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    READ = BitFieldMember(
        "READ",
        """
        :
        
        """,
        0,
        1
    )

    
    WRITE = BitFieldMember(
        "WRITE",
        """
        :
        
        """,
        1,
        1
    )

    
    EXECUTE = BitFieldMember(
        "EXECUTE",
        """
        :
        
        """,
        2,
        1
    )

    
    TYPE = BitFieldMember(
        "TYPE",
        """
        :
        
        """,
        3,
        3
    )

    
    IGNORE_PAT = BitFieldMember(
        "IGNORE_PAT",
        """
        :
        
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        :
        
        """,
        7,
        1
    )

    
    ACCESSED = BitFieldMember(
        "ACCESSED",
        """
        :
        
        """,
        8,
        1
    )

    
    DIRTY = BitFieldMember(
        "DIRTY",
        """
        :
        
        """,
        9,
        1
    )

    
    USER_MODE_EXECUTE = BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        :
        
        """,
        10,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        :
        
        """,
        12,
        36
    )

    
    SUPPRESS_VE = BitFieldMember(
        "SUPPRESS_VE",
        """
        :
        
        """,
        63,
        1
    )

    
