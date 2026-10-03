// Use relative path so it works regardless of localhost vs 127.0.0.1
const API_BASE_URL = "";

const chatEl = document.getElementById("chat");
const formEl = document.getElementById("ask-form");
const inputEl = document.getElementById("question-input");
const sendBtn = document.getElementById("send-btn");
const errorBanner = document.getElementById("error-banner");

function scrollToBottom() {
  chatEl.scrollTop = chatEl.scrollHeight;
}

function addUserMessage(text) {
  const row = document.createElement("div");
  row.className = "message user";
  row.innerHTML = `<div class="bubble"></div>`;
  row.querySelector(".bubble").textContent = text;
  chatEl.appendChild(row);
  scrollToBottom();
}

function addAssistantMessage(answer, sources) {
  const row = document.createElement("div");
  row.className = "message assistant";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = answer;
  row.appendChild(bubble);

  if (sources && sources.length > 0) {
    const sourcesEl = document.createElement("div");
    sourcesEl.className = "sources";
    sources.forEach((kbId) => {
      const chip = document.createElement("span");
      chip.className = "source-chip";
      chip.textContent = kbId;
      sourcesEl.appendChild(chip);
    });
    bubble.appendChild(sourcesEl);
  }

  chatEl.appendChild(row);
  scrollToBottom();
}

function addTypingIndicator() {
  const row = document.createElement("div");
  row.className = "message assistant typing";
  row.id = "typing-indicator";
  row.innerHTML = `<div class="bubble">Thinking…</div>`;
  chatEl.appendChild(row);
  scrollToBottom();
}

function removeTypingIndicator() {
  const el = document.getElementById("typing-indicator");
  if (el) el.remove();
}

function showError(message) {
  errorBanner.textContent = message;
  errorBanner.classList.remove("hidden");
}

function hideError() {
  errorBanner.classList.add("hidden");
}

async function askQuestion(question) {
  const response = await fetch(`${API_BASE_URL}/api/v1/support/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    let detail = `Request failed with status ${response.status}`;
    try {
      const errBody = await response.json();
      if (errBody.detail) detail = errBody.detail;
    } catch (_) {}
    throw new Error(detail);
  }

  return response.json();
}

formEl.addEventListener("submit", async (event) => {
  event.preventDefault();
  hideError();

  const question = inputEl.value.trim();
  if (!question) return;

  addUserMessage(question);
  inputEl.value = "";
  inputEl.disabled = true;
  sendBtn.disabled = true;
  addTypingIndicator();

  try {
    const data = await askQuestion(question);
    removeTypingIndicator();
    addAssistantMessage(data.answer, data.sources);
  } catch (err) {
    removeTypingIndicator();
    showError(`Something went wrong: ${err.message}`);
  } finally {
    inputEl.disabled = false;
    sendBtn.disabled = false;
    inputEl.focus();
  }
});

inputEl.focus();
