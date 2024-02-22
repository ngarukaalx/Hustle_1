// wait for the DOM to load
$(document).ready(function () {
    // attach an event listener
    const signupForm = document.getElementById('signup-form');
    const logTab = document.getElementById('log-info');
    logTab.style.display = 'none';
    signupForm.style.display = 'none';

    const singup = $('#signup-tab');
    singup.click(function () {
        const loginForm = document.getElementById('login-form');
        const signTab = document.getElementById('sign-tab');
        const logTab = document.getElementById('log-info');
        logTab.style.display = 'block';
        loginForm.style.display = 'none';
        signTab.style.display = 'none';
        signupForm.style.display = 'block';
    });
    const login = $('#login-tab');
    login.click(function () {
        const signTab = document.getElementById('sign-tab');
        const loginForm = document.getElementById('login-form');
        const signupForm = document.getElementById('signup-form');
        signupForm.style.display = 'none';
        loginForm.style.display = 'block';
        signTab.style.display = 'block';
        const logTab = document.getElementById('log-info');
        logTab.style.display = 'none';
    })
});