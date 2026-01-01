import { useState, useEffect } from 'react';
import Service from '../services/Service';
import { useAlert } from '../contexts/AlertContext';
import { useNavigate } from 'react-router-dom';

interface User {
    _id: {
        $oid: string;
    };
    email: string;
    fullname: string;
    modification: {
        $date: string;
    };
    password: string;
    registration: {
        $date: string;
    };
}

function Users() {
    const [users, setUsers] = useState<User[]>([]);
    const { setAlertMessage, setAlertVariant } = useAlert();
    const navigate = useNavigate();

    const fetchUsers = async () => {
        try {
            const data = await Service.findAll();
            setUsers(data);
        } catch (error) {
            setAlertMessage('Error fetching users!');
            setAlertVariant('danger');
            console.error('Error fetching users:', error);
        }
    };

    useEffect(() => {fetchUsers();}, []);

    const deleteUser = async (id: string) => {
        if (window.confirm('Are you sure you want to delete this contact?')) {
            try {
                const data = await Service.deleteByID(id);
                setAlertMessage(data.message);
                setAlertVariant('success');
                fetchUsers();
            } catch (error) {
                setAlertMessage('Error deleting user!');
                setAlertVariant('danger');
                console.error('Error deleting user:', error);
            }
        }
    }

    const formatDate = (dateString: string) => {
        const date = new Date(dateString);
        return date.toLocaleString();
    };

    const updateUser = (userId: string) => {
        navigate(`/update/${userId}`);
    };

    return (
        <div className="mt-4 mx-4">
            <h1 className="text-center title">Users</h1>
            <table className="table table-hover mx-auto">
                <thead>
                    <tr className="table-primary">
                        <th scope="col">ID</th>
                        <th scope="col">Full name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Password hash</th>
                        <th scope="col">Registration date</th>
                        <th scope="col">Last modification date</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user) => (
                        <tr className="table-dark" key={user._id.$oid}>
                            <th scope="row">{user._id.$oid.slice(0, 10) + '...'}</th>
                            <td>{user.fullname}</td>
                            <td>{user.email}</td>
                            <td>{user.password.slice(0, 20) + '...'}</td>
                            <td>{formatDate(user.registration.$date)}</td>
                            <td>{user.modification ? formatDate(user.modification.$date) : user.modification}</td>
                            <td>
                                <button
                                    type="button"
                                    className="btn btn-primary btn-sm"
                                    onClick={() => updateUser(user._id.$oid)}
                                >
                                    Update
                                </button>
                                &ensp;
                                <button
                                    type="button"
                                    className="btn btn-danger btn-sm"
                                    onClick={() => deleteUser(user._id.$oid)}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Users;
