import sys

GET_INPUT = False

#http://www.sco.com/developers/devspecs/gabi41.pdf
ELF32_HALF  = 2
ELF32_WORD  = 4
ELF32_OFF   = 4
ELF32_ADDR  = 4

EI_MAG0     = 0
EI_MAG1     = 1
EI_MAG2     = 2
EI_MAG3     = 3
EI_CLASS    = 4
EI_DATA     = 5
EI_VERSION  = 6
EI_PAD      = 7
EI_NIDENT   = 16

ELFCLASSNONE    = b'\x00'
ELFCLASS32      = b'\x01'
ELFCLASS64      = b'\x02'

ELFDATANONE     = b'\x00'
ELFDATA2LSB     = b'\x01'
ELFDATA2MSB     = b'\x02'

EV_NONE         = b'\x00'
EV_CURRENT      = b'\x01'

PAD_VAL         = b'\x00'

class elf32:
    def __init__(self):
        self.h_ident       = [b'\xff']*EI_NIDENT
        self.h_type        = [b'\xff']*ELF32_HALF
        self.h_machine     = [b'\xff']*ELF32_HALF
        self.h_version     = [b'\xff']*ELF32_WORD
        self.h_entry       = [b'\xff']*ELF32_ADDR
        self.h_phoff       = [b'\xff']*ELF32_OFF
        self.h_shoff       = [b'\xff']*ELF32_OFF
        self.h_flags       = [b'\xff']*ELF32_WORD
        self.h_hsize       = [b'\xff']*ELF32_HALF
        self.h_phentsize   = [b'\xff']*ELF32_HALF
        self.h_phnum       = [b'\xff']*ELF32_HALF
        self.h_shentsize   = [b'\xff']*ELF32_HALF
        self.h_shnum       = [b'\xff']*ELF32_HALF
        self.h_shstrrndx   = [b'\xff']*ELF32_HALF

    def dump_h_ident(self):
        print(self.h_ident)

    def dump_h(self):
        self.dump_h_ident()
        print(self.h_type)
        print(self.h_machine)
        print(self.h_version)
        print(self.h_entry)
        print(self.h_phoff)
        print(self.h_shoff)
        print(self.h_flags)
        print(self.h_hsize)
        print(self.h_phentsize)
        print(self.h_phnum)
        print(self.h_shentsize)
        print(self.h_shnum)
        print(self.h_shstrrndx)
        
    def dump(self):
        print("ELF object file")
        self.dump_h()

def parse_assembly():
    return False

if __name__ == "__main__":
    print("ARM Assembler\n")
    if GET_INPUT == True:
        if len(sys.argv) == 3 and (sys.argv[1][-2:] == ".s") and (sys.argv[2][-2:] == ".o"):
            print("input OK")
        else:
            print("invalid arguments")
    
    elf = elf32()

    # build header ident
    elf.h_ident[EI_MAG0]    = b'\x7f'
    elf.h_ident[EI_MAG1]    = b'E'
    elf.h_ident[EI_MAG2]    = b'L'
    elf.h_ident[EI_MAG3]    = b'F'
    elf.h_ident[EI_CLASS]   = ELFCLASS32    # 32-bit objects
    elf.h_ident[EI_DATA]    = ELFDATA2LSB   # 2's complement, little endian
    elf.h_ident[EI_VERSION] = EV_CURRENT
    elf.h_ident[EI_VERSION + 1 : EI_NIDENT] = [PAD_VAL] * (EI_NIDENT - EI_VERSION - 1)

    f = open("out.o", "wb") # write binary mode
    for x in elf.h_ident:
        print(x)
        f.write(x)
    f.close()
