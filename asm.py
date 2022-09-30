import sys

GET_INPUT = False

#http://www.sco.com/developers/devspecs/gabi41.pdf
EI_NIDENT   = 16
ELF32_HALF  = 2
ELF32_WORD  = 4
ELF32_OFF   = 4
ELF32_ADDR  = 4
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

    def dump_header(self):
        print("ELF object file")
        print(self.h_ident)
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
        self.dump_header()

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
    elf.dump()