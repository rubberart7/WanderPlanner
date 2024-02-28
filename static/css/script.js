let currSlide = 0;
slide()

function slide() {
    let i;
    let img = document.querySelectorAll(".images img"); 
    let indicator = document.querySelectorAll(".indicators div");

    for (i = 0; i < img.length; i++) {
        img[i].classList.add("hide");
        indicator[i].classList.remove("indicated");
    }
    currSlide++;
    if (currSlide == img.length) {
        currSlide = 0;

    }
    img[currSlide].classList.remove("hide");
    indicator[currSlide].classList.add("indicated");
    setTimeout(slide, 5000);  
}

