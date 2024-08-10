// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

contract SocialNetwork {
    struct Profile {
        string username;
        string bio;
        address owner;
    }

    struct Post {
        uint256 id;
        string content;
        address author;
        uint256 timestamp;
    }

    mapping(address => Profile) public profiles;
    Post[] public posts;
    uint256 public postCount;

    event ProfileCreated(address indexed owner, string username, string bio);
    event PostCreated(uint256 indexed postId, address indexed author, string content, uint256 timestamp);

    modifier onlyProfileOwner() {
        require(profiles[msg.sender].owner == msg.sender, "Not profile owner");
        _;
    }

    function createProfile(string memory _username, string memory _bio) public {
        require(profiles[msg.sender].owner == address(0), "Profile already exists");

        profiles[msg.sender] = Profile({
        username: _username,
        bio: _bio,
        owner: msg.sender
        });

        emit ProfileCreated(msg.sender, _username, _bio);
    }

    function createPost(string memory _content) public onlyProfileOwner {
        postCount++;
        posts.push(Post({
        id: postCount,
        content: _content,
        author: msg.sender,
        timestamp: block.timestamp
        }));

        emit PostCreated(postCount, msg.sender, _content, block.timestamp);
    }

    function getPost(uint256 _postId) public view returns (Post memory) {
        require(_postId > 0 && _postId <= postCount, "Post does not exist");
        return posts[_postId - 1];
    }

    function getProfile(address _user) public view returns (Profile memory) {
        return profiles[_user];
    }
}
