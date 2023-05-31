namespace api.Dtos.User
{
    public record UserDto
    {
        public Guid Id { get; set; }
        public string Username { get; set; } = string.Empty;
        public string Roles { get; set; } = string.Empty;
    }
}