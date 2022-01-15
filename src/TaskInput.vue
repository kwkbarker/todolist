<template>
  <div class="row-content justify-content-center mb-3">
    <label
      v-if="edit"
      :for="titleInputId"
      class="col-2"
    >Title</label>
    
    <input
      type="text"
      placeholder="Title"
      :value="title"
      :id='titleInputId'
      @input="$emit('update:title', $event.target.value)"
    /><br>

    <label
      v-if="edit"
      :for="descInputId"
      class="col-2"
    >Description</label>
    <input
      type="text"
      placeholder="Description"
      :value="description"
      :id='descInputId'
      @input="$emit('update:description', $event.target.value)"
    />
  
   
    <div class="importance-input">
      <h6 class="col-2">Importance</h6>
      
      <div class='btn-group btn-group-toggle' role="group" data-toggle='buttons'
        id="impTogg">
        <input
          type='radio'
          class='btn-check'
          name='importance'
          value='danger'
          checked='true'
          :id='dangBtnId'
          @input="$emit('update:importance', 'danger')"
        />
        <label class='btn btn-outline-danger' :for='dangBtnId'>
          Urgent
        </label>
        <input
          type='radio'
          class='btn-check'
          name='importance'
          value='warning'
          :id='warnBtnId'
          @input="$emit('update:importance', 'warning')"

        />
        <label class='btn btn-outline-warning' :for='warnBtnId'>
          Soon
        </label>
        <input
          type='radio'
          class='btn-check'
          name='importance'
          value='secondary'
          :id='secBtnId'
          @input="$emit('update:importance', 'secondary')"
        />
        <label class='btn btn-outline-secondary' :for='secBtnId'>
          Whenever
        </label>
      </div>
    </div>

  </div>

</template>

<script>
export default {
  emits: [
    'update:title', 
    'update:description', 
    'update:importance'
  ],

  props: {
    title: {
      type: String
    },
    description: {
      type: String
    },
    edit: {
      type: Boolean,
      default: false
    },
    task: {
      id: Number,
      title: String,
      description: String,
      importance: String
    }
  },

  computed: {
    // compute element IDs to access in methods or within parent component (Task)
    titleInputId() {
      if (this.task) {
        return 'title-input-field-' + this.task.id
      } else {
        return 'title-input-field-main'
      }
    },

    descInputId() {
      if (this.task) {
        return 'description-input-field-' + this.task.id
      } else {
        return 'description-input-main'
      }
    },

    dangBtnId() {
      if (this.task) {
        return 'dangBtnId-' + this.task.id
      } else {
        return 'dangBtnId'
      }
    },

    warnBtnId() {
      if (this.task) {
        return 'warnBtnId-' + this.task.id
      } else {
        return 'warnBtnId'
      }
    },

    secBtnId() {
      if (this.task) {
        return 'secBtnId-' + this.task.id
      } else {
        return 'secBtnId'
      }
    },


  }

}
</script>

<style scoped>

input {
  height: 30px;
  width: 200px;
  padding: 5px;
  margin: 30px;
}
.importance-input {
  margin-left: 30px;
  margin-top: 10px;
}
</style>