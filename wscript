#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
# DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'ZaghawaBeria'
FAMILY = APPNAME
DESC_SHORT = "Font for the Beria script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

designspace('source/' + FAMILY + '.designspace',
    target = process('${DS:FILENAME_BASE}.ttf',
       cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo'])),
    opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/features.feax", to_ufo = 'True'),
    pdf = fret(params='-oi')
)

