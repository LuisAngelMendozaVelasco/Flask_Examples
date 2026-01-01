import React, { createContext, useContext, useState, type ReactNode } from 'react';

interface AlertContextType {
    alertMessage: string;
    alertVariant: string;
    setAlertMessage: (message: string) => void;
    setAlertVariant: (variant: string) => void;
}

const AlertContext = createContext<AlertContextType | undefined>(undefined);

export const AlertProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [alertMessage, setAlertMessage] = useState<string>('');
    const [alertVariant, setAlertVariant] = useState<string>('success');

    return (
        <AlertContext.Provider value={{ alertMessage, alertVariant, setAlertMessage, setAlertVariant }}>
            {children}
        </AlertContext.Provider>
    );
};

export const useAlert = () => {
    const context = useContext(AlertContext);
    if (!context) {
        throw new Error('useAlert must be used within an AlertProvider');
    }
    return context;
};