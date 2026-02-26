document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('qr-form');
    const btnGenerate = document.querySelector('.btn-generate');
    const qrContainer = document.getElementById('qr-preview-container');
    const btnDownload = document.getElementById('btn-download');

    // Color inputs logic
    const fgInput = document.getElementById('fg_color');
    const bgInput = document.getElementById('bg_color');

    fgInput.addEventListener('input', (e) => {
        e.target.nextElementSibling.textContent = e.target.value;
    });

    bgInput.addEventListener('input', (e) => {
        e.target.nextElementSibling.textContent = e.target.value;
    });

    let currentObjectUrl = null;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = document.getElementById('data').value.trim();
        const fg_color = fgInput.value;
        const bg_color = bgInput.value;
        const style = document.getElementById('style').value;

        if (!data) return;

        // Start loading
        btnGenerate.classList.add('loading');
        btnGenerate.disabled = true;

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    data,
                    fg_color,
                    bg_color,
                    style
                })
            });

            if (!response.ok) {
                throw new Error('Failed to generate QR code');
            }

            const blob = await response.blob();

            // Generate local URL
            if (currentObjectUrl) {
                URL.revokeObjectURL(currentObjectUrl);
            }
            currentObjectUrl = URL.createObjectURL(blob);

            // Show image
            qrContainer.innerHTML = `<img src="${currentObjectUrl}" alt="Generated QR Code">`;
            qrContainer.classList.add('active');

            // Setup download
            btnDownload.onclick = () => {
                const a = document.createElement('a');
                a.href = currentObjectUrl;
                a.download = `ChromaQR_${new Date().getTime()}.png`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            };
            btnDownload.classList.remove('hidden');

        } catch (error) {
            console.error('Error:', error);
            alert('Failed to generate QR code. Please try again later.');
        } finally {
            // End loading
            btnGenerate.classList.remove('loading');
            btnGenerate.disabled = false;
        }
    });
});
