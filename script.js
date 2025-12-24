// Modal de contacto y comportamiento del formulario
function abrirModal() {
    const modal = document.getElementById('modal');
    modal.setAttribute('aria-hidden', 'false');
}

function cerrarModal() {
    const modal = document.getElementById('modal');
    modal.setAttribute('aria-hidden', 'true');
}

document.addEventListener('DOMContentLoaded', function() {
    // actualizar año en footer
    const y = new Date().getFullYear();
    const el = document.getElementById('year');
    if (el) el.textContent = y;

    // formulario
    const form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', function(evt) {
            evt.preventDefault();
            // Simular envío: mostrar mensaje y cerrar modal
            const nombre = document.getElementById('nombre').value || 'Amigo';
            alert('Gracias, ' + nombre + '. Hemos recibido tu mensaje.');
            cerrarModal();
            form.reset();
        });
    }
    // Ver proyectos - scroll y foco en input
    const verBtn = document.getElementById('ver-proyectos');
    if (verBtn) {
        verBtn.addEventListener('click', function() {
            const target = document.getElementById('proyectos');
            if (target) target.scrollIntoView({ behavior: 'smooth' });
            const fileIn = document.getElementById('fileInput');
            if (fileIn) fileIn.focus();
        });
    }

    // Cancel upload
    const cancelBtn = document.getElementById('cancelUpload');
    if (cancelBtn) cancelBtn.addEventListener('click', function() {
        const form = document.getElementById('uploadForm');
        if (form) form.reset();
        const status = document.getElementById('uploadStatus');
        if (status) status.textContent = '';
    });

    // Mostrar status si viene query param uploaded
    const params = new URLSearchParams(window.location.search);
    if (params.has('uploaded')) {
        const name = params.get('uploaded');
        const status = document.getElementById('uploadStatus');
        if (status) status.innerHTML = 'Archivo subido: <strong>' + decodeURIComponent(name) + '</strong>';
        // limpiar la URL para evitar mensajes repetidos
        if (history.replaceState) history.replaceState(null, '', window.location.pathname);
    }
});
