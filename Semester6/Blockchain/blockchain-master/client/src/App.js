import React, { useEffect, useState } from "react";
import web3 from "./web3";
import SocialNetwork from "./SocialNetwork";

function App() {
    const [account, setAccount] = useState("");
    const [profile, setProfile] = useState({});
    const [posts, setPosts] = useState([]);
    const [username, setUsername] = useState("");
    const [bio, setBio] = useState("");
    const [content, setContent] = useState("");

    useEffect(() => {
        async function load() {
            const accounts = await web3.eth.getAccounts();
            setAccount(accounts[1]);

            try {
                const profile = await SocialNetwork.methods.getProfile(accounts[1]).call();
                setProfile(profile);

                const postCount = await SocialNetwork.methods.postCount().call();
                let posts = [];
                for (let i = 1; i <= postCount; i++) {
                    const post = await SocialNetwork.methods.getPost(i).call();
                    posts.push(post);
                }
                setPosts(posts);
            } catch (error) {
                console.error("Error loading profile or posts", error);
            }
        }
        load();
    }, []);

    const createProfile = async () => {
        try {
            await SocialNetwork.methods.createProfile(username, bio).send({
                from: account,
                gas: 500000
            });
        } catch (error) {
            console.error("Error creating profile", error);
        }
    };

    const createPost = async () => {
        try {
            await SocialNetwork.methods.createPost(content).send({
                from: account,
                gas: 500000
            });
            const postCount = await SocialNetwork.methods.postCount().call();
            let posts = [];
            for (let i = 1; i <= postCount; i++) {
                const post = await SocialNetwork.methods.getPost(i).call();
                posts.push(post);
            }
            setPosts(posts);
        } catch (error) {
            console.error("Error creating post", error);
        }
    };

    return (
        <div>
            <h1>Social Network</h1>
            <h2>Account: {account}</h2>
            <h2>Profile</h2>
            <p>Username: {profile.username}</p>
            <p>Bio: {profile.bio}</p>
            <h2>Create Profile</h2>
            <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
            <input value={bio} onChange={e => setBio(e.target.value)} placeholder="Bio" />
            <button onClick={createProfile}>Create Profile</button>
            <h2>Create Post</h2>
            <input value={content} onChange={e => setContent(e.target.value)} placeholder="Content" />
            <button onClick={createPost}>Create Post</button>
            <h2>Posts</h2>
            <ul>
                {posts.map(post => (
                    <li key={post.id}>
                        <p>{post.content}</p>
                        <p>By: {post.author}</p>
                        <p>At: {new Date(Number(post.timestamp) * 1000).toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
