document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'default';
    setTheme(savedTheme);

    document.querySelectorAll('button[data-theme]').forEach(button => {
        button.addEventListener('click', () => {
            const theme = button.getAttribute('data-theme');
            setTheme(theme);
        });
    });
});

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

document.addEventListener('DOMContentLoaded', () => {
        function updateProgressBar() {
        const progressBar = document.getElementById('progressBar');

        const totalTasks = document.querySelectorAll('li').length;
        const completedTasks = document.querySelectorAll('li.completed').length;

        const completionPercentage = (completedTasks / totalTasks) * 100;

        progressBar.style.width = completionPercentage + '%';

        if (completionPercentage < 33) {
            progressBar.className = 'progress-bar low';
        } else if (completionPercentage < 66) {
            progressBar.className = 'progress-bar medium';
        } else {
            progressBar.className = 'progress-bar high';
        }
    }
    updateProgressBar();

    document.querySelectorAll('li').forEach(task => {
        task.addEventListener('click', updateProgressBar);
    });
});