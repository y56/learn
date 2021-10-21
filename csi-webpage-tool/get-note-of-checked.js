var li = [];
L = $("input[type=checkbox][name=chk][checked=checked]", frames['main'].document).length;
for (i = 0; i < L; i++) {
  li.push($("input[type=checkbox][name=chk][checked=checked]", frames['main'].document)[i].closest('tr')['cells'][6]['innerHTML']);
}
uniq = [...new Set(li)];
console.log(uniq);
