from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief 32-Bit Guest-State Fields

32-Bit Guest-State Fields.
"""


VMCS_GUEST_ES_LIMIT = 0x4800


VMCS_GUEST_CS_LIMIT = 0x4802


VMCS_GUEST_SS_LIMIT = 0x4804


VMCS_GUEST_DS_LIMIT = 0x4806


VMCS_GUEST_FS_LIMIT = 0x4808


VMCS_GUEST_GS_LIMIT = 0x480a


VMCS_GUEST_LDTR_LIMIT = 0x480c


VMCS_GUEST_TR_LIMIT = 0x480e


VMCS_GUEST_GDTR_LIMIT = 0x4810


VMCS_GUEST_IDTR_LIMIT = 0x4812


VMCS_GUEST_ES_ACCESS_RIGHTS = 0x4814


VMCS_GUEST_CS_ACCESS_RIGHTS = 0x4816


VMCS_GUEST_SS_ACCESS_RIGHTS = 0x4818


VMCS_GUEST_DS_ACCESS_RIGHTS = 0x481a


VMCS_GUEST_FS_ACCESS_RIGHTS = 0x481c


VMCS_GUEST_GS_ACCESS_RIGHTS = 0x481e


VMCS_GUEST_LDTR_ACCESS_RIGHTS = 0x4820


VMCS_GUEST_TR_ACCESS_RIGHTS = 0x4822


VMCS_GUEST_INTERRUPTIBILITY_STATE = 0x4824


VMCS_GUEST_ACTIVITY_STATE = 0x4826


VMCS_GUEST_SMBASE = 0x4828


VMCS_GUEST_SYSENTER_CS = 0x482a


VMCS_GUEST_PREEMPT_TIMER_VALUE = 0x482e


