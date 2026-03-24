document.addEventListener('DOMContentLoaded', () => {
    const topicInput = document.getElementById('topicInput');
    const explainBtn = document.getElementById('explainBtn');
    const resultContent = document.getElementById('resultContent');
    const loading = document.getElementById('loading');
    const placeholder = document.getElementById('placeholder');
    const cardTitle = document.getElementById('cardTitle');
    const latencySpan = document.getElementById('latency');

    const handleExplain = async () => {
        const topic = topicInput.value.trim();
        if (!topic) return;

        // Reset UI
        placeholder.classList.add('hidden');
        resultContent.classList.add('hidden');
        loading.classList.remove('hidden');
        cardTitle.textContent = `Explaining: ${topic}`;
        latencySpan.textContent = "Calculating...";
        
        const startTime = performance.now();

        try {
            const response = await fetch('/explain', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Failed to fetch explanation');
            }

            const data = await response.json();
            
            // Calculate Latency
            const endTime = performance.now();
            const duration = ((endTime - startTime) / 1000).toFixed(2);
            latencySpan.textContent = `${duration}s`;

            // Display Result with typewriter effect
            loading.classList.add('hidden');
            resultContent.classList.remove('hidden');
            typeWriter(resultContent, data.explanation);

        } catch (error) {
            loading.classList.add('hidden');
            resultContent.classList.remove('hidden');
            resultContent.innerHTML = `<p style="color: #ff6b6b;"><i class="fa-solid fa-triangle-exclamation"></i> Error: ${error.message}</p>`;
            latencySpan.textContent = "Error";
        }
    };

    // Typewriter effect function
    const typeWriter = (element, text) => {
        element.innerHTML = '';
        let i = 0;
        const speed = 10; // ms per character

        function type() {
            if (i < text.length) {
                // Handle newlines correctly
                if (text.charAt(i) === '\n') {
                    element.innerHTML += '<br>';
                } else {
                    element.innerHTML += text.charAt(i);
                }
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    };

    // Event Listeners
    explainBtn.addEventListener('click', handleExplain);

    topicInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleExplain();
        }
    });

    // Optional: Auto-focus input on load
    topicInput.focus();
});
