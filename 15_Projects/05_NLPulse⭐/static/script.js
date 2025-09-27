// ⚡ NLPulse - Interactive NLP Analytics
class NLPulse {
    constructor() {
        this.initializeElements();
        this.bindEvents();
        this.currentResults = null;
    }

    initializeElements() {
        // Input elements
        this.textInput = document.getElementById('textInput');
        this.tokenType = document.getElementById('tokenType');
        this.stemmerType = document.getElementById('stemmerType');
        this.ngramN = document.getElementById('ngramN');
        this.lemmatizeCheck = document.getElementById('lemmatizeCheck');
        this.stopwordsCheck = document.getElementById('stopwordsCheck');
        this.summarizeCheck = document.getElementById('summarizeCheck');
        this.analyzeBtn = document.getElementById('analyzeBtn');

        // UI elements
        this.loadingIndicator = document.getElementById('loadingIndicator');
        this.resultsSection = document.getElementById('resultsSection');

        // Result elements
        this.tokensResult = document.getElementById('tokensResult');
        this.stemmedResult = document.getElementById('stemmedResult');
        this.lemmatizedResult = document.getElementById('lemmatizedResult');
        this.filteredResult = document.getElementById('filteredResult');
        this.ngramsResult = document.getElementById('ngramsResult');
        this.posTagsResult = document.getElementById('posTagsResult');
        this.nerResult = document.getElementById('nerResult');
        this.chunksResult = document.getElementById('chunksResult');
        this.summaryResult = document.getElementById('summaryResult');

        // Chart elements
        this.wordCloudCanvas = document.getElementById('wordCloudCanvas');
        this.frequencyChart = document.getElementById('frequencyChart');
    }

