<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
//  import axios from 'axios';

export default {
  name: 'TextFx',
  data() {
    return {
      msg: 'Text',
    };
  },
};
</script>
