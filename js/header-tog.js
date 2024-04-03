const tog = document.querySelector(".status-bar__i ");
const togCont = document.querySelector(".stauts-bar__profile-menu");
const icons = document.querySelector(".status-bar__i .fa-chevron-down");

console.log(togCont);
console.log(icons);

tog.addEventListener("click", function() {
    if (togCont.style.display === "none") {
        togCont.style.display = "block";
        icons.classList.remove("fa-chevron-down");
        icons.classList.add("fa-chevron-up");
    } else {
        togCont.style.display = "none";
        icons.classList.remove("fa-chevron-up");
        icons.classList.add("fa-chevron-down");
    }
});