    bindEvents() {
        this.analyzeBtn.addEventListener('click', () => this.analyzeText());

        // Tab navigation
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchTab(e.target.dataset.tab));
        });

        // Keyboard shortcuts
        this.textInput.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                this.analyzeText();
            }
        });
    }

    switchTab(tabName) {
        // Update tab buttons
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

        // Update tab panes
        document.querySelectorAll('.tab-pane').forEach(pane => {
            pane.classList.remove('active');
        });
        document.getElementById(`${tabName}-tab`).classList.add('active');
    }

    async analyzeText() {
        const text = this.textInput.value.trim();

        if (!text) {
            alert('⚠️ Please enter some text for NLPulse to analyze.');
            return;
        }

        // Show loading
        this.showLoading();

        try {
            const requestData = {
                text: text,
                token_type: this.tokenType.value,
                stemmer: this.stemmerType.value,
                lemmatize: this.lemmatizeCheck.checked,
                ngram_n: parseInt(this.ngramN.value),
                remove_stopwords: this.stopwordsCheck.checked,
                summarize: this.summarizeCheck.checked
            };

            const response = await fetch('/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestData)
            });

            const results = await response.json();

            if (!response.ok || results.error) {
                throw new Error(results.error || `HTTP error! status: ${response.status}`);
            }

            this.currentResults = results;
            this.displayResults(results);

            // Auto-scroll to results
            this.resultsSection.scrollIntoView({ behavior: 'smooth' });

            // Show success state on button
            this.analyzeBtn.textContent = '✅ Analysis Complete!';
            setTimeout(() => {
                this.analyzeBtn.textContent = '🚀 Analyze with NLPulse';
            }, 2000);

        } catch (error) {
            console.error('Error analyzing text:', error);
            this.resultsSection.innerHTML = `
                <div class="error-box">
                    ⚠️ Oops! NLPulse hit a snag: ${error.message}
                </div>`;
        } finally {
            this.hideLoading();
        }
    }

    showLoading() {
        this.loadingIndicator.style.display = 'block';
        this.resultsSection.style.display = 'none';
        this.analyzeBtn.disabled = true;
        this.analyzeBtn.textContent = '⏳ NLPulse is processing...';
    }

    hideLoading() {
        this.loadingIndicator.style.display = 'none';
        this.resultsSection.style.display = 'block';
        this.analyzeBtn.disabled = false;
    }

    displayResults(results) {
        this.displayTokens(this.tokensResult, results.tokens);
        this.displayTokens(this.stemmedResult, results.stemmed);
        this.displayTokens(this.lemmatizedResult, results.lemmatized);
        this.displayTokens(this.filteredResult, results.filtered);
        this.displayTokens(this.ngramsResult, results.ngrams);
        this.displayPOSTags(results.pos_tags);
        this.displayNER(results.ner);
        this.displayTokens(this.chunksResult, results.chunks);
        this.createWordCloud(results.frequency);
        this.createFrequencyChart(results.frequency);
        this.displaySummary(results.summary);
    }

    displayTokens(container, tokens) {
        if (!tokens || tokens.length === 0) {
            container.innerHTML = '<p class="no-data">No data available</p>';
            return;
        }
        container.innerHTML = tokens.map(token =>
            `<span class="token">${this.escapeHtml(token)}</span>`
        ).join('');
    }

    displayPOSTags(posTags) {
        if (!posTags || posTags.length === 0) {
            this.posTagsResult.innerHTML = '<p class="no-data">No POS tags available</p>';
            return;
        }
        this.posTagsResult.innerHTML = posTags.map(([word, tag]) =>
            `<div class="pos-tag">
                <span class="pos-word">${this.escapeHtml(word)}</span>
                <span class="pos-label">${tag}</span>
            </div>`
        ).join('');
    }

    displayNER(nerEntities) {
        if (!nerEntities || nerEntities.length === 0) {
            this.nerResult.innerHTML = '<p class="no-data">No named entities found</p>';
            return;
        }
        this.nerResult.innerHTML = nerEntities.map(([label, text]) =>
            `<div class="ner-item">
                <div class="ner-label">${label}</div>
                <div class="ner-text">${this.escapeHtml(text)}</div>
            </div>`
        ).join('');
    }

    displaySummary(summary) {
        if (!summary || summary.trim() === '') {
            this.summaryResult.innerHTML = '<p class="no-data">No summary available</p>';
            return;
        }
        this.summaryResult.innerHTML = `<p>${this.escapeHtml(summary)}</p>`;
    }

    createWordCloud(frequency) {
        if (!frequency || Object.keys(frequency).length === 0) {
            this.wordCloudCanvas.parentElement.innerHTML =
                '<p class="no-data">No word frequency data available</p>';
            return;
        }

        const wordList = Object.entries(frequency)
            .filter(([word, freq]) => word.length > 2 && freq > 1)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 40);

        if (wordList.length === 0) {
            this.wordCloudCanvas.parentElement.innerHTML =
                '<p class="no-data">Not enough data for word cloud</p>';
            return;
        }

        this.createCustomWordCloud(wordList);
    }

    createCustomWordCloud(wordList) {
        const canvas = this.wordCloudCanvas;
        const ctx = canvas.getContext('2d');

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const colors = ['#19183B', '#708993', '#A1C2BD', '#E7F2EF'];
        const maxFreq = wordList[0][1];
        const minFreq = wordList[wordList.length - 1][1];

        const words = wordList.map(([word, freq], index) => {
            const normalizedFreq = (freq - minFreq) / (maxFreq - minFreq);
            const fontSize = Math.max(14, Math.min(48, 14 + normalizedFreq * 34));
            const color = colors[index % colors.length];
            return { text: word, fontSize, color, x: 0, y: 0 };
        });

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        words.forEach((word, index) => {
            ctx.font = `bold ${word.fontSize}px Segoe UI, Arial, sans-serif`;
            const textWidth = ctx.measureText(word.text).width;

            const angle = index * 0.5;
            const radius = Math.min(30 + index * 8, Math.min(canvas.width, canvas.height) / 3);

            word.x = centerX + Math.cos(angle) * radius - textWidth / 2;
            word.y = centerY + Math.sin(angle) * radius + word.fontSize / 3;

            word.x = Math.max(10, Math.min(canvas.width - textWidth - 10, word.x));
            word.y = Math.max(word.fontSize, Math.min(canvas.height - 10, word.y));
        });

        words.forEach(word => {
            ctx.font = `bold ${word.fontSize}px Segoe UI, Arial, sans-serif`;
            ctx.fillStyle = word.color;
            ctx.fillText(word.text, word.x, word.y);
        });
    }

    createFrequencyChart(frequency) {
        if (!frequency || Object.keys(frequency).length === 0) {
            return;
        }

        const sortedWords = Object.entries(frequency)
            .filter(([word]) => word.length > 2)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10);

        const labels = sortedWords.map(([word]) => word);
        const data = sortedWords.map(([, freq]) => freq);

        if (this.frequencyChartInstance) {
            this.frequencyChartInstance.destroy();
        }

        const ctx = this.frequencyChart.getContext('2d');
        this.frequencyChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{
                    label: 'Word Frequency',
                    data,
                    backgroundColor: 'rgba(112, 137, 147, 0.8)',
                    borderColor: '#19183B',
                    borderWidth: 2,
                    borderRadius: 8,
                    borderSkipped: false,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Top 10 Most Frequent Words',
                        font: { size: 16, weight: 'bold' },
                        color: '#19183B'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#19183B' },
                        grid: { color: 'rgba(25, 24, 59, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#19183B', maxRotation: 45 },
                        grid: { display: false }
                    }
                }
            }
        });
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize NLPulse
document.addEventListener('DOMContentLoaded', () => {
    new NLPulse();

    const sampleText = `Natural Language Processing (NLP) is a fascinating field...`;
    document.getElementById('textInput').placeholder =
        `⚡ Try NLPulse with your own text...\n\nExample:\n${sampleText}`;
});

// Shortcut
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        document.getElementById('analyzeBtn').click();
    }
});
