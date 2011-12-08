"""
canstat.py: contains Python equivalents of the function and constant
definitions in CANLIB's canstat.h, with some supporting functionality
specific to Python.

Copyright (C) 2010 Dynamic Controls

"""
import ctypes

class c_canStatus(ctypes.c_int):
    pass

canOK = 0
canERR_PARAM = -1
canERR_NOMSG = -2
canERR_NOTFOUND = -3
canERR_NOMEM = -4
canERR_NOCHANNELS = -5
canERR_RESERVED_3 = -6
canERR_TIMEOUT = -7
canERR_NOTINITIALIZED = -8
canERR_NOHANDLES = -9
canERR_INVHANDLE = -10
canERR_INIFILE = -11
canERR_DRIVER = -12
canERR_TXBUFOFL = -13
canERR_RESERVED_1 = -14
canERR_HARDWARE = -15
canERR_DYNALOAD = -16
canERR_DYNALIB = -17
canERR_DYNAINIT = -18
canERR_NOT_SUPPORTED = -19
canERR_RESERVED_5 = -20
canERR_RESERVED_6 = -21
canERR_RESERVED_2 = -22
canERR_DRIVERLOAD = -23
canERR_DRIVERFAILED = -24
canERR_NOCONFIGMGR = -25
canERR_NOCARD = -26
canERR_RESERVED_7 = -27
canERR_REGISTRY = -28
canERR_LICENSE = -29
canERR_INTERNAL = -30
canERR_NO_ACCESS = -31
canERR_NOT_IMPLEMENTED = -32
canERR__RESERVED = -33


canStatusLookupTable = {}
canStatusLookupTable[canOK] = "canOK"
canStatusLookupTable[canERR_PARAM] = "canERR_PARAM"
canStatusLookupTable[canERR_NOMSG] = "canERR_NOMSG"
canStatusLookupTable[canERR_NOTFOUND] = "canERR_NOTFOUND"
canStatusLookupTable[canERR_NOMEM] = "canERR_NOMEM"
canStatusLookupTable[canERR_NOCHANNELS] = "canERR_NOCHANNELS"
canStatusLookupTable[canERR_RESERVED_3] = "canERR_NOCHANNELS"
canStatusLookupTable[canERR_TIMEOUT] = "canERR_TIMEOUT"
canStatusLookupTable[canERR_NOTINITIALIZED] = "canERR_NOTINITIALIZED"
canStatusLookupTable[canERR_NOHANDLES] = "canERR_NOHANDLES"
canStatusLookupTable[canERR_INVHANDLE] = "canERR_INVHANDLE"
canStatusLookupTable[canERR_INIFILE] = "canERR_INIFILE"
canStatusLookupTable[canERR_DRIVER] = "canERR_DRIVER"
canStatusLookupTable[canERR_TXBUFOFL] = "canERR_TXBUFOFL"
canStatusLookupTable[canERR_RESERVED_1] = "canERR_RESERVED_1"
canStatusLookupTable[canERR_HARDWARE] = "canERR_HARDWARE"
canStatusLookupTable[canERR_DYNALOAD] = "canERR_DYNALOAD"
canStatusLookupTable[canERR_DYNALIB] = "canERR_DYNALIB"
canStatusLookupTable[canERR_DYNAINIT] = "canERR_DYNAINIT"
canStatusLookupTable[canERR_NOT_SUPPORTED] = "canERR_NOT_SUPPORTED"
canStatusLookupTable[canERR_RESERVED_5] = "canERR_RESERVED_5"
canStatusLookupTable[canERR_RESERVED_6] = "canERR_RESERVED_6"
canStatusLookupTable[canERR_RESERVED_2] = "canERR_RESERVED_2"
canStatusLookupTable[canERR_DRIVERLOAD] = "canERR_DRIVERLOAD"
canStatusLookupTable[canERR_DRIVERFAILED] = "canERR_DRIVERFAILED"
canStatusLookupTable[canERR_NOCONFIGMGR] = "canERR_NOCONFIGMGR"
canStatusLookupTable[canERR_NOCARD] = "canERR_NOCARD"
canStatusLookupTable[canERR_RESERVED_7] = "canERR_RESERVED_7"
canStatusLookupTable[canERR_REGISTRY] = "canERR_REGISTRY"
canStatusLookupTable[canERR_LICENSE] = "canERR_LICENSE"
canStatusLookupTable[canERR_INTERNAL] = "canERR_INTERNAL"
canStatusLookupTable[canERR_NO_ACCESS] = "canERR_NO_ACCESS"
canStatusLookupTable[canERR_NOT_IMPLEMENTED] = "canERR_NOT_IMPLEMENTED"
canStatusLookupTable[canERR__RESERVED] = "canERR__RESERVED"


def CANSTATUS_SUCCESS(status):
    return (status >= canOK)

canMSG_MASK = 0x00ff
canMSG_RTR = 0x0001
canMSG_STD = 0x0002
canMSG_EXT = 0x0004
canMSG_WAKEUP = 0x0008
canMSG_NERR = 0x0010
canMSG_ERROR_FRAME = 0x0020
canMSG_TXACK = 0x0040
canMSG_TXRQ = 0x0080

canMSGERR_MASK = 0xff00
canMSGERR_HW_OVERRUN = 0x0200
canMSGERR_SW_OVERRUN = 0x0400
canMSGERR_STUFF = 0x0800
canMSGERR_FORM = 0x1000
canMSGERR_CRC = 0x2000
canMSGERR_BIT0 = 0x4000
canMSGERR_BIT1 = 0x8000

canMSGERR_OVERRUN = 0x0600
canMSGERR_BIT = 0xC000
canMSGERR_BUSERR = 0xF800

canTRANSCEIVER_LINEMODE_NA = 0
canTRANSCEIVER_LINEMODE_SWC_SLEEP = 4
canTRANSCEIVER_LINEMODE_SWC_NORMAL = 5
canTRANSCEIVER_LINEMODE_SWC_FAST = 6
canTRANSCEIVER_LINEMODE_SWC_WAKEUP = 7
canTRANSCEIVER_LINEMODE_SLEEP = 8
canTRANSCEIVER_LINEMODE_NORMAL = 9
canTRANSCEIVER_LINEMODE_STDBY = 10
canTRANSCEIVER_LINEMODE_TT_CAN_H = 11
canTRANSCEIVER_LINEMODE_TT_CAN_L = 12
canTRANSCEIVER_LINEMODE_OEM1 = 13
canTRANSCEIVER_LINEMODE_OEM2 = 14
canTRANSCEIVER_LINEMODE_OEM3 = 15
canTRANSCEIVER_LINEMODE_OEM4 = 16
canTRANSCEIVER_RESNET_NA = 0
canTRANSCEIVER_RESNET_MASTER = 1
canTRANSCEIVER_RESNET_MASTER_STBY = 2
canTRANSCEIVER_RESNET_SLAVE = 3
