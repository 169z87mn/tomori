<template>
  <div class="newRadioForm">
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field v-model="title" :rules="nameRules" label="タイトル" required></v-text-field>
      <v-text-field v-model="personality" :rules="nameRules" label="パーソナリティ" required></v-text-field>
      <v-text-field v-model="broadcast_station" :rules="nameRules" label="配信局" required></v-text-field>
      <v-text-field v-model="start_time" :rules="nameRules" label="配信日時(開始)" required></v-text-field>
      <v-text-field v-model="end_time" :rules="nameRules" label="配信日時(終了)" required></v-text-field>
      <v-text-field v-model="details" :rules="nameRules" label="詳細" required></v-text-field>
      <v-text-field v-model="official_site" :rules="nameRules" label="公式サイト" required></v-text-field>
      <v-text-field v-model="mail" :rules="nameRules" label="番組メール" required></v-text-field>
      <v-text-field v-model="twitter_account" :rules="nameRules" label="公式Twitter" required></v-text-field>
      <v-text-field v-model="twitter_tag" :rules="nameRules" label="Twitterタグ" required></v-text-field>
      <v-text-field v-model="price" :rules="nameRules" label="料金" required></v-text-field>
      <v-text-field v-model="start_date" :rules="nameRules" label="配信開始日" required></v-text-field>
      <v-text-field v-model="end_date" :rules="nameRules" label="配信開始日" required></v-text-field>
      <v-text-field v-model="count" :rules="nameRules" label="配信回数" required></v-text-field>
      <v-text-field v-model="style" :rules="nameRules" label="配信形式" required></v-text-field>
      <v-text-field v-model="writer" :rules="nameRules" label="構成作家" required></v-text-field>
      <v-text-field v-model="week" :rules="nameRules" label="曜日" required></v-text-field>
      <v-btn color="dark" class="mr-4" @click="submit">Submit</v-btn>
      <v-btn color="dark" class="mr-4" @click="reset">Reset Form</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    title: '',
    personality: '',
    broadcast_station: '',
    start_time: '',
    end_time: '',
    details: '',
    official_site: '',
    mail: '',
    twitter_account: '',
    twitter_tag: '',
    price: '',
    start_date: '',
    end_date: '',
    count: '',
    style: '',
    writer: '',
    week: '',
  }),

  methods: {
    reset () {
      this.$refs.form.reset()
    },
    submit () {
      
    },
  },
}
</script>

<style lang="scss" scoped>
.newRadioForm {
  margin: 100px
}
</style>