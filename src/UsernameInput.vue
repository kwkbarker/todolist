<template>
  <div class="input">
      <label :for="name" class="label">{{ name }}</label>
      <div class="error">{{ error }}</div>
      
      <input
        :type="type"
        :value="title"
        :id='name'
        @input="input"
      />
    </div>
</template>

<script>

export default {
  props: {
    value: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    rules: {
      type: Object,
      default: {}
    },
    type: {
      type: String,
      default: "text"
    }
  },

  computed: {
    error() {
      return this.validate(this.value)
    }
  },

  methods: {
    validate(value) {
      if (this.rules.required && this.length === 0) {
        return 'This value is required.'
      }

      if (this.rules.min && value.length < this.rules.min) {
        return `The minimum length id ${this.rules.min}`
      }
    },

    input($event) {
      this.$emit('update', {
        name: this.name.toLowerCase(),
        value: $event.target.value,
        valid: !this.validate($event.target.value)
      })
    }
  }
  
}
</script>


<style scoped>
.input {
  display: flex;
  flex-direction: column;
}
.label {
  display: flex;
  justify-content: space-between;
}
.error {
  color: red;
}
.input {
  width: 100%;
}
input {
  box-sizing: border-box;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid silver;
  margin: 2px;
  font-size: 16px;
  width: 100%;
  cursor: pointer;
}
</style>