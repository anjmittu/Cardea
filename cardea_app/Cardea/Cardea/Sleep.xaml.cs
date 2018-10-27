using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using System.Threading.Tasks;

namespace Cardea
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class Sleep : ContentPage
	{
		public Sleep ()
		{
			InitializeComponent ();
            Task.Run(() =>
            {
                string sleepstr = HttpHelper.Get("http://35.236.207.9/CardeaSleep?auth_tok=" + App.auth_token + "&userid=" + App.userid);
                Device.BeginInvokeOnMainThread(() =>
                {
                    CardeaSleep.Text = sleepstr;
                });
            });
            
		}
	}
}