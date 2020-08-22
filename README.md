# leisihanzi
类似汉字

# Sourcing fonts

https://fonts.google.com/specimen/Noto+Sans+SC?subset=chinese-simplified&sidebar.open&selection.family=Noto+Sans+SC

Font file needs to include SVG paths.

# Mapping characters to glyphs

Use `cmap` table.

# References

## SVG

Excellent documentation on SVG paths from Mozilla: https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths


# TODO
 * extract SVG path from glyph
   * should be able to draw the path on something like https://www.w3schools.com/graphics/tryit.asp?filename=trysvg_path
   * posted a question on Gitter since i'm totally lost...
 * validate each glyph's height and width (ideally the same with monospace?)
 * 'draw' SVG path onto arbitrary canvas
 * transform the canvas into a matrix of pixels, say
 * compare 2 canvases

## Bonus points
 * be able to super-impose 2 characters and make common portions disappear! 

# Braindump

OTF format!

Microsoft has some docu: https://docs.microsoft.com/en-us/typography/opentype/spec/otff

The SVG table is optional, and may be used in OpenType fonts with TrueType, CFF or CFF2 outlines. For every SVG glyph description, there must be a corresponding TrueType, CFF or CFF2 glyph description in the font.

From <https://docs.microsoft.com/en-us/typography/opentype/spec/svg> 


Nice example of i in SVG: https://docs.microsoft.com/en-us/typography/opentype/spec/svg

Mapping char code to glyph: https://docs.microsoft.com/en-us/typography/opentype/spec/cmap

Free tool to view the font: https://www.babelstone.co.uk/Software/BabelMap.html

If I ever wanted to find out how a font engine worked: https://developer.apple.com/fonts/TrueType-Reference-Manual/RM02/Chap2.html#how_works

Found one on https://www.fontsquirrel.com/fonts/list/find_fonts?filter%5Bclassifications%5D%5B0%5D=monospaced&filter%5Blanguages%5D%5B0%5D=latinbasic!
Mozilla fira-mono: https://www.fontsquirrel.com/fonts/fira-mono?filter%5Bclassifications%5D%5B0%5D=monospaced&filter%5Blanguages%5D%5B0%5D=latinbasic


Droid Sans Mono has 900 glyphs: https://www.fontsquirrel.com/fonts/droid-sans-mono?filter%5Bclassifications%5D%5B0%5D=monospaced&filter%5Blanguages%5D%5B0%5D=english - better than the 1.4k above.

From a parsing perspective, this looks really handy: https://github.com/fonttools/fonttools/tree/master/Lib/fontTools

