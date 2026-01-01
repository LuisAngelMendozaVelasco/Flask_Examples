import { useAlert } from '../contexts/AlertContext';
import Alert from 'react-bootstrap/Alert';

function Alerts() {
    const { alertMessage, alertVariant, setAlertMessage } = useAlert();

    if (!alertMessage) return null;

    const handleClose = () => {setAlertMessage('');};

    return (
        <div className={"mt-4 mx-4"}>
            <Alert key={alertVariant} variant={alertVariant} dismissible onClose={handleClose}>
                {alertMessage}
            </Alert>
        </div>
    );
}

export default Alerts;
