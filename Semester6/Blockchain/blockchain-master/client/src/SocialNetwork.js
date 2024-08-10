import web3 from "./web3";
import SocialNetwork from "./build/contracts/SocialNetwork.json";

const instance = new web3.eth.Contract(
    SocialNetwork.abi,
    "0xe93370f4CC2D387A3C4E4dBCad3B30F42A29DF72"
);

export default instance;
