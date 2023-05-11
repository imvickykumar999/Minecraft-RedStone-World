import SchemGenerator
import easygui
from os import getlogin
def main():
    MAXPAGE = 16
    PAGESIZE = 64
    INSTRUCTIONS = {"ADD": (0x00, "T"), "SUB": (0x10, "T"), "NOR": (0x20, "T"),
    "CMP": (0x30, "T"), "MOV": (0x40, "T"), "MST": (0x50, "T"),
    "MLD": (0x60, "T"), "ISW": (0x70, "B"), "PDC": (0x80, "W"),
    "RSH": (0x90, "S"), "INC": (0x94, "S"), "DEC": (0x98, "S"),
    "HLT": (0x9C, "N"), "RET": (0x9D, "N"), "PSHPC": (0x9E, "N"),
    "NOP": (0x9F, "N"), "NEG": (0xA0, "S"), "PSH": (0xA4, "S"),
    "POP": (0xA8, "S"), "CLR": (0xAC, "S"), "MSTD": (0xB0, "D"),
    "MLDD": (0xB4, "D"), "ABS": (0xB8, "S"), "DFU": (0xBC, "N"),
    "AWT": (0xBD, "N"), "JMP": (0xC0, "V")}
    defines = {}
    code, filePath = ReadTXT()
    for i, line in enumerate(code):     #remove comments and split code and pad with 0s
        line = line.split(";")[0]
        line = line.upper().split()
        if line == [] or line[0] == "":
            line=[";"]
        for j in range(max(0, 3-len(line))):
            line.append("0")
        code[i] = line
    for i in range(2):
        pages = [[0 for __ in range(PAGESIZE)] for _ in range(MAXPAGE)]
        pagepointer = 0
        instrpointer = 0
        immpointer = 0
        immediates = [0 for _ in range(16)]
        warnings = []
        for linenumber, line in enumerate(code):
            try:
                linenumber += 1
                opcode = line[0]
                arg1 = line[1]
                arg2 = line[2]
                if opcode == "@DEF":
                    if arg1 in defines.keys() and defines.get(arg1) != arg2:
                        warnings.append(f"Overwrote definition of '{arg1}' which previously was '{defines.get(arg1)}' with '{arg2}' in line '{linenumber}'")
                    defines[arg1] = arg2
                    continue
                elif opcode == "@IMM":
                    if arg2[:2] == "FP":
                        for i in line[3:]:
                            arg2 += i
                        arg2 = arg2[3:-1].split(",")
                        arg2[0] = float(arg2[0])
                        arg2[1] = int(arg2[1], base = 0)
                        arg2[2] = int(arg2[2], base = 0)
                        if arg2[1] + arg2[2] != 32:
                            raise ValueError(f"The bitcounts of fixed point immediate in line '{linenumber}' dont add up to 32 bit")
                        arg2 = str(int(arg2[0] * 2**arg2[2])&0xffff_ffff)
                    immediates[immpointer] = int(arg2, base = 0)
                    defines[arg1] = str(immpointer+128+64)
                    immpointer += 1
                    continue
                elif opcode[0] == ";":
                    continue
                elif opcode[0] == ".":
                    if opcode in defines.keys() and defines.get(opcode) != str(instrpointer):
                        warnings.append(f"Overwrote definition of '{opcode}' which previously was '{defines.get(opcode)}' with '{instrpointer}' in line '{linenumber}'")
                    defines[opcode] = str(instrpointer)
                    continue
                #opcode = defines.get(opcode, opcode)
                if opcode == "@PAGE":
                    pagepointer = int(defines.get(arg1, arg1), base = 0)
                    instrpointer = 0
                    continue
                #try instr dict
                binary, instrtype = INSTRUCTIONS.get(opcode, (0, "U"))
                #try conditional before converting to int
                if instrtype == "W":
                    pages[pagepointer][instrpointer] = binary + 8 * ("C" in arg1) + 4*("M" in arg1) + 2*("Z" in arg1) + 1*("!" in arg1 or "N" in arg1)
                    instrpointer += 1
                    continue
                #6bit arg
                elif instrtype == "V":
                    instrpointer+= 1
                    try:
                        arg1 = int(defines.get(arg1, arg1), base = 0)
                    except:
                        if i == 1:      #second run
                            warnings.append(f"Could not find a matching address for label '{arg1}' in line '{linenumber}'") 
                        continue
                    pages[pagepointer][instrpointer-1] = binary + arg1%64
                    
                    continue
                #convert to int
                arg1 = int(defines.get(arg1, arg1).removeprefix("R"), base = 0)
                arg2 = int(defines.get(arg2, arg2).removeprefix("R"), base = 0)
                #unknown inst
                if instrtype == "U":        #number or unknown
                    try:
                        pages[pagepointer][instrpointer] = int(opcode, base = 0)%256        #try converting to int
                    except: 
                        warnings.append(f"Unknown Instruction '{opcode}' in line '{linenumber}'")
                        continue
                #two args
                elif instrtype == "T":
                    if arg1 > 3 or arg2 > 3: warnings.append(f"Argument(s) too big in line '{linenumber}'")
                    pages[pagepointer][instrpointer] = binary + arg1%4 + (arg2%4)*4
                #big chungus arg
                elif instrtype == "B":
                    if arg1 > 15: warnings.append(f"Argument(s) too big in line '{linenumber}'")
                    pages[pagepointer][instrpointer] = binary + arg1%16
                #single argument
                elif instrtype == "S":
                    if arg1 > 3: warnings.append(f"Argument(s) too big in line '{linenumber}'")
                    pages[pagepointer][instrpointer] = binary + arg1%4
                #no argument
                elif instrtype == "N":
                    pages[pagepointer][instrpointer] = binary
                #two cycle instr
                elif instrtype == "D":
                    if arg1 > 3 or arg2 > 255: warnings.append(f"Argument(s) too big in line '{linenumber}'")
                    pages[pagepointer][instrpointer] = binary + arg1%4
                    instrpointer += 1
                    pages[pagepointer][instrpointer] = arg2%256

                instrpointer += 1
            except Exception as e:
                print(f"Something went wrong with Instruction '{line}' in line '{linenumber}'!")
                print(f"The Error raised is: '{e}'")
                exit()

    for pageid, page in enumerate(pages):
        if all(v == 0 for v in page):
            continue
        print("Page:", pageid)
        for k in range(PAGESIZE//8):
            for j in range(8):
                i = page[k+j*8]
                print(f"{str(k + j*8).rjust(2)}:",'0'*(8-len(bin(i).removeprefix('0b')))+bin(i).removeprefix('0b'), end = "  ")
            print()
    for e in warnings:
        print("Warning:",e)
    makeSchematic(pages, immediates, filePath, PAGESIZE)

def makeSchematic(pages, immediates, filePath, PAGESIZE):
    schem = SchemGenerator.Schematic()
    #generate instr rom
    for pageid, page in enumerate(pages):
        zlist = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]
        z = zlist[pageid] * 2
        for instrid in range(PAGESIZE//4):
            x = instrid*2
            instrs = [pages[pageid][i + instrid*4] for i in range(4)]
            for bit in range(8):
                y = -14 + bit*2
                ss = 0
                for instr in instrs:
                    ss = ss>>1
                    ss += ((instr&(1<<bit))>>bit)*8
                schem.setSSContainer((x , y, z), "barrel", ss)
    schem.move((11,-4,48))
    #immediates
    for immid, imm in enumerate(immediates):
        z = 2 - 2*(immid//8)
        x = (immid%8)*2
        for digit in range(8):
            y = -(7-digit)*2 -1
            ss = (imm & (15 << (digit*4))) >> (digit*4)
            schem.setSSContainer((x , y, z), "barrel", ss)
    schem.save(filePath)
    name = filePath.split('\\')[-1]
    #save to mchprs folder (you probably want to change this)
    schem.save(f"C:\\Users\\{getlogin()}\\OneDrive\\MCHPRS-master\\target\\release\\schems\\{name}")

def ReadTXT():
    #read the txt input file
    FilePath = easygui.fileopenbox('Select the Assembly .txt file', filetypes = ["*.txt"])

    if FilePath == None:    #no file selected smh
        raise Exception("No File selected")
    #check if file is .txt
    PathList = FilePath.rsplit('\\',1)
    Name, FileType = PathList[-1].rsplit(".",1)
    if "txt" != FileType:
        raise Exception(f'Selected file has the wrong format: ".{FileType}"')
    with open(FilePath) as file:
        Code = file.readlines()

    SavePath = f"{PathList[0]}\\{Name}_argon.schem" #change that to whatever should be added to the original name of the file
    return Code, SavePath

if __name__ == "__main__":
    main()