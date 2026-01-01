import UserForm from './UserForm';

function Home() {
    return (
        <div className="mt-4 mx-4">
            <h1 className="text-center title">Create user</h1>
            <UserForm isUpdate={false} />
        </div>
    )
}

export default Home;
