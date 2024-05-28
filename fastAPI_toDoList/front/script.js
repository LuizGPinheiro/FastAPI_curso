const apiUrl = "http://127.0.0.1:8000/tasks";

document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("task-form");
    const taskList = document.getElementById("task-list");

    taskForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;

        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ title, description }),
        });

        if (response.ok) {
            const task = await response.json();
            addTaskToDOM(task);
            taskForm.reset();
        }
    });

    taskList.addEventListener("click", async (e) => {
        if (e.target.tagName === "BUTTON") {
            const taskId = e.target.parentElement.dataset.id;

            const response = await fetch(`${apiUrl}/${taskId}`, {
                method: "DELETE",
            });

            if (response.ok) {
                e.target.parentElement.remove();
            }
        }
    });

    async function fetchTasks() {
        const response = await fetch(apiUrl);
        const tasks = await response.json();
        tasks.forEach(addTaskToDOM);
    }

    function addTaskToDOM(task) {
        const taskItem = document.createElement("li");
        taskItem.classList.add("task");
        taskItem.dataset.id = task.id;
        taskItem.innerHTML = `
            ${task.title} - ${task.description} 
            <button>Delete</button>
        `;
        taskList.appendChild(taskItem);
    }

    fetchTasks();
});
