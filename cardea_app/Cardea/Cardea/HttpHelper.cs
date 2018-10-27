using System;
using System.Collections.Generic;
using System.Text;
using System.Net.Http;
using System.Net.Http.Headers;

namespace Cardea
{
    public class HttpHelper
    {
        public static string Get(string url)
        {
            var client = new HttpClient();
            return client.GetAsync(url).Result.Content.ReadAsStringAsync().Result;
        }
    }
}
