function toggleChatbot() {
    var chatbot = document.getElementById('chatbot');
    if (chatbot.classList.contains('hidden')) {
        chatbot.classList.remove('hidden');
    } else {
        chatbot.classList.add('hidden');
    }
}

function sendMessage(event) {
    if (event.key === "Enter") {
        var input = document.getElementById('userInput');
        var message = input.value;
        if (message.trim() !== '') {
            var messagesContainer = document.querySelector('.chatbot-messages');
            var newMessage = document.createElement('div');
            newMessage.textContent = message;
            messagesContainer.appendChild(newMessage);
            input.value = ''; // Clear input field
        }
    }
}
