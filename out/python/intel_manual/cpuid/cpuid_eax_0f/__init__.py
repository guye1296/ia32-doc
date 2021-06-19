from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 0FH and ECX = 0, the processor returns information about the bit-vector
representation of QoS monitoring resource types that are supported in the processor and maximum range of RMID
values the processor can use to monitor of any supported resource types. Each bit, starting from bit 1, corresponds
to a specific resource type if the bit is set. The bit position corresponds to the sub-leaf index (or ResID) that software
must use to query QoS monitoring capability available for that type. See Table 3-8.

When CPUID executes with EAX set to 0FH and ECX = n (n >= 1, and is a valid ResID), the processor returns information
software can use to program IA32_PQR_ASSOC, IA32_QM_EVTSEL MSRs before reading QoS data from the
IA32_QM_CTR MSR.
"""
CPUID_INTEL_RDT_MONITORING = 0xf

class CpuidEax0fEcx00(with_metaclass(BitFieldMeta, BitField)):
    """Intel Resource Director Technology (Intel RDT) Monitoring Enumeration Sub-leaf (EAX = 0FH, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax0fEcx01(with_metaclass(BitFieldMeta, BitField)):
    """L3 Cache Intel RDT Monitoring Capability Enumeration Sub-leaf (EAX = 0FH, ECX = 1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

