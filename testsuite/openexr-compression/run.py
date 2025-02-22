#!/usr/bin/env python

imagedir = "../common"

compressions = [
    "none",
    "rle",
    "zips",
    "zip",
    "piz",
    "pxr24",
    "b44",
    "b44a",
    "dwaa",
    "dwab",
]

anymatch = True
outputs = []
for c in compressions:
    outname = "out-" + c + ".exr"
    command += oiiotool("../common/tahoe-tiny.tif --compression " + c +
                        " -o " + outname)
    command += oiiotool(outname + " --echo \"" + outname + " compression "
                        + "{TOP.compression}\"")
    outputs += [ outname ]

outputs += [ "out.txt" ]
