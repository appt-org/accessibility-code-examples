# Accessibility focus indicator - Xamarin

In Xamarin.Forms, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

The [`Visual State Manager`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/visual-state-manager) (VSM) provides a structured way to make visual changes to the user interface from code. The `VSM` contains a visual state group named `CommonStates` which includes the `Focused` state.

The code sample below shows how to change the background color of a button on focus.

```xml
<Style TargetType="Button">
    <Setter Property="VisualStateManager.VisualStateGroups">
        <VisualStateGroupList>
            <VisualStateGroup x:Name="CommonStates">
                <VisualState x:Name="Normal">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="DefaultColor" />
                    </VisualState.Setters>
                </VisualState>
                <VisualState x:Name="Focused">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="FocusedColor" />
                    </VisualState.Setters>
                </VisualState>
                <VisualState x:Name="Disabled">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="DisabledColor" />
                    </VisualState.Setters>
                </VisualState>
            </VisualStateGroup>
        </VisualStateGroupList>
    </Setter>
</Style>
```
