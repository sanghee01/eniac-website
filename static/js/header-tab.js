const headerSpan = document.querySelectorAll(".status-bar__circle");
const headerBtn = document.querySelectorAll(".status-bar__button");

for (let i = 0; i < headerSpan.length; i++) {
    headerBtn[i].addEventListener("click", function(e) {
        e.preventDefault();
        for (let j = 0; j < headerSpan.length; j++) {
            headerSpan[j].classList.remove("is_on");
        }
        this.nextElementSibling.classList.add("is_on");

        // if (headerList.classList === "is_on") {
        //     headerList.classList.remove("is_on");
        // } else {
        //     headerList.classList.add("is_on");
        // }
    });
}

// is on일경우 제거