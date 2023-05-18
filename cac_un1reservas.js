document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});

function validarFormulario(evento) {
    evento.preventDefault();
    var nombreReserva = document.getElementById("nombreReserva").value;
    if (nombreReserva.length == 0) {
        alert('No has escrito el nombre de la reserva');
        return;
    }


    var tel = document.getElementById('tel').value;
    if (tel.length < 10) {
        alert('El teléfono no es válido');
        return;
    }

    var mail = document.getElementById('mail').value;
    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(mail))) {
        alert('El email no es válido');
        return;
    }

    this.submit();
}