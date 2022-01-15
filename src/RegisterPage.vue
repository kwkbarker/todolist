<template>
  <div class="container">
    <form 
      class="form-register"
      @submit.prevent="registerUser"
    >
      <div class='row row-content justify-content-center mt-2'>
          <h1 class="h3 mb-3 font-weight-normal">
              Login
          </h1>
      </div>
      <br>
      <div class='row row-content justify-content-center textfield'>
          <div class="col-sm-2"></div>
          <div class="col-12 col-sm-8">
            <username-input 
              name="Username"
              :rules="{ required: true, min: 5 }"
              :value="username.value"
              :type="text"
              @update="update"
            />
          </div>

          <div class="col-sm-2"></div>
          <div class="col-12 col-sm-8">
            <username-input 
              name="Password"
              :rules="{ required: true, min: 5 }"
              :value="username.value"
              :type='password'
              @update="update"
            />
          </div>

        <div class="col-sm-2"></div>
      </div>

      <div class="row row-content mb-2 justify-content-center">
        <button class="btn btn-lg btn-primary" type="submit" :disabled="!valid">
          Login
        </button>
      </div>

      <div class="row row-content justify-content-end col-sm-10 mt-4">
        <h6>Don't have an account?</h6>
      </div>
      <div class='row row-content justify-content-end col-sm-10'>
        <router-link to="/register">Register</router-link>
      </div>
    </form>
  </div>

</template>

<script>
import UsernameInput from './UsernameInput.vue'

export default {
  components: { UsernameInput },
  data() {
    return {
      username: null,
      password: null
    }
  },

  methods: {
    registerUser() {
      console.log("register")
    }
  },

  computed: {
    valid() {
      return this.username.valid && this.password.valid
    }
  }
}
</script>

<style scoped>

</style> 