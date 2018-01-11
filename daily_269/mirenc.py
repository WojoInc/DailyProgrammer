# mirenc
# Description:
#
# Created by Thomas John Wesolowski <wojoinc@iastate.edu> on 8/6/17
from enum import Enum
from random import randrange


class keyspace(Enum):
    ALPHA_MIXED = 13

def plot_keyfield(keyfield):
    """
    Slice the input keyfield and plot mirrors. Return a 1 dimensional array of mirrors
    :param keyfield:
    :return:
    """

    keys = [keyfield[i:i+4] for i in range(0,len(keyfield),4)]
    print(keys)
    mirrors = []
    ort = 0
    for key in keys:
        temp = int(key, 16)
        print(temp)

def encrypt(inString, keyfield):

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

    return key


plot_keyfield(gen_key_field(20))
