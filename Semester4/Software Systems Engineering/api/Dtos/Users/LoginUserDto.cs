using System.ComponentModel.DataAnnotations;

namespace api.Dtos.User
{
    public record LoginUserDto
    {
        [Required]
        public string Username { get; set; } = string.Empty;
        [Required]
        public string Password { get; set; } = string.Empty;
    }
}