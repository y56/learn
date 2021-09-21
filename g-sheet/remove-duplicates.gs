function myFunction() {
    var sheet = SpreadsheetApp.getActiveSheet();
    var data = sheet.getDataRange().getValues();
    var len = data.length;

    var col = 0; // compare duplicates at this col // assume already sorted by this col
    var pre = -5566; // 

    for (var i = 0; i < len; i++) {

        var cur = data[i][col_num_of_val];
    
        if (pre === cur) {
            sheet.deleteRow(i); 
            var data = sheet.getDataRange().getValues();
            len -= 1;
            i -= 1;
        } else { 
          pre = cur;
        }
    }
}
