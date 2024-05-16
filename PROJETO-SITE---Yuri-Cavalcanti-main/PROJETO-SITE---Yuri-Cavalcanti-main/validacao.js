document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    var nome = document.getElementById('nome');
    var email = document.getElementById('email');
    var mensagem = document.getElementById('mensagem');

    form.addEventListener('input', function() {
        if (nome.value === '') {
            nome.style.borderColor = 'red';
        } else {
            nome.style.borderColor = 'green';
        }

        if (email.value === '' || !email.value.includes('@')) {
            email.style.borderColor = 'red';
        } else {
            email.style.borderColor = 'green';
        }

        if (mensagem.value === '') {
            mensagem.style.borderColor = 'red';
        } else {
            mensagem.style.borderColor = 'green';
        }
    });

    form.addEventListener('submit', function(event) {
        if (nome.value === '' || email.value === '' || !email.value.includes('@') || mensagem.value === '') {
            event.preventDefault();
            alert('Por favor, preencha todos os campos corretamente antes de enviar.');
        } else {
            alert('Mensagem enviada com sucesso!');
        }
    });
});
