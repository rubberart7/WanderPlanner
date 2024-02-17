var currSlide = 0;
slide()

function slide() {
    var i;
    var img = document.querySelectorAll(".images img"); 
    var indicator = document.querySelectorAll(".indicators div");

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

