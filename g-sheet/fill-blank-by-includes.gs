function myFunction() {
  
    var sheet = SpreadsheetApp.getActiveSheet();
    var sheet2 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet2');
    var data = sheet.getDataRange().getValues();
    var data2 = sheet2.getDataRange().getValues();

    var arr = [];

    for (i = 0; i < data2.length; i++) {
        arr.push(data2[i][6]); // 0-indexing: i row, 6 col
    } 

    for (i = 0; i < data.length; i++) {

        num = data[i][0].toString();
        desc = data[i][1]; 
    
        if (!desc) { // if desc is blank, find in arr for all element containing num
        
            var col=2; // put the found element 
        
            for (k = 0; k < arr.length; k++) { // loop over all elements in arr
            
                var x = arr[k].toString(); 
            
                if (x.includes(num)) {
            
                    SpreadsheetApp.getActiveSheet().getRange(i+1,col).setValue(x);  
                    col += 1; // if find a next match, put it to the next col 
                }    
            }
        }
    }
}
