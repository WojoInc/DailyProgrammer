# mirenc
# Description:
#
# Created by Thomas John Wesolowski <wojoinc@iastate.edu> on 8/6/17
from enum import Enum
from random import randrange


class keyspace(Enum):
    ALPHA_MIXED = 13


def encrypt():
    return 0


def decrypt():
    return 0
    # This is a placeholder


def gen_key_field(num_mrs, keyspace=keyspace.ALPHA_MIXED.value):
    """
    Make a random keyfield with an amount of mirrors specified by num_mrs

    """
    key = ""
    xpos = randrange(0, keyspace) % keyspace
    ypos = randrange(0, keyspace) % keyspace
    mirror_loc = []
    # add mirrors until num_mrs is reached
    while num_mrs > 0:
        # TODO change range to be a larger range, allowing for more random spread
        ort = randrange(-1, 2)
        mirror = 0x0000
        if ort >= 0:
            mirror |= (ort << 14)
            mirror |= (xpos << 7)
            mirror |= ypos
            print(str(ort) + " at (" + str(xpos) + "," + str(ypos) + ") " + format(mirror, '016b')
                  + " |" + format(mirror, '04x'))
            # add this back in if and when I figure out how to convert this hex key to readable plaintext
            # char1 = (mirror & 0xFF00) >> 8
            # char2 = (mirror & 0x00FF)
            # key += chr(char1)
            # key += chr(char2)
            key += format(mirror, '04x')
            num_mrs -= 1

            # add the current location to list of already added mirrors
            mirror_loc.append((xpos, ypos))
            # increment the position of the next mirror, wrap around if greater than the x or y limit
            # also check if the current position already has a mirror, and keep picking coordinates
            # until an empty space is found
            while (xpos, ypos) in mirror_loc:
                xpos = randrange(0, keyspace) % keyspace
                ypos = randrange(0, keyspace) % keyspace

    print(key)


gen_key_field(20)
