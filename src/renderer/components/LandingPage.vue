<template>
    <div>
        <v-app-bar color="primary">
            <!--            <v-app-bar-nav-icon></v-app-bar-nav-icon>-->

            <v-toolbar-title>Курсовая работа. Вариант №24.</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-toolbar-title>Мухин Артем и Килбас Игорь. Группа 6409</v-toolbar-title>
        </v-app-bar>

        <div class="body mt-3">
            <v-row no-gutters>
                <div class="d-flex flex-column text-center full-width">
                    <v-spacer></v-spacer>
                    <strong>Инструкция использования:</strong>
                    <span>1. Ввести параметры для решения дифференциального уравнения (значения параметров должны быть
                больше нуля)</span>
                    <span>2. Нажать кнопку вычислить</span>
                    <v-spacer></v-spacer>
                </div>
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
    .full-width {
        width: 100%;
    }
</style>
