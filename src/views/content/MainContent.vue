<template>
  <div>
    <v-container pading-top ma-4>
      <!-- タスク追加 -->
      <v-row>
        <v-col cols="12" sm="6">
          <v-text-field
            v-if="resetFlag"
            ref="taskName"
            v-model="taskName"
            :counter="maxTaskName"
            :rules="[rules.required]"
            label="Task name"
          />
        </v-col>
        <v-col>
          <v-btn
            class="mx-2"
            fab
            dark
            color="indigo"
            :disabled="isProcessed"
            @click="submit"
          >
            <v-icon dark> mdi-plus </v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <!-- タスク一覧 -->
      <v-row v-for="(item, index) in items" :key="index">
        <v-checkbox
          v-model="item.is_check"
          hide-details
          :label="item.task_name"
        />
      </v-row>
      <v-row v-if="isNoResult" ma-4>
        <span>タスクが登録されていません。</span>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      items: [], //タスク一覧情報
      taskName: null, //タスク名
      maxTaskName: 40,
      rules: {
        required: (value) => !!value || "Required.",
      },
      formHasErrors: false, //フォーマットエラーフラグ
      isProcessed: false, //処理中フラグ
      isNoResult: false, //タスク未登録フラグ
      resetFlag: true,
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
    async getTaskList() {
      // ローディング画面表示
      this.$store.commit("setLoading", true);
      this.isProcessed = true;

      axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;
      console.log("GET /api");
      await axios
        .get("/api")
        .then(
          function (res) {
            console.log(res.data);
            if (res.status == 200) {
              if (res.data.length != 0) {
                this.items = res.data;
                this.isNoResult = false;
              } else {
                // タスク未登録の場合
                this.isNoResult = true;
              }
            }
          }.bind(this)
        )
        .catch(function (error) {
          window.alert(error);
          console.log(error);
        });

      // ローディング画面非表示
      this.isProcessed = false;
      this.$store.commit("setLoading", false);
    },
    async submit() {
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

      this.$store.commit("setLoading", true);
      this.isProcessed = false; //追加ボタン非活性
      // 追加処理
      console.log("タスク追加処理");
      let params = {
        id: null,
        task_name: this.taskName,
        is_check: 0, //false
      };
      console.log("POST /api" + params);
      await axios
        .post("/api", params)
        .then(
          function (res) {
            console.log(res);
            if (res.status == 200) {
              this.initData();
              this.getTaskList();
            }
          }.bind(this)
        )
        .catch(function (error) {
          window.alert(error);
          console.log(error);
        });

      this.$store.commit("setLoading", false);
      this.isProcessed = false;
    },
    initData() {
      this.taskName = "";
      // 再描画
      this.resetFlag = false;
      this.$nextTick(() => (this.resetFlag = true));
    },
  },
};
</script>

<style scoped>
</style>