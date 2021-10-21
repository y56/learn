// var target_wo_list =  ['303088'];
let target_wo_list = result;
for (const target_wo of target_wo_list){
    $("span[wonumber=" + target_wo + "]", frames['main'].document)
    .each(
        function(){
			console.log('CW');
			if (  $(this).closest('tr').find(':checkbox').attr("checked")  === undefined) {
				console.log('found an unchecked');
			};
            $(this).closest('tr').find(':checkbox').attr("checked", 'checked');
        }
    )
}
