document.addEventListener('DOMContentLoaded', () => {
    const languageButton = document.querySelector('.language');
    languageButton.addEventListener('click', () => {
        alert('Переключение языка пока не реализовано');
    });

    const newMeetingButton = document.querySelector('.new-meeting');
    newMeetingButton.addEventListener('click', () => {
        openModal();
    });

    function openModal() {
        const modal = document.createElement('div');
        modal.classList.add('modal');
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close-button">&times;</span>
                <h2>Создать видеовстречу</h2>
                <p>Форма для создания видеовстречи</p>
                <button class="submit-meeting">Создать</button>
            </div>
        `;
        document.body.appendChild(modal);

        const closeButton = modal.querySelector('.close-button');
        closeButton.addEventListener('click', () => {
            closeModal(modal);
        });

        const submitButton = modal.querySelector('.submit-meeting');
        submitButton.addEventListener('click', () => {
            alert('Видеовстреча создана!');
            closeModal(modal);
        });
    }

    function closeModal(modal) {
        document.body.removeChild(modal);
    }
});
