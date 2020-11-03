<template>
  <div class="container">
   <div class="row">
      <div class="col-sm-10">
    <button type="button" class="btn btn-primary">{{ msg1 }}</button>
    <br>
    <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Text</th>
              <th scope="col">New text</th>
            </tr>
          </thead>
          <tbody>

            <td> <input v-model="in_message">
            <button v-on:click="sendAddress()">Send</button>
            </td>
            <td> {{in_message}} </td>
          </tbody>
    </table>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TextFx',
  data() {
    return {
      msg1: 'Text',
      in_message: 'sd',
    };
  },
  methods: {
    sendAddress() {
      const path = 'http://127.0.0.1:5000/';
      return axios.post(path, this.in_message);
    },
  },

};
</script>
