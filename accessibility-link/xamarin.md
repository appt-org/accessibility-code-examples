# Accessibility link - Xamarin

In Xamarin, you need to follow four steps to create links:

1. Set the `TextColor` and `TextDecoration` properties of the [`Label`](/en-us/dotnet/api/xamarin.forms.label) or [`Span`](/en-us/dotnet/api/xamarin.forms.span).
2. Add a [`TapGestureRecognizer`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer) to the [`GestureRecognizers`](/en-us/dotnet/api/xamarin.forms.gestureelement.gesturerecognizers#xamarin-forms-gestureelement-gesturerecognizers) collection of the [`Label`](/en-us/dotnet/api/xamarin.forms.label) or [`Span`](/en-us/dotnet/api/xamarin.forms.span), whose [`Command`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer.command#xamarin-forms-tapgesturerecognizer-command) property binds to a `ICommand`, and whose [`CommandParameter`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer.commandparameter#xamarin-forms-tapgesturerecognizer-commandparameter) property contains the URL to open.
3. Define the `ICommand` that will be executed by the [`TapGestureRecognizer`](/en-us/dotnet/api/xamarin.forms.tapgesturerecognizer).
4. Write the code that will be executed by the `ICommand`.

For more information, see [Xamarin Hyperlinks](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label#hyperlinks), it includes information how you can create your own [Hyperlink class](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/label#creating-a-reusable-hyperlink-class).

```xml
<Label>
    <Label.FormattedText>
        <FormattedString>
            <Span Text="Read more about " />
            <Span Text="Appt"
                  TextColor="Blue"
                  TextDecorations="Underline">
                <Span.GestureRecognizers>
                    <TapGestureRecognizer Command="{Binding TapCommand}"
                                          CommandParameter="https://appt.org" />
                </Span.GestureRecognizers>
            </Span>
        </FormattedString>
    </Label.FormattedText>
</Label>
```
