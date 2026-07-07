// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
  // Auto-focus on input
  userInput?.focus();
});

// Clear Chat functionality
document.getElementById('clearChatBtn')?.addEventListener('click', () => {
  if (confirm('Are you sure you want to clear the current chat?')) {
    chatMessages.innerHTML = `
      <div class="message bot-message">
        <div class="message-content">
          <p>👋 Hello! I'm your Health Assistant. I can help you with general health information about diseases, symptoms, prevention, food recommendations, and healthy lifestyle tips.</p>
          <p><strong>Remember:</strong> I provide educational information only and cannot diagnose or prescribe treatments. Always consult a doctor for medical advice.</p>
        </div>
      </div>
    `;
  }
});

// Chat functionality
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');
const sendBtn = document.getElementById('sendBtn');
const trackerForm = document.getElementById('dailyTrackerForm');
const trackerDateInput = document.getElementById('trackerDate');
const sleepHoursInput = document.getElementById('sleepHours');
const waterCupsInput = document.getElementById('waterCups');
const activityMinutesInput = document.getElementById('activityMinutes');
const moodLevelInput = document.getElementById('moodLevel');
const trackerNotesInput = document.getElementById('trackerNotes');
const trackerHistoryList = document.getElementById('trackerHistoryList');
const trackerStatus = document.getElementById('trackerStatus');
const loadTodayBtn = document.getElementById('loadTodayBtn');

const LAST_ACTIVE_AT_KEY = 'healthAssistant:lastActiveAt';
const LAST_REMINDER_AT_KEY = 'healthAssistant:lastReminderAt';
const DAILY_TRACKER_STORAGE_KEY = 'healthAssistant:dailyTrackerEntries';
const INACTIVITY_LIMIT_MS = 3 * 24 * 60 * 60 * 1000; // 3 days

const ENGAGEMENT_QUESTIONS = [
  'Would you like a quick 1-minute healthy habit challenge for today?',
  'Do you want one simple tip to improve your sleep tonight?',
  'Should I share one easy food suggestion for better daily energy?'
];

// Use dynamic URL fallback to Flask backend on port 5000 if hosted on a different port (e.g. 3000) or opened via file://
const API_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') && window.location.port === '5000'
  ? '/api/chat'
  : 'http://127.0.0.1:5000/api/chat';

initializeDailyTracker();
initializeInactivityReminder();

chatForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const message = userInput.value.trim();
  if (!message) return;

  recordUserActivity();

  // Add user message to chat
  addMessage(message, 'user');
  userInput.value = '';

  try {
    const responseText = await sendMessageToAssistant(message);

    if (responseText) {
      addMessage(responseText, 'bot');
    }
  } catch (error) {
    console.error('Error:', error);
    const msg = error.message && error.message !== 'Failed to fetch'
      ? `⚠️ Error: ${error.message}`
      : 'Sorry, I could not connect to the server. Please make sure the backend is running.';
    addMessage(msg, 'bot');
  }

  // Scroll to bottom
  scrollToBottom();
});

