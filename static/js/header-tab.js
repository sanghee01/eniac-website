const headerSpan = document.querySelectorAll(".status-bar__circle");
const headerBtn = document.querySelectorAll(".status-bar__button");

console.log(this.location.href);

for (let i = 0; i < tabList.length; i++) {
    headerBtn[i].addEventListener("click", function(e) {
        if (this.location.href === "http://127.0.0.1:8000/notice") {
            // 잴 앞에거만 냄겨놓고 잴 앞에것만 is_on실행
            headerSpan[0].classList.add("is_on");
        } else if (this.location.href === "http://127.0.0.1:8000/project") {
            // 잴 앞에거만 냄겨놓고 잴 앞에것만 is_on실행
            headerSpan[1].classList.add("is_on");
        } else if (this.location.href === "http://127.0.0.1:8000/activity") {
            // 잴 앞에거만 냄겨놓고 잴 앞에것만 is_on실행
            headerSpan[2].classList.add("is_on");
        }
    });
}

console.log(headerSpan[0]);