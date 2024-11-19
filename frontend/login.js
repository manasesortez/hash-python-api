document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault(); // Evita la recarga de la página
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
  
    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });
  
      const data = await response.json();
  
      if (response.ok) {
        document.getElementById("message").textContent = `Token: ${data.token}`;
        console.log("Token recibido:", data.token);
      } else {
        document.getElementById("message").textContent = `Error: ${data.message}`;
      }
    } catch (error) {
      document.getElementById("message").textContent = "Error de conexión al servidor";
      console.error("Error:", error);
    }
  });
  