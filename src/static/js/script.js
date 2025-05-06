document.addEventListener('DOMContentLoaded', function() {
    const processBtn = document.getElementById('process-btn');
    const copyBtn = document.getElementById('copy-btn');
    const keyInput = document.getElementById('key');
    const textInput = document.getElementById('text');
    const resultTextarea = document.getElementById('result');
    
    processBtn.addEventListener('click', async function() {
        const key = keyInput.value.trim();
        const text = textInput.value.trim();
        const mode = document.querySelector('input[name="mode"]:checked').value;
        
        if (!key) {
            alert('Please enter a key');
            keyInput.focus();
            return;
        }
        
        if (!text) {
            alert('Please enter text to process');
            textInput.focus();
            return;
        }
        
        try {
            const response = await fetch('/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ key, text, mode })
            });
            
            const data = await response.json();
            
            if (data.error) {
                alert('Error: ' + data.error);
            } else {
                resultTextarea.value = data.result;
            }
        } catch (error) {
            alert('Error processing request: ' + error.message);
        }
    });
    
    copyBtn.addEventListener('click', function() {
        resultTextarea.select();
        document.execCommand('copy');
        
        // Visual feedback
        const originalText = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        setTimeout(() => {
            copyBtn.textContent = originalText;
        }, 1500);
    });
});
