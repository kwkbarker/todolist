import { createStore } from 'vuex'

// module: tasks
const tasks = {
    namespaced: true,

    state() {
        return {
            all: []
        }
    },

    mutations: {
        setTasks(state, tasks) {
            if (tasks) {
                state.all = tasks
            } else {
                state.all = []
            }
        },

        addTask(state, task) {
            state.all.push(task)
        },

        editTask(state, newTask) {
            state.all[newTask.id] = newTask
        },

        deleteTask(state, taskId) {
            state.all.splice([taskId], 1)
        },

        fixIds(state) {
            for (var i = 0; i < state.all.length; i++){
                state.all[i].id = i
            }
        }

    },

    actions: {

        // fetch
        fetch(ctx) {
            var str_data =  localStorage.getItem('tasks')
            var arr = JSON.parse(str_data)
            ctx.commit('setTasks', arr)
        },

        save(ctx) {
            const parsed = JSON.stringify(ctx.state.all)
            localStorage.setItem('tasks', parsed)
        }
    },

    getters: {
        count(state) {
            return state.all.length
        },

        nextId(state) {
            if (state.all.length > 0) {
                return state.all.length
            } else {
                return 0
            }
        },

        // title(state, id) {
        //     return state.all[id-1].title
        // },

        // description(state, id) {
        //     return state.all[id-1].description
        // },

        // importance(state, id) {
        //     return state.all[id-1].importance
        // },
    }
}

export const store = createStore({
    modules: {
        tasks
    }
})