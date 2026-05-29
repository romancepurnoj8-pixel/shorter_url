document.addEventListener('DOMContentLoaded', () => {
    // Реализация кнопки быстрого копирования ссылки в буфер обмена
    const copyButtons = document.querySelectorAll('.btn-copy');

    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const textToCopy = button.getAttribute('data-clipboard');
            
            // Навигационное API для копирования
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalEmoji = button.innerText;
                button.innerText = '✅';
                setTimeout(() => {
                    button.innerText = originalEmoji;
                }, 1500);
            }).catch(err => {
                console.error('Не удалось скопировать: ', err);
            });
        });
    });
});