const toggle = document.querySelectorAll(".activity__comment-tog");
const submit = document.querySelectorAll(".activity__submit");

toggle.forEach((tog) =>
    tog.addEventListener("click", function(e) {
        const cont = tog.nextElementSibling;
        const icon = tog.children[0];

        if (cont.classList.contains("show")) {
            cont.classList.remove("show");
            icon.classList.remove("fa-chevron-up");
            icon.classList.add("fa-chevron-down");
        } else {
            cont.classList.add("show");
            icon.classList.remove("fa-chevron-down");
            icon.classList.add("fa-chevron-up");
        }
    })
);

submit.addEventListener("click", function(e) {
    e.preventDefault();
});