namespace api.Responses
{
    public class LoginResponse<T> : Response<T>
    {

        public LoginResponse(T data, string token) : base(data)
        {
            this.Token = token;
        }

        public string Token { get; set; }
    }
}