import axios from "axios";

interface User {
    fullname: string;
    email: string;
    password: string;
}

const apiClient = axios.create({
    baseURL: 'http://localhost:5000',
    headers: {'Content-type': 'application/json'},
});

const create = async (user: User) => {
    const response = await apiClient.post('/users', user);
    return response.data;
};

const update = async (id: string, user: User) => {
    const response = await apiClient.put(`/users/${id}`, user);
    return response.data;
}

const findAll = async () => {
    const response = await apiClient.get('/users');
    return response.data;
};

const findByID = async (id: string) => {
    const response = await apiClient.get(`/users/${id}`);
    return response.data;
};

const deleteByID = async (id: string) => {
    const response = await apiClient.delete(`/users/${id}`);
    return response.data;
};

export default {
    create,
    update,
    findAll,
    findByID,
    deleteByID,
};
