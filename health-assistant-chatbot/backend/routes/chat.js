const express = require('express');
const router = express.Router();
const chatController = require('../controllers/chatController');

// POST /api/chat - Send message and get response
router.post('/', chatController.handleChat);

module.exports = router;
