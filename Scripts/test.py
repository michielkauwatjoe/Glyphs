#MenuTitle: Test Glyphs Scripting
# -*- coding: utf-8 -*-

from GlyphsApp import *
from vanilla import *
from AppKit import NSDragOperationMove

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
    w = Window((800, 600), "Window Test")
    buildList(w)
    #w.myButton = Button((10, 10, -10, 20), "My Button")
    #w.myTextBox = TextBox((10, 40, -10, 17), "My Text Box")
    w.open()

def buildList(view):
    u"""
    Builds the font list.
    """
    dragSettings = dict(type="myInternalDragProofType", callback=None)
    selfDropSettings = dict(type="myInternalDragProofType",
                        callback=None, operation=NSDragOperationMove)

    view.styleList = List((4, 4, -4, -4), [],
        selectionCallback=None,
        doubleClickCallback=None,
        editCallback=None,
        dragSettings=dragSettings,
        allowsSorting=True,
        drawFocusRing=False,
        enableDelete=False,
        allowsMultipleSelection=True,
        allowsEmptySelection=True,
        drawHorizontalLines=True,
        showColumnTitles=True,
        selfDropSettings=selfDropSettings,
        columnDescriptions=getColumnDescriptions(),
        rowHeight=18,
    )

    styleItems = []

    for f in Glyphs.fonts:
        styleName = f.familyName + ' ' + f.masters[0].name
        d = dict(styleName=styleName)
        styleItems.append(d)

    view.styleList.set(styleItems)

def getColumnDescriptions():
    u"""
    Style list descriptors, sets headers and data structure.
    """
    return [
        # Also styleKey is added for selection reference, not displayed.
        dict(title='File name', key='styleName', width=250, editable=False),
        # 'magic' kludgy column so we'll get edit callbacks even though
        # none of our columns are editable
        dict(title="", key="dummy", width=200, editable=True),
    ]

if __name__ == "__main__":
        print 'Starting testing'
        test()
