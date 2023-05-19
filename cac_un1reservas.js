function validarFormulario() {
    let fecha = document.getElementById("fecha").value.trim();
    let personas = document.getElementById("personas").value.trim();
    let nombreReserva = document.getElementById("nombreReserva").value.trim();
    let mail = document.getElementById("mail").value.trim();
    let telefono = document.getElementById("tel").value.trim();

    if (fecha === "" || personas === "" || nombreReserva === "" || mail === "" || telefono === "") {
        alert("Por favor, complete todos los campos para la reserva.");
        return false;
    }

    for (let i = 0; i < nombreReserva.length; i++) {
        let charCode = nombreReserva.charCodeAt(i);
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || (charCode === 32))) {
            alert("El campo 'Nombre de reserva' sólo puede contener carácteres alfabéticos y espacios.");
            return false;
        }
    }

    alert("Formulario enviado correctamente.");
    return true;


}

// document.addEventListener("DOMContentLoaded", function() {
//     document.getElementById("formulario").addEventListener('submit', validarFormulario);
// });

// function validarFormulario(evento) {
//     evento.preventDefault();
//     var nombreReserva = document.getElementById("nombreReserva").value;
//     if (nombreReserva.length == 0) {
//         alert('No has escrito el nombre de la reserva');
//         return;
//     }


//     var tel = document.getElementById('tel').value;
//     if (tel.length < 10) {
//         alert('El teléfono no es válido');
//         return;
//     }

//     var mail = document.getElementById('mail').value;
//     if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(mail))) {
//         alert('El email no es válido');
//         return;
//     }

//     this.submit();
// }