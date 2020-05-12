
def divblock(hh2):
    blocks = []
    block = []
    ele1 = []
    ele2 = []
    ele3 = []
    ele4 = []
    for i in range(0, len(hh2), 4):
        for j in range(0, len(hh2), 4):
            ele1.append(hh2[i][j])
            ele1.append(hh2[i][j + 1])
            ele1.append(hh2[i][j + 2])
            ele1.append(hh2[i][j + 3])
            ele2.append(hh2[i + 1][j])
            ele2.append(hh2[i + 1][j + 1])
            ele2.append(hh2[i + 1][j + 2])
            ele2.append(hh2[i + 1][j + 3])

            ele3.append(hh2[i+2][j])
            ele3.append(hh2[i+2][j + 1])
            ele3.append(hh2[i + 2][j + 2])
            ele3.append(hh2[i + 2][j + 3])

            ele4.append(hh2[i + 3][j])
            ele4.append(hh2[i + 3][j + 1])
            ele4.append(hh2[i + 3][j + 2])
            ele4.append(hh2[i + 3][j + 3])

            block.append(ele1)
            block.append(ele2)
            block.append(ele3)
            block.append(ele4)
            # print(block)
            blocks.append(block)
            ele1 = []
            ele2 = []
            ele3 = []
            ele4 = []
            block = []
    return blocks

def combinblocks(blocks):

    HHw = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []

    for i in range(0, 64*64):
        block = blocks[i]
        if i == 64*64 - 1:
            row1, row2, row3, row4 = addToRow(row1, row2, row3, row4, block)
            HHw.append(row1)
            HHw.append(row2)
            HHw.append(row3)
            HHw.append(row4)
            break
        if i% 64 == 0:
            if i == 0:
                row1, row2, row3, row4 = addToRow(row1, row2, row3, row4, block)
            else:
                HHw.append(row1)
                HHw.append(row2)
                HHw.append(row3)
                HHw.append(row4)
               
                row1 = []
                row2 = []
                row3 = []
                row4 = []
                row1, row2, row3, row4 = addToRow(row1, row2, row3, row4, block)

        elif i % 64 != 0:
            row1, row2, row3, row4 = addToRow(row1, row2, row3, row4, block)

    return HHw

def addToRow(row1, row2, row3, row4, block):

    row1.append(block[0][0])
    row1.append(block[0][1])
    row1.append(block[0][2])
    row1.append(block[0][3])
    
    row2.append(block[1][0])
    row2.append(block[1][1])
    row2.append(block[1][2])
    row2.append(block[1][3])

    row3.append(block[2][0])
    row3.append(block[2][1])
    row3.append(block[2][2])
    row3.append(block[2][3])

    row4.append(block[3][0])
    row4.append(block[3][1])
    row4.append(block[3][2])
    row4.append(block[3][3])
    return row1, row2, row3, row4