function formatTextContent(text) {
  // Replace markdown-style bold (**text**) with actual bold tags
  let formattedText = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  
  // Split into lines
  const lines = formattedText.split('\n');
  const elements = [];
  let currentBulletList = [];

  lines.forEach((line) => {
    const trimmed = line.trim();
    
    // Skip empty lines
    if (!trimmed) {
      // Flush any pending bullet list
      if (currentBulletList.length > 0) {
        const ul = document.createElement('ul');
        ul.className = 'response-list';
        currentBulletList.forEach(bulletHtml => {
          const li = document.createElement('li');
          li.innerHTML = bulletHtml;
          ul.appendChild(li);
        });
        elements.push(ul);
        currentBulletList = [];
      }
      return;
    }

    // Check if it's a bullet point (starts with * or -)
    if (trimmed.startsWith('* ') || trimmed.startsWith('- ') || trimmed.startsWith('• ')) {
      let bulletText = trimmed.replace(/^[\*\-•]\s*/, '');
      currentBulletList.push(bulletText);
      return;
    }

    // Flush pending bullets before adding new element
    if (currentBulletList.length > 0) {
      const ul = document.createElement('ul');
      ul.className = 'response-list';
      currentBulletList.forEach(bulletHtml => {
        const li = document.createElement('li');
        li.innerHTML = bulletHtml;
        ul.appendChild(li);
      });
      elements.push(ul);
      currentBulletList = [];
    }

    // Check if it looks like a section header (starts with ** or ends with colon or is all caps)
    const isHeader = trimmed.startsWith('**') || /^[A-Z][A-Za-z\s]+:$/.test(trimmed) || (trimmed === trimmed.toUpperCase() && trimmed.length > 1);
    
    if (isHeader) {
      const h4 = document.createElement('h4');
      h4.className = 'response-heading';
      // Remove ** markers if present
      h4.innerHTML = trimmed.replace(/\*\*/g, '');
      elements.push(h4);
    } else {
      const p = document.createElement('p');
      p.innerHTML = trimmed;
      elements.push(p);
    }
  });

  // Flush any remaining bullets
  if (currentBulletList.length > 0) {
    const ul = document.createElement('ul');
    ul.className = 'response-list';
    currentBulletList.forEach(bulletHtml => {
      const li = document.createElement('li');
      li.innerHTML = bulletHtml;
      ul.appendChild(li);
    });
    elements.push(ul);
  }

  return elements;
}

