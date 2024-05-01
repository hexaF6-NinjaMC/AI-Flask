function closeDiv(el) {
    el.parentElement.style.display = 'none';
}

try {
    flashMsgCloseBtnDivs = document.querySelectorAll('.alert');
    flashMsgCloseBtnDivs.forEach(div => {
        const child = div.querySelector('.btn-close');
        
        if (child.tagName.toLowerCase() === 'button') {
            child.addEventListener('click', () => {closeDiv(child)});
        }
    });
} catch (error) {
    console.error(error)
}