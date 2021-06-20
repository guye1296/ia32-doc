from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief VM-Instruction Error Numbers

VM-Instruction Error Numbers.
"""


VMX_ERROR_VMCALL = 0x1


VMX_ERROR_VMCLEAR_INVALID_PHYS_ADDR = 0x2


VMX_ERROR_VMCLEAR_INVALID_VMXON_PTR = 0x3


VMX_ERROR_VMLAUCH_NON_CLEAR_VMCS = 0x4


VMX_ERROR_VMRESUME_NON_LAUNCHED_VMCS = 0x5


VMX_ERROR_VMRESUME_CORRUPTED_VMCS = 0x6


VMX_ERROR_VMENTRY_INVALID_CONTROL_FIELDS = 0x7


VMX_ERROR_VMENTRY_INVALID_HOST_STATE = 0x8


VMX_ERROR_VMPTRLD_INVALID_PHYS_ADDR = 0x9


VMX_ERROR_VMPTRLD_VMXON_PTR = 0xa


VMX_ERROR_VMPTRLD_WRONG_VMCS_REVISION = 0xb


VMX_ERROR_VMREAD_VMWRITE_INVALID_COMPONENT = 0xc


VMX_ERROR_VMWRITE_READONLY_COMPONENT = 0xd


VMX_ERROR_VMXON_IN_VMX_ROOT_OP = 0xf


VMX_ERROR_VMENTRY_INVALID_VMCS_EXEC_PTR = 0x10


VMX_ERROR_VMENTRY_NON_LAUNCHED_EXEC_VMCS = 0x11


VMX_ERROR_VMENTRY_EXEC_VMCS_PTR = 0x12


VMX_ERROR_VMCALL_NON_CLEAR_VMCS = 0x13


VMX_ERROR_VMCALL_INVALID_VMEXIT_FIELDS = 0x14


VMX_ERROR_VMCALL_INVALID_MSEG_REVISION = 0x16


VMX_ERROR_VMXOFF_DUAL_MONITOR = 0x17


VMX_ERROR_VMCALL_INVALID_SMM_MONITOR = 0x18


VMX_ERROR_VMENTRY_INVALID_VM_EXEC_CTRL = 0x19


VMX_ERROR_VMENTRY_MOV_SS = 0x1a


VMX_ERROR_INVEPTVPID_INVALID_OPERAND = 0x1c


