using System.Security.Claims;
using api.Exceptions;

namespace api.Services
{
    public class Permission : IPermission
    {
        private readonly IHttpContextAccessor httpContextAccessor;

        public Permission(IHttpContextAccessor httpContextAccessor)
        {
            this.httpContextAccessor = httpContextAccessor;
        }

        public void Check(Guid id) {
            if (this.httpContextAccessor.HttpContext is not null)
            {
                var jwtId = this.httpContextAccessor.HttpContext.User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
                var roles = this.httpContextAccessor.HttpContext.User
                    .FindAll(ClaimTypes.Role)
                    .Select(c => c.Value)
                    .ToList();

                if (!roles.Contains("Admin"))
                {
                    if (!roles.Contains("Normal") || id.ToString() != jwtId)
                    {
                        throw new ForbiddenException("You don't have permission.");
                    }
                }
            }
        }
    }
}