
from frontTools import ttLib
tt=ttLib.TTFont('fonts/NotoSansSC-Regular.otf')
# number of glyphs
tt['maxp'].numGlyphs
s='汉'
u=s.encode('unicode_escape')
# extract hex
gs=tt.getGlyphSet()
tt.getGlyphName(27721)
gl=gs.get('cid44176')
from fontTools.pens.svgPathPen import SVGPathPen
>>> pen = SVGPathPen(gs)
>>> pen.moveTo((0,0))
>>> pen.getCommands()
'M0 0'
gl.draw(pen) # returns a ton of what seems to be garbage?
