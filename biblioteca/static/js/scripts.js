const botaoMenuMobile = document.querySelector('.menu-mobile');
const navbar = document.querySelector(nav);

botaoMenuMobile.onclick = function () {
    botaoMenuMobile.classList.toggle('');
    navbar.classList.toggle('');
};