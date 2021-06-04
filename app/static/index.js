document.querySelector(".header").style.backgroundImage = "url('static/college.jpeg')"; // Change The Top Background Here

const tabs = [...document.querySelectorAll('.tab')];
const pageContainer = document.querySelector('.content');
const activeSpan = document.querySelector('.tabs .active');

tabs.forEach((item, i) => {
    item.addEventListener('click', () => {
        pageContainer.style.marginLeft = `-${i * 100}%`;
        activeSpan.style.left = `${i * 20}%`;
    })
})