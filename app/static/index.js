document.querySelector(".header").style.backgroundImage = "url('static/college.jpeg')"; // Change The Top Background Here

var item1 =document.getElementById("item1");
var item2 =document.getElementById("item2");
var item3 = document.getElementById("item3");
var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var btn3 = document.getElementById("btn3");

function openone(){
    item1.style.transform="translateX(0)";
    item2.style.transform="translateX(100%)";
    item3.style.transform="translateX(100%)";
    btn1.style.color="red";
    btn2.style.color="black";
    btn3.style.color="black";
    item1.style.transitionDelay="0.3s";
    item2.style.transitionDelay="0s";
    item3.style.transitionDelay="0s";
}
function opentwo(){
    item1.style.transform="translateX(100%)";
    item2.style.transform="translateX(0)";
    item3.style.transform="translateX(100%)";
    btn1.style.color="black";
    btn2.style.color="red";
    btn3.style.color="black";
    item1.style.transitionDelay="0s";
    item2.style.transitionDelay="0.3s";
    item3.style.transitionDelay="0s";
}
function openthree(){
    item1.style.transform="translateX(100%)";
    item2.style.transform="translateX(100%)";
    item3.style.transform="translateX(0)";
    btn1.style.color="black";
    btn2.style.color="black";
    btn3.style.color="red";
    item1.style.transitionDelay="0s";
    item2.style.transitionDelay="0s";
    item3.style.transitionDelay="0.3s";
}