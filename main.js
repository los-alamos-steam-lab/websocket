import { Settings } from './settings.js';

function showMessage(message) {
    window.setTimeout(() => window.alert(message), 50);
}

// Called when the webpage opens or reloads
function initGame(websocket) {
    websocket.addEventListener("open", () => {
      // Send an "init" event according to who is connecting.
      const params = new URLSearchParams(window.location.search);
      let event = { type: "init" };
      event.client = "webclient";
      event.name = "STEAMLab";
      websocket.send(JSON.stringify(event));
    });
}
  
function handleJSONmessage(jsonobj) {
    showMessage("JSON" + JSON.stringify(jsonobj));
    // switch (jsonobj.type) {
    //     case "init":
    //       // Create links for inviting the second player and spectators.
    //       document.querySelector(".join").href = "?join=" + event.join;
    //       document.querySelector(".watch").href = "?watch=" + event.watch;
    //       break;
    //     case "play":
    //       // Update the UI with the move.
    //       playMove(board, event.player, event.column, event.row);
    //       break;
    //     case "win":
    //       showMessage(`Player ${event.player} wins!`);
    //       // No further messages are expected; close the WebSocket connection.
    //       websocket.close(1000);
    //       break;
    //     case "error":
    //       showMessage(event.message);
    //       break;
    //     default:
    //       throw new Error(`Unsupported event type: ${jsonobj.type}.`);
    //   }
  }

function handleTextMessage(text) {
    showMessage("not JSON" + text);
}

function receiveMessage(websocket) {
    websocket.addEventListener("message", ({ data }) => {
        try {
            const jsonobj = JSON.parse(data);
            handleJSONmessage(jsonobj)
        } catch(error) {
            handleTextMessage(data)
        }
    });
}

function sendMessage(sendmesssage, websocket) {
    sendmesssage.addEventListener("click", ({ target }) => {
        const event = {
            type: "command",
            command: "getconnected",
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
    initGame(websocket);
    receiveMessage(websocket);
    sendMessage(sendmessage, websocket);
});