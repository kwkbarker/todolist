<template>
  <div class="wrapper">
    <div class="tasks-list">
      <h2 class="grey">Tasks</h2>
      <div
           v-if="tasks.length > 0"
        >
          <div class="tasks"
            v-for="task in tasks"
            :key="task.id"
          >
            <task :task="task"
            @refreshTasks='refreshTasks'
            />
          </div>
      </div>
      <div
          v-else
        >
        <h5>No tasks to show.</h5>
      </div>
    </div>
  <div class="new-task">
    <h2 class="grey">New Task</h2>
    <form @submit.prevent="addTask">
      <task-input
        v-model:title="title"
        v-model:description="description"
        v-model:importance="importance"
      />
      <button
        type="submit"
        class="btn btn-primary"
      >
        Submit
      </button>
    </form>
  </div>
  </div>
</template>

<script>

import Task from './Task.vue'
import TaskInput from './TaskInput.vue'

export default {
  components: {
    Task,
    TaskInput,
  },

  data() {
    return {
      title: null,
      description: null,
      importance: null,
    }
  },

  // // fetch tasks from local storage
  // or initialize empty storage
  mounted() {
    this.refreshTasks()
  },

  methods: {
    addTask() {
      if (!this.title) {
        return
      }

      const newTask = {
        id: this.$store.getters['tasks/nextId'],
        title: this.title,
        description: this.description,
        importance: this.importance
      }
      this.$store.commit('tasks/addTask', newTask)
      this.$store.dispatch('tasks/save')
      this.title = null
      this.description = null
      this.importance = null

      this.$emit('refreshTasks')
    },

    refreshTasks() {
      this.$store.dispatch('tasks/fetch')
      this.title = null
      this.description = null
      this.importance = null
    },

  },

  computed: {
    tasks() {
      return this.$store.state.tasks.all
    }
  }

}
</script>

<style scoped>

button {
  margin-left: 30px;
}

.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.tasks {
  width: 100%;
}

edit-input {
  margin:0;
}

.grey {
  color: rgb(110, 110, 110);
}

h2, h5 {
  margin-left: 30px;
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>