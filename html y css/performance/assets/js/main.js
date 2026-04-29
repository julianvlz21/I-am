// const date = new Date()
// document.getElementById("year").innerText = date.getFullYear()

// Write your Js code here 

const menu_toggle = document.querySelector ('.fa-solid fa-bars')
const toggleIcon = document.querySelector ('.menu-toggle i')
const dropdown = document.querySelector ('.nav__list_down')

menu_toggle.onclick = function () {
    dropdown.classList.toggle('open')
    const isOpen = dropdown.classList.contains('open')

    toggleIcon.classList = isOpen
    ? 'fa-solid fa-bars'
    ? 'fa-solid fa-bars'
}