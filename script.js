let tasks = [];

function addTask() {
    const input = document.getElementById("taskInput");
    const taskText = input.value.trim();

    if (taskText === "") {
        alert("Please enter a task");
        return;
    }

    tasks.push({
        text: taskText,
        completed: false
    });

    input.value = "";

    displayTasks();
}

function displayTasks() {
    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach((task, index) => {

        const li = document.createElement("li");

        li.className = "task";

        if (task.completed) {
            li.classList.add("completed");
        }

        li.innerHTML = `
            <span onclick="toggleTask(${index})">
                ${task.text}
            </span>

            <button class="delete-btn"
                    onclick="deleteTask(${index})">
                Delete
            </button>
        `;

        taskList.appendChild(li);
    });

    updateStats();
}

function toggleTask(index) {
    tasks[index].completed = !tasks[index].completed;

    displayTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);

    displayTasks();
}

function updateStats() {
    const total = tasks.length;

    const completed = tasks.filter(
        task => task.completed
    ).length;

    const pending = total - completed;

    document.getElementById("totalTasks").textContent = total;
    document.getElementById("completedTasks").textContent = completed;
    document.getElementById("pendingTasks").textContent = pending;
}