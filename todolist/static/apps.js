document.addEventListener('DOMContentLoaded', () => {
    clearFields();
})

function clearFields() {
    document.getElementById('title').value = '';
    document.getElementById('description').value = '';
}

function fillFields(task) {
    console.log(task);
    
    var title = document.getElementById(`title${task}`);
    console.log(title.innerHTML);
    
    var edittitle = document.getElementById(`edittitle${task}`);
    var description = document.getElementById(`description${task}`);
    var editdescription = document.getElementById(`editdescription${task}`);
    
    edittitle.value = title.innerHTML;
    editdescription.value = description.innerHTML;
}
