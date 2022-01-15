<template>
    <div :id="editWindowName" class="modal fade">
        <div class='modal-dialog modal-lg'>
            <div class="modal-content">
                <div class='modal-header'>
                    <h4>Edit Task</h4>
                    <button type="button" class="close" data-bs-dismiss='modal'>
                        &times;
                    </button>
                </div>

                <div class='modal-body'>
                    <task-input
                        :edit="edit"
                        :task="task"
                        v-model:title="newTask.newTitle"
                        v-model:description="newTask.newDesc"
                        v-model:importance="newTask.newImport"
                    />
                
                    <button
                        data-bs-dismiss="modal"
                        class="btn btn-primary"
                        @click="editTask"
                    >
                        Submit
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TaskInput from './TaskInput.vue'
export default {
    emits: ['editTask'],
    components: {
        TaskInput
    },

    props: {
        task: {
            id: Number,
            title: String,
            description: String,
            importance: String
        },
    },

    data() {
        return {
            newTask: {
                newTitle: null,
                newDesc: null,
                newImport: null
            },
            danger: null,
            warning: null,
            secondary: null,

            edit: true
        }
    },

    methods: {
        editTask() {
            this.$emit('editTask', {
                title: this.newTask.newTitle,
                description: this.newTask.newDesc,
                importance: this.newTask.newImport
            })
        },
    },

    computed: {
        editWindowName() {
            return "editWindow" + this.task.id
        }
    }
    
}
</script>

<style scoped>

</style>