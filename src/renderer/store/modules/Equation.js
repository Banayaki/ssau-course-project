import {postSolveEquation} from '../../api/SolverAPI'

export const SET_PARAMETER_VALUE = 'SET_PARAMETER_VALUE'
export const SET_PLOT_VALUES = 'SET_PLOT_VALUES'
export const SOLVE_EQUATION = 'SOLVE_EQUATION'
export const SET_WAITING = 'SET_WAITING'

const MUTATION_SET_PARAMETER_VALUE = 'MUTATION_SET_PARAMETER_VALUE'
const MUTATION_SET_PLOT_VALUE = 'MUTATION_SET_PLOT_VALUE'
const MUTATION_CLEAR_PLOT_VALUE = 'MUTATION_CLEAR_PLOT_VALUE'
const MUTATION_SET_WAITING = 'MUTATION_SET_WAITING'

const state = {
    parameters: {
        'K': 0.59,
        'C': 1.24,
        'R': 5,
        'T': 20,
        'Nx': 50,
        'Nt': 100,
        'Implicit': true,
        'Explicit': true,
        'force_stability': false
    },
    eqParametersNames: ['K', 'C', 'R', 'T'],
    numericalParametersNames: ['Nx', 'Nt'],
    availableMethods: ['Implicit', 'Explicit'],
    plotX: [],
    plotY: [],
    plotExplicitY: [],
    plotImplicitY: [],
    waitingStatus: false,
    stability: {'stable': true}
}

const getters = {
    getEqParametersNames: state => state.eqParametersNames,
    getNumericalParametersNames: state => state.numericalParametersNames,
    getAvailableSolvers: state => state.availableMethods,
    getParameters: state => state.parameters,
    getXValues: state => state.plotX,
    getYValues: state => state.plotY,
    getExplicitYValues: state => state.plotExplicitY,
    getImplicitYValues: state => state.plotImplicitY,
    getWaitingStatus: state => state.waitingStatus,
    getStabilityStatus: state => state.stability
}

const mutations = {
    [MUTATION_SET_PARAMETER_VALUE] (state, payload) {
        state.parameters[payload.name] = payload.value
    },
    [MUTATION_SET_PLOT_VALUE] (state, payload) {
        console.log(payload)
        state.plotX = payload.analytic.x
        state.plotY = payload.analytic.y
        if (payload.explicit) {
            state.plotExplicitY = payload.explicit.y
            state.stability = payload.explicit.stability
        }
        if (payload.implicit) {
            state.plotImplicitY = payload.implicit.y
        }
    },
    [MUTATION_CLEAR_PLOT_VALUE] (state) {
        state.plotX = []
        state.plotY = []
        state.plotExplicitY = []
        state.plotImplicitY = []
    },
    [MUTATION_SET_WAITING] (state, payload) {
        state.waitingStatus = payload
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
    [SET_WAITING] ({commit, state}, payload) {
        commit(MUTATION_SET_WAITING, payload)
    },
    [SOLVE_EQUATION] ({commit, dispatch, state}, payload) {
        commit(MUTATION_CLEAR_PLOT_VALUE)
        commit(MUTATION_SET_WAITING, true)
        return new Promise((resolve, reject) => {
            postSolveEquation(payload)
                .then(response => {
                    dispatch(SET_PLOT_VALUES, response.data)
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
                .finally(() => {
                    commit(MUTATION_SET_WAITING, false)
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
