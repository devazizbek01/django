function copyToClipboardWithTooltip(button) {
    const currentUrl = window.location.href;

    navigator.clipboard.writeText(currentUrl).then(() => {
        const original = button.innerHTML;
        button.innerHTML = '✅ silka Nusxalandi!';
        button.classList.add('copied');

        setTimeout(() => {
            button.innerHTML = original;
            button.classList.remove('copied');
        }, 2000);
    }).catch(() => {
        alert('Nusxalash amalga oshmadi');
    });
}