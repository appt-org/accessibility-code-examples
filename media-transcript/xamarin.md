# Transcript - Xamarin

In Xamarin, you can use [`Label`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.label?view=xamarin-forms) to display written text. Make sure to wrap the `Label` widget in a [`ScrollView`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.scrollview?view=xamarin-forms) to enable scrolling.

```xml
<ScrollView>
    <Label x:name="transcript" Text="{Binding ApptTranscript}" />
</ScrollView>
```
