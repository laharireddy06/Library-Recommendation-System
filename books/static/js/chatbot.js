document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    addMessage("You", message);
    input.value = "";

    fetch("/api/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        const botReply = data.response || "Bot error: No reply";
        addMessage("Bot", botReply, true);  // render HTML
    })
    .catch(() => {
        addMessage("Bot", "Error: Could not reach server.");
    });
}

function addMessage(sender, text, isHTML = false) {
    const box = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = sender === "You" ? "user-msg" : "bot-msg";

    if (isHTML) {
        msg.innerHTML = `<strong>${sender}:</strong><br>${text}`;
    } else {
        msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    }

    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}

function getCSRFToken() {
    return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1];
}
