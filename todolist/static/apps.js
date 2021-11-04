document.addEventListener('DOMContentLoaded', () => {
    clearFields();
})

function clearFields() {
    document.getElementById('title').value = '';
    document.getElementById('description').value = '';
}

function editTask(task) {
    console.log(task);
    var modal = document.getElementById(`editWindow${task}`);
    var btn = document.getElementById(`edit${task}`);
    var span = document.getElementsByClassName(`close${task}`);
    var title = document.getElementById(`title${task}`);
    var edittitle = document.getElementById(`edittitle${task}`);
    var description = document.getElementById(`description${task}`);
    var editdescription = document.getElementById(`editdescription${task}`);

    edittitle.innerHTML = title.innerHTML;
    editdescription.innerHTML = description.innerHTML;
    
    console.log(modal)
    modal.style.display == "block";
    
    span.onclick = function() {
        modal.style.display == "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display == "none";
        }
    }

    submit = document.getElementById(`submit${task}`);
    submit.onclick = function() {
        fetch('/tasks', {
            method: 'POST',
            body: JSON.stringify({
                title: edittitle.value,
                description: editdescription.value,
                name: 'edit',
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })

        var edittitle = document.getElementById(`edittitle${task}`);
        var editdescription = document.getElementById(`editdescription${task}`);

    }

}