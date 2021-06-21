//var slideIndex = 0;
//showSlides();

//function showSlides() {
//  var i;
//var slides = document.getElementsByClassName("mySlides");
//for (i = 0; i < slides.length; i++) {
//    slides[i].style.display = "none";
//}
//slideIndex++;
//if (slideIndex > slides.length) { slideIndex = 1 }
//slides[slideIndex - 1].style.display = "block";
//setTimeout(showSlides, 2000); // Change image every 2 seconds
//}

function ChatViseble(){

    var chat = document.getElementsByClassName("showchat")
    console.log(chat)
    for(let i =0; i <chat.length; i++){
        chat[i].classList.toggle("showchatss")
    }

}

var index = 0
var step = 0
Slider()


function Sort(id) {
    var CategoryItems = document.getElementsByClassName("category-item")
    var CategoryTitles = document.getElementsByClassName("category-title")
    console.log(CategoryTitles)
    for (let i = 0; i < CategoryTitles.length; i++) {
        if (CategoryTitles[i].id == id) {
            CategoryTitles[i].classList.add("border")
        } else {
            CategoryTitles[i].classList.remove("border")
        }
    }
    for (let i = 0; i < CategoryItems.length; i++) {
        if (CategoryItems[i].id == id) {
            CategoryItems[i].classList.add("show")
            CategoryItems[i].classList.remove("hide")
        } else {
            CategoryItems[i].classList.add("hide")
            CategoryItems[i].classList.remove("show")
        }

    }
}



function slideIndex(item) {
    index += item
    step = item
    Slider()
}

function Slider() {
    var SliderItems = document.getElementsByClassName("slider-item")
    if (index < 0) {
        index = SliderItems.length - 1
    }
    if (index > SliderItems.length - 1) {
        index = 0
    }
    for (let i = 0; i < SliderItems.length; i++) {
        var newi = i
        if (i == index) {
            SliderItems[i].classList.add("show-slide")

        } else {
            SliderItems[i].classList.remove("show-slide")
        }

    }
}