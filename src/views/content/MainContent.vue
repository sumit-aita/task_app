<template>
  <div>
    <v-container pading-top ma-4>
      <v-row>
        <v-col cols="12" sm="6">
          <v-text-field
            ref="taskName"
            v-model="taskName"
            :counter="maxTaskName"
            :rules="[rules.required]"
            label="Task name"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-btn class="mx-2" fab dark color="indigo" @click="submit">
            <v-icon dark> mdi-plus </v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row v-for="(item, index) in items" :key="index">
        <v-checkbox
          v-model="item.is_check"
          hide-details
          :label="item.task_name"
        ></v-checkbox>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      items: [],
      taskName: null,
      maxTaskName: 40,
      rules: {
        required: (value) => !!value || "Required.",
      },
      formHasErrors: false,
    };
  },
  created() {
    this.getTaskList();
  },
  computed: {
    form() {
      return {
        taskName: this.taskName,
      };
    },
  },
  methods: {
    getTaskList() {
      axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT
      console.log("GET /api");
      axios.get("/api").then(function(res){
        console.log(res.data);
        this.items = res.data;
      }.bind(this)).catch(function(error){
        console.log(error);
      })
    },
    submit() {
      // フォーマットチェック処理
      this.formHasErrors = false;

      Object.keys(this.form).forEach((f) => {
        if (!this.form[f]) this.formHasErrors = true;

        this.$refs[f].validate(true);
      });
      if (this.formHasErrors) {
        console.log("フォーマットエラー");
        return;
      }
      // 追加処理
      console.log("タスク追加処理");
      let params = {
        "id": null,
        "task_name": this.taskName,
        "is_check": 0 //false
      }
      console.log("POST /api" + params);
       axios.post("/api", params).then(function(res){
        console.log(res);
          if (res.status == 200) {
            this.initData();
            this.getTaskList();
         }
      }.bind(this)).catch(function(error){
        console.log(error);
      })
    },
    initData() {
      this.taskName = "";
    }
  },
};
</script>

<style scoped>
</style>