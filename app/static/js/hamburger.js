function toggleMenu() {
    document.getElementsByClassName('navigation')[0].classList.toggle('responsive')
    
    if (document.getElementsByClassName('responsive')[0]) {
        document.querySelector('nav > button').innerHTML = `&#x2261; Menu`;
    } else {
        document.querySelector('nav > button').innerHTML = `&times; Close`;
    }
}