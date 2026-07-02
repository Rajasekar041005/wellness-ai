require('dotenv').config();

const express = require('express');
const cors = require('cors');
const path = require('path');
const chatRoutes = require('./routes/chat');

const app = express();
const DEFAULT_PORT = Number(process.env.PORT) || 3000;

const handleListenError = (error, port, retriesLeft) => {
  if (error.code === 'EADDRINUSE' && retriesLeft > 0) {
    const nextPort = port + 1;
    console.warn(`Port ${port} is busy, trying ${nextPort} instead.`);
    startServer(nextPort, retriesLeft - 1);
    return;
  }

  console.error('Server failed to start:', error);
  process.exit(1);
};

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from frontend
app.use(express.static(path.join(__dirname, '../frontend')));

// API Routes
app.use('/api/chat', chatRoutes);

// Root route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend', 'chat.html'));
});

const startServer = (port, retriesLeft = 10) => {
  let server;

  try {
    server = app.listen(port, () => {
      const activePort = server.address().port;
      console.log(`🏥 Health Assistant Chatbot server running on http://localhost:${activePort}`);
      console.log(`📡 API endpoint: http://localhost:${activePort}/api/chat`);
    });
  } catch (error) {
    handleListenError(error, port, retriesLeft);
    return;
  }

  server.once('error', (error) => handleListenError(error, port, retriesLeft));
};

// Start server
startServer(DEFAULT_PORT);
