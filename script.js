async function uploadImage() {
const fileInput = document.getElementById('imageInput');
const formData = new FormData();
formData.append('file', fileInput.files[0]);
const response = await fetch('/predict', {
method: 'POST',
body: formData
});
const data = await response.json();
document.getElementById('result').innerHTML = `
 Disease: ${data.disease}<br>
 Confidence: ${data.confidence}%
 `;
}
async function sendMessage() {
const input = document.getElementById('chatInput');
const message = input.value;
const chatBox = document.getElementById('chatBox');
chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
const response = await fetch('/chat', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify({message})
});
const data = await response.json();
chatBox.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
input.value = '';
}
