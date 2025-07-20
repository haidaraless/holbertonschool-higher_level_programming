document.querySelector('#toggle_header').addEventListener('click', function () {
    if (document.querySelector('header').className == 'red') {
        document.querySelector('header').className = 'green';
        return;
    }
    document.querySelector('header').className = 'red';
});