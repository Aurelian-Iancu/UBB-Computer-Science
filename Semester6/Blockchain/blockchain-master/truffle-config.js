module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*",
      gas: 6721975
    }
  },
  compilers: {
    solc: {
      version: "0.5.1"
    }
  }
};
