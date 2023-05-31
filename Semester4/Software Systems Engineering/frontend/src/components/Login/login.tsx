import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {useNavigate} from "react-router-dom";

export const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPassword(e.target.value);
    };

    const handleFormSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            // Perform API request to authenticate user
            const response = await fetch('https://localhost:7203/api/Auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username: username, password: password }),
            });

            console.log(response.status);
            if (response.ok) {
                const data = await response.json();
                const item = {
                    userid: data.data.id,
                    username: data.data.username,
                    roles: data.data.roles,
                    token: data.token
                };

                const itemString = JSON.stringify(item);
                localStorage.setItem('item', itemString);

                if(data.data.roles === "Admin")
                    window.location.href = '/alldestinations';
                else
                    window.location.href = '/pickpublic';
            } else {
                throw new Error('Login failed');
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <div className="mb-3">
                <label htmlFor="username" className="form-label">
                    Username
                </label>
                <input
                    type="text"
                    className="form-control"
                    id="username"
                    value={username}
                    onChange={handleUsernameChange}
                />
            </div>
            <div className="mb-3">
                <label htmlFor="password" className="form-label">
                    Password
                </label>
                <input
                    type="password"
                    className="form-control"
                    id="password"
                    value={password}
                    onChange={handlePasswordChange}
                />
            </div>
            <button type="submit" className="btn btn-primary">
                Login
            </button>
        </form>
    );
};
