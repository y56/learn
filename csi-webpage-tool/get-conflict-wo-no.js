var result = [];
$("div[role=dialog]").find('tr.grideven, tr.gridodd')
.each( 
    function(){
        $(this).find("td:eq(1)").css('color', 'blue').text().split(',').
		forEach(wo_number_item =>  result.push(wo_number_item.slice(3,8)))
    } 
);
console.log(result);
