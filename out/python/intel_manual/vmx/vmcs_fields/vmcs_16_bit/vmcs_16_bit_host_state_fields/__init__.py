from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
16-Bit Host-State Fields.
"""
VMCS_HOST_ES_SEL = 0xc00

VMCS_HOST_CS_SEL = 0xc02

VMCS_HOST_SS_SEL = 0xc04

VMCS_HOST_DS_SEL = 0xc06

VMCS_HOST_FS_SEL = 0xc08

VMCS_HOST_GS_SEL = 0xc0a

VMCS_HOST_TR_SEL = 0xc0c
