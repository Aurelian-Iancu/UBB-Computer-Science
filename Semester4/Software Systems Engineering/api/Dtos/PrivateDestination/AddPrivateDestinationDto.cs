using System.ComponentModel.DataAnnotations;

namespace api.Dtos.PrivateDestination
{
    public record AddPrivateDestinationDto
    {
        [Required]
        public string Geolocation { get; set; } = string.Empty;
        [Required]
        public string Title { get; set; } = string.Empty;
        [Required]
        public string Image { get; set; } = string.Empty;
        [Required]
        public string Description { get; set; } = string.Empty;
        [Required]
        public DateTime StartDate { get; set; }
        [Required]
        public DateTime EndDate { get; set; }
        [Required]
        public Guid UserId { get; set; }
    }
}