<template>
    <div>
        <v-app-bar color="primary">
            <!--            <v-app-bar-nav-icon></v-app-bar-nav-icon>-->

            <v-toolbar-title>Курсовая работа. Вариант №24.</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-toolbar-title>Мухин Артем и Килбас Игорь. Группа 6309</v-toolbar-title>
        </v-app-bar>

        <div class="body mt-3">
            <v-row no-gutters>
                <v-spacer></v-spacer>
                <span>Dialog box</span>
                <v-spacer></v-spacer>
            </v-row>
            <v-row no-gutters>
                <v-col>
                    <equation-view></equation-view>
                </v-col>
                <v-col>
                    <plot-view></plot-view>
                </v-col>
            </v-row>
        </div>
    </div>
</template>

<script>
    import EquationView from './EquationView'
    import PlotView from './PlotView'

    export default {
        name: 'LandingPage',
        components: {PlotView, EquationView}
    }
</script>

<style scoped>

</style>
