import Service from '../services/Service';
import { useRef, useEffect } from 'react';
import { useAlert } from '../contexts/AlertContext';
import { useParams } from 'react-router-dom';

const UserForm = ({ isUpdate }: { isUpdate: boolean }) => {
    const fullnameRef = useRef<HTMLInputElement>(null);
    const emailRef = useRef<HTMLInputElement>(null);
    const passwordRef = useRef<HTMLInputElement>(null);
    const { setAlertMessage, setAlertVariant } = useAlert();
    const { userId } = useParams<{ userId: string }>();

    useEffect(() => {
        if (isUpdate && userId) {
            const fetchUser = async () => {
                try {
                    const data = await Service.findByID(userId);
                    if (fullnameRef.current) fullnameRef.current.value = data.fullname;
                    if (emailRef.current) emailRef.current.value = data.email;
                } catch (error) {
                    setAlertMessage('Error fetching user!');
                    setAlertVariant('danger');
                    console.error('Error fetching user:', error);
                }
            };
            fetchUser();
        }
    }, [isUpdate, userId]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const user_data = {
                fullname: fullnameRef.current?.value || '',
                email: emailRef.current?.value || '',
                password: passwordRef.current?.value || ''
            };
            let data;
            if (isUpdate && userId) {
                data = await Service.update(userId, user_data);
            } else {
                data = await Service.create(user_data);
            }
            setAlertMessage(data.message);
            setAlertVariant('success');
            if (fullnameRef.current) fullnameRef.current.value = '';
            if (emailRef.current) emailRef.current.value = '';
            if (passwordRef.current) passwordRef.current.value = '';
        } catch (error) {
            setAlertMessage('Error submitting user!');
            setAlertVariant('danger');
            console.error('Error submitting user:', error);
        }
    };

    return (
        <div className="card mx-auto mt-4 border-light" style={{ maxWidth: '30rem' }}>
            <fieldset className="card-body">
                <legend className="card-title">Contact information</legend>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="fullname" className="form-label mt-4">Full name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="fullname"
                            name="fullname"
                            placeholder="Enter full name"
                            ref={fullnameRef}
                            required
                        />
                    </div>
                    <div>
                        <label htmlFor="email" className="form-label mt-4">Email address</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            name="email"
                            placeholder="Enter email address"
                            ref={emailRef}
                            required
                        />
                    </div>
                    <div>
                        <label htmlFor="password" className="form-label mt-4">Password</label>
                        <input
                            type="password"
                            className="form-control"
                            id="password"
                            name="password"
                            placeholder="Enter password"
                            ref={passwordRef}
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-primary mt-4">
                        {isUpdate ? 'Update' : 'Save'}
                    </button>
                </form>
            </fieldset>
        </div>
    );
};

export default UserForm;
