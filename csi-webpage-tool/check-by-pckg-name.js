var text_list =  ['20201209_htsai_25975', '20201211_htsai_25990'];
for (const text_item of text_list){
    $("td:contains('" + text_item + "')", frames['main'].document)[2].closest('tr')['childNodes'][0]['children'][0]['checked']=true
}
