using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace Fitbit_Data_Analysis_App
{
    public partial class LoginPage : ContentPage
    {
        public LoginPage()
        {
            InitializeComponent();
            WebView.Source = "https://www.fitbit.com";
        }

        void Login(object sender, System.EventArgs e)
        {
            WebView.IsVisible = true;
            LoginButton.IsVisible = false;
            LoginLabel.IsVisible = false;
        }

        void webOnEndNavigating(object sender, WebNavigatedEventArgs e)
        {
            
        }
    }
}
