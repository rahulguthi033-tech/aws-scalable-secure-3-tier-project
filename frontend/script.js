// Replace this with your backend server address when deployed.
const API_URL = "http://localhost:8080";

async function checkBackend() {
    const result = document.getElementById("result");

    try {
        const response = await fetch(`${API_URL}/api/health`);
        const data = await response.json();

        result.textContent =
            "Backend Status: " + data.status;

    } catch (error) {
        result.textContent = "Backend connection failed!";
    }
}
