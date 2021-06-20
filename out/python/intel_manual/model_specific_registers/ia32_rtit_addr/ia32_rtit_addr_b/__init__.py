from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Region n End Address.
"""
IA32_RTIT_ADDR0_B = 0x581

IA32_RTIT_ADDR1_B = 0x583

IA32_RTIT_ADDR2_B = 0x585

IA32_RTIT_ADDR3_B = 0x587

class Ia32RtitAddrRegister(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    VIRTUAL_ADDRESS = BitFieldMember(
        "VIRTUAL_ADDRESS",
        """
        Virtual Address:
        Virtual Address.
        """,
        0,
        48
    )

    
    SIGN_EXT_VA = BitFieldMember(
        "SIGN_EXT_VA",
        """
        SignExt_VA:
        SignExt_VA.
        """,
        48,
        16
    )

    

IA32_DS_AREA = 0x600

IA32_TSC_DEADLINE = 0x6e0

IA32_PM_ENABLE = 0x770

IA32_HWP_CAPABILITIES = 0x771

IA32_HWP_REQUEST_PKG = 0x772

IA32_HWP_INTERRUPT = 0x773

IA32_HWP_REQUEST = 0x774

IA32_HWP_STATUS = 0x777

IA32_X2APIC_APICID = 0x802

IA32_X2APIC_VERSION = 0x803

IA32_X2APIC_TPR = 0x808

IA32_X2APIC_PPR = 0x80a

IA32_X2APIC_EOI = 0x80b

IA32_X2APIC_LDR = 0x80d

IA32_X2APIC_SIVR = 0x80f
