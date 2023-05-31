namespace api.Models
{
    public record User 
    {
        public Guid Id { get; set; }
        public string Username { get; set; } = string.Empty;
        public string Password { get; set; } = string.Empty;
        public string Roles { get; set; } = string.Empty;

        // Navigation properties
        public ICollection<PrivateDestination> Destinations { get; set; } = new List<PrivateDestination>();
    }
}