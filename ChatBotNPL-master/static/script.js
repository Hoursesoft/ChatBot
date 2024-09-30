function sendMessage() {
    var userMessage = document.getElementById('user-input').value;

    // Enviar el mensaje del usuario al servidor usando Ajax
    $.ajax({
        url: '/api/bot',
        method: 'POST',
        data: { user_message: userMessage },
        success: function (response) {
            // Actualizar el contenedor de chat con la respuesta del BOT
            var chatContainer = document.getElementById('chat-container');
            chatContainer.innerHTML += '<div class="card mb-2 mt-2"> <div class="card-body message user-message"><p class="text-start fw-bold"> Users: </p> <p class="text-start">' + userMessage + '</p></div> </div>';
            
            // Mostrar la respuesta del BOT línea por línea usando función recursiva
            displayBotResponse(chatContainer, response.bot_response.split('\n'), 0);
        }
    });
}

function displayBotResponse(container, responses, index) {
    if (index < responses.length) {
        var botResponseElement = document.createElement('div');
        botResponseElement.classList.add('card');
        botResponseElement.innerHTML = `
            <div class="card-body message bot-message mb-2"">
                <p class="text-start fw-bold"></p>
            </div>`;
        container.appendChild(botResponseElement);

        // Iniciar Typed.js para mostrar la respuesta letra por letra sin el cursor
        var typed = new Typed(botResponseElement.querySelector('.message p'), {
            strings: [responses[index]],
            typeSpeed: 50,
            showCursor: false,
            onComplete: function () {
                // Llamada recursiva para la siguiente línea
                displayBotResponse(container, responses, index + 1);
            }
        });
    } else {
        // Limpiar la entrada del usuario después de mostrar todas las respuestas
        document.getElementById('user-input').value = '';
    }
}
