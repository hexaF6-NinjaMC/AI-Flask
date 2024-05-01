const htmlCode = document.querySelector('.html-code textarea');
const cssCode = document.querySelector('.css-code textarea');
const jsCode = document.querySelector('.js-code textarea');
const result = document.querySelector('#result');

document.addEventListener('keydown', (event) => { if (event.key === 'Tab') { console.log('Tabbed!') } })

function run() {
    localStorage.setItem('html_code', htmlCode.value);
    localStorage.setItem('css_code', cssCode.value);
    localStorage.setItem('js_code', jsCode.value);
    result.contentDocument.body.replaceChildren()
    result.contentDocument.body.insertAdjacentHTML('beforeend', `<style>${localStorage.css_code}</style>` + localStorage.html_code);
    result.contentWindow.eval(localStorage.js_code);
}

htmlCode.addEventListener('keydown', (event) => {
    if (event.key === 'Tab') {
        event.preventDefault();
        const {value, selectionStart, selectionEnd} = htmlCode;
        htmlCode.value = `${value.substring(0, selectionEnd)}\t${value.substring(selectionEnd)}`;
        htmlCode.selectionStart = htmlCode.selectionEnd = selectionEnd + 1;
    }
})

cssCode.addEventListener('keydown', (event) => {
    if (event.key === 'Tab') {
        event.preventDefault();
        const {value, selectionStart, selectionEnd} = cssCode;
        cssCode.value = `${value.substring(0, selectionEnd)}\t${value.substring(selectionEnd)}`;
        cssCode.selectionStart = cssCode.selectionEnd = selectionEnd + 1;
    }
})

jsCode.addEventListener('keydown', (event) => {
    if (event.key === 'Tab') {
        event.preventDefault();
        const {value, selectionStart, selectionEnd} = jsCode;
        jsCode.value = `${value.substring(0, selectionEnd)}\t${value.substring(selectionEnd)}`;
        jsCode.selectionStart = jsCode.selectionEnd = selectionEnd + 1;
    }
})

htmlCode.onkeyup = () => run();
cssCode.onkeyup = () => run();
jsCode.onkeyup = () => run();



if (localStorage.html_code == undefined) {
    htmlCode.value = '';
} else {
    htmlCode.value = localStorage.html_code;
}

if (localStorage.css_code == undefined) {
    cssCode.value = '';
} else {
    cssCode.value = localStorage.css_code;
}

if (localStorage.js_code == undefined) {
    jsCode.value = '';
} else {
    jsCode.value = localStorage.js_code;
}

window.onload = () => {
    result.contentDocument.body.insertAdjacentHTML('beforeend', `<style>${cssCode.value}</style>` + htmlCode.value);
    result.contentWindow.eval(jsCode.value);
};
