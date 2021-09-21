Sub ShowBkMk()
    Dim Bmk() As String
    Dim x As Integer, J As Integer
 
    x = ActiveDocument.Bookmarks.Count
    ReDim Bmk(x)

    For J = 1 To x
        Bmk(J) = ActiveDocument.Bookmarks(J).Name
    
        Set r = ActiveDocument.Bookmarks(J).Range
        With r
            r.HighlightColorIndex = wdBrightGreen
            r.Font.ColorIndex = wdRed
            .InsertAfter Text:=ActiveDocument.Bookmarks(J).Name
            '.InsertParagraphAfter
        End With
    Next J
End Sub
