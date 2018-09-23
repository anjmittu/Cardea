using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Xamarin.Forms;

namespace Cardea
{
	public partial class App : Application
	{
        public static string auth_token;
        public static string userid;

		public App ()
		{
			InitializeComponent();

			MainPage = new Cardea.LoginPage();
		}

		protected override void OnStart ()
		{
			// Handle when your app starts
		}

		protected override void OnSleep ()
		{
			// Handle when your app sleeps
		}

		protected override void OnResume ()
		{
			// Handle when your app resumes
		}
	}
}
