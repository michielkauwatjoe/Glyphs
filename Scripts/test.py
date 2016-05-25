#MenuTitle: Test Glyphs Scripting
# -*- coding: utf-8 -*-

from GlyphsApp import *
from vanilla import *

def test():
        print 'Current document', Glyphs.currentDocument
        print 'Number of fonts', len(Glyphs.fonts)

        for f in Glyphs.fonts:
            printFont(f)

        testVanilla()

def printFont(f):
    print '---'
    print f
    print 'Family', f.familyName
    print 'Masters', f.masters
    print 'Glyphs', len(f.glyphs)
    print 'Path', f.filepath

def testVanilla():
    w = Window((200, 70), "Window Demo")
    w.myButton = Button((10, 10, -10, 20), "My Button")
    w.myTextBox = TextBox((10, 40, -10, 17), "My Text Box")
    w.open()


if __name__ == "__main__":
        print 'Starting testing'
        test()
