document.addEventListener('DOMContentLoaded', function () {
    // Handle todo item checkbox toggles
    setupTodoToggles();
    setupMessageDismissal();
    setupFormValidation();
    setupAnimations();
});

function setupTodoToggles() {
    document.querySelectorAll('.todo-checkbox input').forEach(checkbox => {
        checkbox.addEventListener('change', async function () {
            const todoItem = this.closest('.todo-item');
            const todoId = todoItem.dataset.id;

            try {
                const response = await fetch(`/todo/toggle/${todoId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) throw new Error('Network response was not ok');

                const data = await response.json();
                todoItem.classList.toggle('completed', data.status);

                // Add animation
                todoItem.style.animation = 'none';
                todoItem.offsetHeight; // Trigger reflow
                todoItem.style.animation = 'updateTodo 0.3s ease-in-out';
            } catch (error) {
                console.error('Error:', error);
                showMessage('Failed to update task status', 'error');
            }
        });
    });
}

function setupMessageDismissal() {
    document.querySelectorAll('.message').forEach(message => {
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => message.remove(), 300);
        }, 5000);

        // Click to dismiss
        message.addEventListener('click', () => {
            message.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => message.remove(), 300);
        });
    });
}

function setupFormValidation() {
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function (e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    showFieldError(field, 'This field is required');
                } else {
                    field.classList.remove('error');
                    removeFieldError(field);
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });
}

function setupAnimations() {
    // Add entrance animation to todo items
    document.querySelectorAll('.todo-item').forEach((item, index) => {
        item.style.animation = `fadeIn 0.3s ease-out ${index * 0.1}s both`;
    });
}

function showMessage(message, type = 'info') {
    const messagesContainer = document.querySelector('.messages') || createMessagesContainer();
    const messageElement = document.createElement('div');
    messageElement.className = `message ${type}`;
    messageElement.textContent = message;

    messagesContainer.appendChild(messageElement);
    messageElement.style.animation = 'slideIn 0.3s ease-out';

    setTimeout(() => {
        messageElement.style.animation = 'slideOut 0.3s ease-out forwards';
        setTimeout(() => messageElement.remove(), 300);
    }, 5000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages';
    document.body.appendChild(container);
    return container;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Add keyframe animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes updateTodo {
        0% { transform: scale(1); }
        50% { transform: scale(0.95); }
        100% { transform: scale(1); }
    }
    
    @keyframes slideOut {
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);