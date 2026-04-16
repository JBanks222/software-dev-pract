document.addEventListener("DOMContentLoaded", loadTasks);

function createTaskElement(id, task) {
    const list = document.getElementById("taskList");
    const item = document.createElement("li");
    item.textContent = `${id}. ${task}`;
    list.appendChild(item);
}

function loadTasks() {
    fetch("/get_tasks")
        .then((response) => response.json())
        .then((data) => {
            const list = document.getElementById("taskList");
            list.innerHTML = "";

            data.forEach((task) => {
                createTaskElement(task.id, task.task);
            });
        });
}

function addTask() {
    const input = document.getElementById("taskinput");
    const task = input.value.trim();

    if (task === "") return;

    fetch("/add_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ task: task })
    }).then(() => {
        input.value = "";
        loadTasks();
    });
}

function deleteTask(id) {
    fetch("/delete_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: id })
    }).then(() => {
        loadTasks();
    });
}

function createTaskElement(id, taskText) {
    const list = document.querySelector("#taskList");
    const li = document.createElement("li");
    li.classList.add("task-item");
    li.textContent = taskText + " ";

    const btn = document.createElement("button");
    btn.innerHTML = "&#10060;";
    btn.onclick = () => deleteTask(id);
    btn.classList.add("btn-delete-item");

    li.appendChild(btn);
    list.appendChild(li);
}
