import {postSolveEquation} from '../../api/SolverAPI'

export const SET_PARAMETER_VALUE = 'SET_PARAMETER_VALUE'
export const SET_PLOT_VALUES = 'SET_PLOT_VALUES'
export const SOLVE_EQUATION = 'SOLVE_EQUATION'

const MUTATION_SET_PARAMETER_VALUE = 'MUTATION_SET_PARAMETER_VALUE'
const MUTATION_SET_PLOT_VALUE = 'MUTATION_SET_PLOT_VALUE'

const state = {
    parameters: {
        'K': 0.59,
        'C': 1.24,
        'R': 5,
        'T': 20,
        'Nx': 100,
        'Nt': 100
    },
    eqParametersNames: ['K', 'C', 'R', 'T'],
    numericalParametersNames: ['Nx', 'Nt'],
    plotX: [],
    plotY: [],
    plotNumY: []
}

const getters = {
    getEqParametersNames: state => state.eqParametersNames,
    getNumericalParametersNames: state => state.numericalParametersNames,
    getParameters: state => state.parameters,
    getXValues: state => state.plotX,
    getYValues: state => state.plotY,
    getNumericalYValues: state => state.plotNumY
}

const mutations = {
    [MUTATION_SET_PARAMETER_VALUE] (state, payload) {
        state.parameters[payload.name] = payload.value
    },
    [MUTATION_SET_PLOT_VALUE] (state, payload) {
        state.plotX = payload.analytic.x
        state.plotY = payload.analytic.y
        state.plotNumY = payload.numerical.y
    }
}

const actions = {
    // on of the vuex-electron issue. We can't call mutation from renderer context
    [SET_PARAMETER_VALUE] ({commit, state}, payload) {
        commit(MUTATION_SET_PARAMETER_VALUE, payload)
    },
    [SET_PLOT_VALUES] ({commit, state}, payload) {
        commit(MUTATION_SET_PLOT_VALUE, payload)
    },
    [SOLVE_EQUATION] ({dispatch, state}) {
        return new Promise((resolve, reject) => {
            postSolveEquation(state.parameters)
                .then(response => {
                    dispatch(SET_PLOT_VALUES, response.data)
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
        })
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
