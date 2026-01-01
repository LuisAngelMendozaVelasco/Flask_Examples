import UserForm from './UserForm';

function Update() {
    return (
        <div className="mt-4 mx-4">
            <h1 className="text-center title">Update user</h1>
            <UserForm isUpdate={true} />
        </div>
    )
}

export default Update;
