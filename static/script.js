document.getElementById("send-btn").addEventListener("click", sendMessage);

async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message)  return;

    addMessage("You",message);
    input.value = "";

    try{
        const response = await fetch("/chat", {
            method : "POST",
            headers: { "Content-Type":"application/json" },
            body : JSON.stringify({message : message})
        });

            if (!response.ok) {
                addMessage("campusBot","server error:" + response.status);
                return;
            }

            const data = await response.json();
            addMessage("campusBot",data.reply);

            } catch(error) {
                console.error("Error sending mesage:", error);
            addMessage("campusBot", "Network error - check your connection.");

    }

}

function addMessage(sender,text) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.innerHTML = `${sender}: ${text}`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
