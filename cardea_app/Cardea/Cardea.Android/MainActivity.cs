using System;

using Android.App;
using Android.Content.PM;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;

namespace Cardea.Droid
{
	[Activity (Label = "Cardea", Icon = "@drawable/icon", Theme="@style/MainTheme", MainLauncher = true, ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
    [IntentFilter(new[] { Android.Content.Intent.ActionView },
        DataScheme = "cardea",
        DataHost = "auth",
        Categories = new[] { Android.Content.Intent.CategoryDefault, Android.Content.Intent.CategoryBrowsable },
        AutoVerify=true)]
    public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity
	{
		protected override void OnCreate (Bundle bundle)
		{
			TabLayoutResource = Resource.Layout.Tabbar;
			ToolbarResource = Resource.Layout.Toolbar; 

			base.OnCreate (bundle);

            var data = Intent?.Data?.EncodedAuthority;

            global::Xamarin.Forms.Forms.Init (this, bundle);
			LoadApplication (new Cardea.App ());
		}
	}
}

