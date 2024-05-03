function getApiKey() {
    // Option 1: Retrieve the API key from the environment variable
    const apiKey = process.env.OPENAI_API_KEY;
  
    // Option 2: Retrieve the API key from a secure storage (e.g., Chrome storage)
    // chrome.storage.sync.get('openaiApiKey', function(data) {
    //   const apiKey = data.openaiApiKey;
    //   // Use the retrieved API key
    // });
  
    // Option 3: Retrieve the API key from a remote server or a secure API endpoint
    // fetch('https://your-secure-server.com/api/getApiKey')
    //   .then(response => response.text())
    //   .then(apiKey => {
    //     // Use the retrieved API key
    //   });
  
    return apiKey;
  }