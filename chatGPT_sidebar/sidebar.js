document.getElementById('chatbot-send').addEventListener('click', sendMessage);

function sendMessage() {
  const inputElement = document.getElementById('chatbot-input');
  const message = inputElement.value;
  inputElement.value = '';

  displayMessage('user', message);

  // Send the message to the internal API for processing
  processMessageWithAPI(message)
    .then(response => {
      displayMessage('bot', response);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function displayMessage(sender, message) {
  const messagesElement = document.getElementById('chatbot-messages');
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.textContent = message;
  messagesElement.appendChild(messageElement);
}

function processMessageWithAPI(message) {
  return new Promise((resolve, reject) => {
    const apiKey = getApiKey();
    const apiUrl = 'https://api.openai.com/v1/chat/completions';

    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: 'gpt-4-turbo',
        messages: [
          {
            role: 'system',
            content: 'You are a helpful assistant.'
          },
          {
            role: 'user',
            content: message
          }
        ]
      })
    };

    fetch(apiUrl, requestOptions)
      .then(response => response.json())
      .then(data => {
        if (data.choices && data.choices.length > 0) {
          const assistantReply = data.choices[0].message.content;
          resolve(assistantReply);
        } else {
          reject('No response received from the API.');
        }
      })
      .catch(error => {
        reject('Error communicating with the API: ' + error);
      });
  });
}