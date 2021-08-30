' source: https://www.mrexcel.com/board/threads/exporting-word-bookmarks-to-excel.1004800/

Sub WdBkMktoXL()
  Dim ObjExcel As Object, ObjWorkBook As Object, ObjWorksheet As Object
  Dim Bmk() As String
  Dim x As Integer, J As Integer

  Set ObjExcel = CreateObject("EXCEL.APPLICATION")
    Set ObjWorkBook = ObjExcel.Workbooks.Open("C:\Users\y56\Documents\bkmk-list.xlsx") 'output file
  Set ObjWorksheet = ObjWorkBook.Worksheets("Sheet1")

  x = ActiveDocument.Bookmarks.Count
  ReDim Bmk(x)
  For J = 1 To x
    Bmk(J) = ActiveDocument.Bookmarks(J).Name
    ObjWorksheet.Range("A" & J) = ActiveDocument.Bookmarks(J).Range.Text
    ObjWorksheet.Range("B" & J) = ActiveDocument.Bookmarks(J).Name
  Next J

  ObjWorkBook.Save
  ObjWorkBook.Close
  Set ObjWorksheet = Nothing
  Set ObjWorkBook = Nothing
  ObjExcel.Quit
  Set ObjExcel = Nothing
End Sub
