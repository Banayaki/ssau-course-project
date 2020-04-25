import axios from '../plugins/axios'

export function postSolveEquation (payload) {
    return axios.post('/solve', payload)
}
