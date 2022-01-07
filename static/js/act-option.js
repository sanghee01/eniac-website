// 왜 찾을수없을가.. ?
let Select = document.querySelector(".activity__dropdown");
console.log(Select.dir);

let text = Select.options[Select.selectedIndex].innerText;
let value = Select.options[Select.selectedIndex].innerValue;
console.log(text);
console.log(value);