function addMessage(text, type) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${type}-message`;
  
  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  
  // Format the text content based on message type
  if (type === 'bot') {
    const formattedElements = formatTextContent(text);
    formattedElements.forEach(element => {
      contentDiv.appendChild(element);
    });
  } else {
    // For user messages, keep simple paragraph format
    const paragraphs = text.split('\n').filter(p => p.trim());
    paragraphs.forEach(paragraph => {
      const p = document.createElement('p');
      p.textContent = paragraph;
      contentDiv.appendChild(p);
    });
  }
  
  messageDiv.appendChild(contentDiv);
  chatMessages.appendChild(messageDiv);
  
  return messageDiv;
}

function addTypingIndicator() {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'message bot-message';
  
  const typingDiv = document.createElement('div');
  typingDiv.className = 'typing-indicator';
  
  for (let i = 0; i < 3; i++) {
    const dot = document.createElement('div');
    dot.className = 'typing-dot';
    typingDiv.appendChild(dot);
  }
  
  messageDiv.appendChild(typingDiv);
  chatMessages.appendChild(messageDiv);
  scrollToBottom();
  
  return messageDiv;
}

function scrollToBottom() {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function initializeDailyTracker() {
  if (!trackerDateInput) {
    return;
  }

  trackerDateInput.value = getLocalDateValue();
  loadTrackerEntry(trackerDateInput.value);
  renderTrackerHistory();
  updateTrackerStatus();

  trackerDateInput.addEventListener('change', () => {
    loadTrackerEntry(trackerDateInput.value);
    updateTrackerStatus();
  });

  trackerForm?.addEventListener('submit', handleTrackerSubmit);

  loadTodayBtn?.addEventListener('click', () => {
    trackerDateInput.value = getLocalDateValue();
    loadTrackerEntry(trackerDateInput.value);
    updateTrackerStatus();
  });
}

async function handleTrackerSubmit(event) {
  event.preventDefault();

  if (!trackerDateInput?.value) {
    return;
  }

  const entry = {
    date: trackerDateInput.value,
    sleepHours: parseOptionalNumber(sleepHoursInput?.value),
    waterCups: parseOptionalNumber(waterCupsInput?.value),
    activityMinutes: parseOptionalNumber(activityMinutesInput?.value),
    mood: moodLevelInput?.value || '',
    notes: trackerNotesInput?.value.trim() || '',
    updatedAt: new Date().toISOString()
  };

  saveTrackerEntry(entry);
  renderTrackerHistory();
  updateTrackerStatus(entry);

  addMessage(`Daily update saved for ${formatDateLabel(entry.date)}. I’m generating a routine suggestion based on your check-in.`, 'bot');

  try {
    const routinePrompt = buildRoutinePrompt(entry);
    const responseText = await sendMessageToAssistant(routinePrompt, entry);

    if (responseText) {
      addMessage(responseText, 'bot');
    }
  } catch (error) {
    console.error('Tracker suggestion error:', error);
    addMessage('I saved your check-in, but I could not generate a routine suggestion right now.', 'bot');
  }
}

async function sendMessageToAssistant(message, trackingData = null) {
  const typingIndicator = addTypingIndicator();

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message, trackingData })
    });

    const data = await response.json();

    if (!response.ok || !data.success) {
      throw new Error(data.error || 'Request failed');
    }

    return data.response;
  } finally {
    typingIndicator.remove();
    scrollToBottom();
  }
}

function buildRoutinePrompt(entry) {
  return [
    'I completed my daily health check-in.',
    `Date: ${entry.date}`,
    `Sleep hours: ${formatOptionalValue(entry.sleepHours, 'not recorded')}`,
    `Water cups: ${formatOptionalValue(entry.waterCups, 'not recorded')}`,
    `Activity minutes: ${formatOptionalValue(entry.activityMinutes, 'not recorded')}`,
    `Mood: ${entry.mood || 'not recorded'}`,
    `Notes: ${entry.notes || 'none'}`,
    '',
    'Please suggest a simple routine for today using this check-in. Include a daily summary, morning routine, afternoon routine, evening routine, food and hydration tips, and one small goal for tomorrow.'
  ].join('\n');
}

function saveTrackerEntry(entry) {
  const entries = getTrackerEntries().filter((storedEntry) => storedEntry.date !== entry.date);
  entries.unshift(entry);
  localStorage.setItem(DAILY_TRACKER_STORAGE_KEY, JSON.stringify(entries));
  loadTrackerEntry(entry.date);
}

function loadTrackerEntry(dateValue) {
  const entry = getTrackerEntries().find((storedEntry) => storedEntry.date === dateValue);

  if (!entry) {
    clearTrackerForm();
    return;
  }

  sleepHoursInput.value = formatNumericValue(entry.sleepHours);
  waterCupsInput.value = formatNumericValue(entry.waterCups);
  activityMinutesInput.value = formatNumericValue(entry.activityMinutes);
  moodLevelInput.value = entry.mood || '';
  trackerNotesInput.value = entry.notes || '';
}

function clearTrackerForm() {
  if (sleepHoursInput) sleepHoursInput.value = '';
  if (waterCupsInput) waterCupsInput.value = '';
  if (activityMinutesInput) activityMinutesInput.value = '';
  if (moodLevelInput) moodLevelInput.value = '';
  if (trackerNotesInput) trackerNotesInput.value = '';
}

function renderTrackerHistory() {
  if (!trackerHistoryList) {
    return;
  }

  const recentEntries = getTrackerEntries()
    .slice()
    .sort((a, b) => b.date.localeCompare(a.date))
    .slice(0, 7);

  if (recentEntries.length === 0) {
    trackerHistoryList.innerHTML = '<div class="tracker-history-empty">No daily updates saved yet.</div>';
    return;
  }

  trackerHistoryList.innerHTML = recentEntries.map((entry) => `
    <article class="tracker-card">
      <div class="tracker-card-header">
        <strong>${formatDateLabel(entry.date)}</strong>
        <span class="tracker-card-meta">${formatEntryQuickStats(entry)}</span>
      </div>
      <div class="tracker-card-notes">${entry.notes ? escapeHtml(entry.notes) : 'No notes added.'}</div>
    </article>
  `).join('');
}

function updateTrackerStatus(entryOverride = null) {
  if (!trackerStatus) {
    return;
  }

  const todayEntry = entryOverride || getTrackerEntries().find((entry) => entry.date === getLocalDateValue());

  if (!todayEntry) {
    trackerStatus.textContent = 'No entry saved for today';
    return;
  }

  trackerStatus.textContent = `Today: ${formatEntryQuickStats(todayEntry)}`;
}

function getTrackerEntries() {
  const rawEntries = localStorage.getItem(DAILY_TRACKER_STORAGE_KEY);

  if (!rawEntries) {
    return [];
  }

  try {
    const parsedEntries = JSON.parse(rawEntries);
    return Array.isArray(parsedEntries) ? parsedEntries : [];
  } catch (error) {
    console.error('Failed to parse tracker entries:', error);
    return [];
  }
}

function formatEntryQuickStats(entry) {
  const stats = [];

  if (isValidNumber(entry.sleepHours)) {
    stats.push(`${entry.sleepHours}h sleep`);
  }

  if (isValidNumber(entry.waterCups)) {
    stats.push(`${entry.waterCups} cups water`);
  }

  if (isValidNumber(entry.activityMinutes)) {
    stats.push(`${entry.activityMinutes} min activity`);
  }

  if (entry.mood) {
    stats.push(entry.mood);
  }

  return stats.length > 0 ? stats.join(' · ') : 'Check-in saved';
}

function getLocalDateValue(date = new Date()) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');

  return `${year}-${month}-${day}`;
}

function formatDateLabel(dateValue) {
  const parsedDate = new Date(`${dateValue}T00:00:00`);

  if (Number.isNaN(parsedDate.getTime())) {
    return dateValue;
  }

  return new Intl.DateTimeFormat('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  }).format(parsedDate);
}

function parseOptionalNumber(value) {
  if (value === '' || value === null || value === undefined) {
    return null;
  }

  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

function formatNumericValue(value) {
  return isValidNumber(value) ? String(value) : '';
}

function formatOptionalValue(value, fallback) {
  return isValidNumber(value) ? String(value) : fallback;
}

function isValidNumber(value) {
  return typeof value === 'number' && Number.isFinite(value);
}

function escapeHtml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function initializeInactivityReminder() {
  if (!getStoredTimestamp(LAST_ACTIVE_AT_KEY)) {
    recordUserActivity();
  }

  checkAndSendInactivityReminder();

  // Re-check periodically while page is open.
  setInterval(checkAndSendInactivityReminder, 60 * 60 * 1000);
}

function checkAndSendInactivityReminder() {
  const now = Date.now();
  const lastActiveAt = getStoredTimestamp(LAST_ACTIVE_AT_KEY);
  const lastReminderAt = getStoredTimestamp(LAST_REMINDER_AT_KEY);

  if (!lastActiveAt) {
    return;
  }

  const isInactiveLongEnough = now - lastActiveAt >= INACTIVITY_LIMIT_MS;
  const reminderAlreadySentForCurrentInactivePeriod =
    typeof lastReminderAt === 'number' && lastReminderAt >= lastActiveAt;

  if (!isInactiveLongEnough || reminderAlreadySentForCurrentInactivePeriod) {
    return;
  }

  const reminderMessage = buildInactivityReminderMessage();
  addMessage(reminderMessage, 'bot');
  scrollToBottom();

  localStorage.setItem(LAST_REMINDER_AT_KEY, String(now));
  showBrowserReminderNotification(reminderMessage);
}

function buildInactivityReminderMessage() {
  const randomQuestion = ENGAGEMENT_QUESTIONS[Math.floor(Math.random() * ENGAGEMENT_QUESTIONS.length)];
  return `Are you inactive? Why are you not using the chatbot?\n${randomQuestion}`;
}

function showBrowserReminderNotification(message) {
  if (typeof Notification === 'undefined') {
    return;
  }

  if (Notification.permission === 'granted') {
    new Notification('Health Assistant Reminder', { body: message });
    return;
  }

  if (Notification.permission === 'default') {
    Notification.requestPermission().then((permission) => {
      if (permission === 'granted') {
        new Notification('Health Assistant Reminder', { body: message });
      }
    }).catch((error) => {
      console.error('Notification permission error:', error);
    });
  }
}

function recordUserActivity() {
  localStorage.setItem(LAST_ACTIVE_AT_KEY, String(Date.now()));
}

function getStoredTimestamp(key) {
  const value = localStorage.getItem(key);
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

// Auto-focus on input
userInput?.focus();
