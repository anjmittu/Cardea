using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using Newtonsoft.Json;

namespace Cardea
{
    class AuthResp
    {
        public string access_token { get; set; }
        public string user_id { get; set; }
    }

	public partial class LoginPage : ContentPage
	{
		public LoginPage()
		{
			InitializeComponent();
            WebView.Source = "https://www.fitbit.com/oauth2/authorize?client_id=22D7B9&response_type=code&scope=activity+heartrate+nutrition+sleep+weight&redirect_uri=cardea://auth";
        }

        void Login(object sender, System.EventArgs e)
        {
            WebView.IsVisible = true;
            LoginForm.IsVisible = false;
        }

        void webOnNavigating(object sender, WebNavigatingEventArgs e)
        {
            LoginButton.IsEnabled = false;
        }

            void webOnEndNavigating(object sender, WebNavigatedEventArgs e)
        {
            LoginButton.IsEnabled = true;
            if (e.Url.StartsWith("cardea://auth"))
            {
                WebView.IsVisible = false;
                LoginForm.IsVisible = true;

                var URL = new Uri(e.Url);
                string code = e.Url.Split(new string[] { "code=" }, System.StringSplitOptions.RemoveEmptyEntries)[1].Split('#')[0];

                Dictionary<string, string> form = new Dictionary<string, string>();
                form["code"] = code;
                form["grant_type"] = "authorization_code";
                form["client_id"] = "22D7B9";
                form["redirect_uri"] = "cardea://auth";

                var content = new FormUrlEncodedContent(form);

                var client = new HttpClient();
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", Convert.ToBase64String(Encoding.ASCII.GetBytes("22D7B9:c501ba0677ae034ac4d64051695b1ffa")));
                var result = client.PostAsync("https://api.fitbit.com/oauth2/token", content).Result;


                string resp = result.Content.ReadAsStringAsync().Result;
                var tokens = JsonConvert.DeserializeObject<AuthResp>(resp);
                App.auth_token = tokens.access_token;
                App.userid = tokens.user_id;

                Navigation.PushModalAsync(new HomePage());
            }
        }
    }
}
