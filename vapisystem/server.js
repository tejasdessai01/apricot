// Import the Vapi class from the package
import Vapi from '@vapi-ai/web';
require('dotenv').config({ path: '../../.env' });

const publicKey = process.env.PUBLIC_KEY;
const assistantId = process.env.ASSISTANT_ID;

// Create a new instance of the Vapi class, passing your Public Key as a parameter to the constructor
const vapi = new Vapi(publicKey);

// Function to start the assistant when the start button is clicked
function startAssistant(assistantId) {
  // Start the assistant using the provided assistant ID
  vapi.start(assistantId);

  // Listen for speech start event
  vapi.on('speech-start', () => {
    console.log('Speech has started');
    // Perform actions if needed when speech starts
  });

  // Listen for speech end event
  vapi.on('speech-end', () => {
    console.log('Speech has ended');
    // Perform actions if needed when speech ends
  });

  // Listen for message event to receive assistant responses
  vapi.on('message', (message) => {
    console.log('Assistant message:', message);
    // Handle assistant messages as needed
  });

  // Listen for call end event
  vapi.on('call-end', () => {
    console.log('Call has stopped');
    // Perform actions if needed when call ends
  });
}

// Function to stop the assistant when the stop button is clicked
function stopAssistant() {
  // Stop the assistant
  vapi.stop();
}

// Function to send voice message to the assistant
function sendVoiceMessage(message) {
  // Send voice message to the assistant
  vapi.send({
    type: "add-message",
    message: {
      role: "user",
      content: message,
    },
  });
}

// Example usage:
// Call startAssistant function with the assistant ID when the start button is clicked
//startAssistant('your-assistant-id');

// Call stopAssistant function when the stop button is clicked
//stopAssistant();

// Call sendVoiceMessage function with the voice message when sending a voice message to the assistant
//sendVoiceMessage('Hello, this is a voice message for the assistant.');
