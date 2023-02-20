import { Settings } from './settings.js';

function showMessage(message) {
    window.setTimeout(() => window.alert(message), 50);
}

function receiveMessage(websocket) {
    websocket.addEventListener("message", ({ data }) => {
        showMessage(data);
    });
}

function sendMessage(sendmesssage, websocket) {
    sendmesssage.addEventListener("click", ({ target }) => {
        const event = {
            type: "message",
            column: "hello",
        };
        websocket.send(JSON.stringify(event));
    });
}

window.addEventListener("DOMContentLoaded", () => {
    // Initialize the UI.
    const sendmessage = document.querySelector(".sendmessage");
    // Open the WebSocket connection and register event handlers.
    const websocket = new WebSocket(Settings.socketserverstring);
    // initGame(websocket);
    receiveMessage(websocket);
    sendMessage(sendmessage, websocket);
});