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
            <button v-on:click="sendMSG();getBack();">Send</button>
            </td>
            <td> {{out_message}} </td>
          </tbody>
    </table>
    <div class="imgContent">
      <div class="imagePreview">
        <img :src="uploadedImage" style="width:100%;" />
      </div>
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        <button v-on:click="submitFile()">Submit</button>
    </div>
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
      out_message: '',
      file: '',
    };
  },
  methods: {
    sendMSG() {
      const path = 'http://127.0.0.1:5000/';
      return axios.post(path, this.in_message);
    },
    getBack() {
      const path = 'http://127.0.0.1:5000/';
      axios.get(path)
        .then((res) => {
          this.out_message = res.data.txt;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    handleFileUpload() {
    },
  },
};
</script>
