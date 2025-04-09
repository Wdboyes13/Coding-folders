const express = require("express");
const axios = require("axios");

const app = express();
const PORT = 3000; // Change this if needed

// Serve static files (optional, if you have an HTML frontend)
app.use(express.static("public"));

// Redirect /map to the second ngrok tunnel
app.get("/map", async (req, res) => {
  try {
    const response = await axios.get("http://localhost:4040/api/tunnels");
    const tunnels = response.data.tunnels;

    if (tunnels.length > 1) {
      const secondTunnel = tunnels[1].public_url; // Get second tunnel
      res.redirect(secondTunnel); // Redirect to the ngrok URL
    } else {
      res.status(404).send("Second tunnel not found.");
    }
  } catch (error) {
    console.error("Error fetching ngrok tunnels:", error);
    res.status(500).send("Internal server error.");
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start Express server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
