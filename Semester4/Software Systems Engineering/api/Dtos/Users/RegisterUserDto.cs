using System.ComponentModel.DataAnnotations;

namespace api.Dtos.User
{
    public record RegisterUserDto
    {
        [Required]
        public string Username { get; set; } = string.Empty;
        [Required]
        public string Password { get; set; } = string.Empty;
        [Required]
        public List<string> Roles { get; set; } = new List<string>();
    }
}