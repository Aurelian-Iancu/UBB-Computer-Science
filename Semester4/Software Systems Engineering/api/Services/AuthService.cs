using api.Exceptions;
using api.Models;
using api.Repositories;
using System.Security.Claims;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using System.IdentityModel.Tokens.Jwt;
using api.Responses;
using api.Dtos.User;
using api.Validators;

namespace api.Services
{
    public class AuthService : IAuthService
    {
        private readonly DatabaseContext context;
        private readonly IConfiguration configuration;
        private readonly AuthValidator validator;
            public AuthService(DatabaseContext context, IConfiguration configuration, AuthValidator validator)
        {
            this.context = context;
            this.configuration = configuration;
            this.validator = validator;
        }

        public async Task<DetailedUserDto> GetUserAsync(Guid id)
        {
            var user = await this.context.Users.FindAsync(id);

            if (user is null)
            {
                throw new NotFoundException("User not found.");
            }

            await this.context.Entry(user)
                .Collection(u => u.Destinations)
                .LoadAsync();

            return user.AsDetailedDto();
        }

        public async Task<UserDto> RegisterAsync(RegisterUserDto user)
        {
            if (this.context.Users.Any(u => u.Username == user.Username))
            {
                throw new ValidationException("Username already exists.");
            }

            var newUser = new User() {
                Id = Guid.NewGuid(),
                Username = user.Username,
                Password = user.Password,
                Roles = string.Join(",", user.Roles)
            };

            var result = this.validator.ValidateUser(newUser);
            if (result != string.Empty)
            {
                throw new ValidationException(result);
            }

            string passwordHash = BCrypt.Net.BCrypt.HashPassword(user.Password);
            newUser.Password = passwordHash;

            this.context.Users.Add(newUser);
            await this.context.SaveChangesAsync();

            return newUser.AsDto();
        }
        
        public LoginResponse<UserDto> Login(LoginUserDto user)
        {
            var actualUser = this.context.Users.FirstOrDefault(u => u.Username == user.Username);
            
            if (actualUser is null) 
            {
                throw new NotFoundException("Username or password are incorrect.");
            }

            if (!BCrypt.Net.BCrypt.Verify(user.Password, actualUser.Password))
            {
                throw new NotFoundException("Username or password are incorrect.");
            }

            string token = CreateJwtToken(actualUser);

            var loginResponse = new LoginResponse<UserDto>(actualUser.AsDto(), token);
            
            return loginResponse;
        }

        private string CreateJwtToken(User user) 
        {   
            List<Claim> claims = new List<Claim> {
                new Claim(ClaimTypes.NameIdentifier, user.Id.ToString())
            };

            List<string> roles = user.Roles!.Split(',').ToList();
            roles.ForEach(role => claims.Add(new Claim(ClaimTypes.Role, role)));

            var key = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(this.configuration.GetSection("AppSettings:Key").Value!
            ));

            var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha512Signature);

            var token = new JwtSecurityToken(
                claims: claims,
                expires: DateTime.Now.AddHours(1),
                signingCredentials: creds
            );

            var jwt = new JwtSecurityTokenHandler().WriteToken(token);

            return jwt;
        }
    }
}