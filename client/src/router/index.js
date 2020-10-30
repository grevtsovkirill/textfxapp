import Vue from 'vue';
import VueRouter from 'vue-router';
import TextFx from '../components/TextFx.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'TextFx',
    component: TextFx,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
