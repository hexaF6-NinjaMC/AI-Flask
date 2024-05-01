const showPassword = document.querySelector('#showPassword');
const passwordField = document.querySelector('#password');
const passwordConfirmField = document.querySelector('#password_confirmation');

showPassword.addEventListener('click', () => {
    if (showPassword.checked) {
        let type = "text";
        passwordField.setAttribute('type', type);
        if (passwordConfirmField != null) {
            passwordConfirmField.setAttribute('type', type);
        }
    } else {
        let type = "password";
        passwordField.setAttribute('type', type);
        if (passwordConfirmField != null) {
            passwordConfirmField.setAttribute('type', type);
        }
    }
});