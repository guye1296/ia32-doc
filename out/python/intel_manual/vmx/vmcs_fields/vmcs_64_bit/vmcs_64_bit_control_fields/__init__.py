from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief 64-Bit Control Fields

64-Bit Control Fields.
"""


VMCS_CTRL_IO_BITMAP_A = 0x2000


VMCS_CTRL_IO_BITMAP_B = 0x2002


VMCS_CTRL_MSR_BITMAP = 0x2004


VMCS_CTRL_VMEXIT_MSR_STORE = 0x2006


VMCS_CTRL_VMEXIT_MSR_LOAD = 0x2008


VMCS_CTRL_VMENTRY_MSR_LOAD = 0x200a


VMCS_CTRL_EXEC_VMCS_PTR = 0x200c


VMCS_CTRL_PML_ADDR = 0x200e


VMCS_CTRL_TSC_OFFSET = 0x2010


VMCS_CTRL_VAPIC_PAGEADDR = 0x2012


VMCS_CTRL_APIC_ACCESSADDR = 0x2014


VMCS_CTRL_POSTED_INTR_DESC = 0x2016


VMCS_CTRL_VMFUNC_CTRLS = 0x2018


VMCS_CTRL_EPTP = 0x201a


VMCS_CTRL_EOI_BITMAP_0 = 0x201c


VMCS_CTRL_EOI_BITMAP_1 = 0x201e


VMCS_CTRL_EOI_BITMAP_2 = 0x2020


VMCS_CTRL_EOI_BITMAP_3 = 0x2022


VMCS_CTRL_EPTP_LIST = 0x2024


VMCS_CTRL_VMREAD_BITMAP = 0x2026


VMCS_CTRL_VMWRITE_BITMAP = 0x2028


VMCS_CTRL_VIRTXCPT_INFO_ADDR = 0x202a


VMCS_CTRL_XSS_EXITING_BITMAP = 0x202c


VMCS_CTRL_ENCLS_EXITING_BITMAP = 0x202e


VMCS_CTRL_TSC_MULTIPLIER = 0x2032


