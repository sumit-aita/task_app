<template>
  <div>
    <v-container pading-top ma-4>
      <v-row>
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="taskName"
            :counter="maxTaskName"
            :rules="[rules.required]"
            label="Task name"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-btn class="mx-2" fab dark color="indigo">
            <v-icon dark> mdi-plus </v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row v-for="(item, index) in items" :key="index">
        <v-checkbox
          v-model="item.status"
          hide-details
          :label="item.task_name"
        ></v-checkbox>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      taskNasme: null,
      maxTaskName: 40,
      rules: {
        required: value => !!value || 'Required.',
      }
    };
  },
  created() {
    this.getTaskList();
  },
  computed: {
    form () {
      return {
        taskName: this.taskNasme
      }
    }
  },
  methods: {
    getTaskList() {
      this.items = [
        {
          task_name: "sampleTaskName1",
          status: true,
        },
        {
          task_name: "sampleTaskName2",
          status: false,
        },
      ];
    },
    submit () {
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true

          this.$refs[f].validate(true)
        })
      },
  },
};
</script>

<style scoped>
</style>