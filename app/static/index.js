document.querySelector(".header").style.backgroundImage = "url('static/college.jpeg')"; // Change The Top Background Here

var cardContainer = document.getElementsByClassName("cardContainer");
var width = window.innerWidth;
var height = window.innerHeight;
// var width = document.getElementById("master").style.width;
// var height = document.getElementById("master").style.height;

if (width>600){
    // Desktop Version
    for(i=0;i<cardContainer.length;i++){
        cardContainer[i].style.width = String(width/4)+"px";
        cardContainer[i].style.height = String(height/1.5)+"px";
    }
} else{
    // Mobile Version
    for(i=0;i<cardContainer.length;i++){
        cardContainer[i].style.width = String(width)+"px";
        cardContainer[i].style.height = String(height/2)+"px";
    }
}

// Blurred Background for card
var cardImage = document.getElementsByClassName("eventPoster");
var cardImageBG = document.getElementsByClassName("card-image-bg");
for (i = 0; i < cardImage.length; i ++) {
    cardImage[i].style.maxHeight = String(cardImageBG[0].offsetHeight) + "px";
    cardImage[i].style.maxWidth = String(cardImageBG[0].offsetWidth) + "px";
    cardImageBG[i].style.background = 'url("' + cardImage[i].src + '")';
}
