let result = [];
$("div[role=dialog]", frames['main'].document).find('tr.grideven, tr.gridodd')
.each( 
    function(){
        $(this).find("td:eq(1)").css('color', 'green').text().split(',').
        forEach(wo_number_item =>  result.push(wo_number_item.slice(3,9)))
    } 
);
let uniq = [...new Set(result)];
result = [...uniq];
console.log(result);
