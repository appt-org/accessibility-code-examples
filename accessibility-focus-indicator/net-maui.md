# Accessibility focus indicator - .NET MAUI

In .NET MAUI, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

The [`Visual State Manager`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.controls.visualstatemanager?view=net-maui-8.0) (VSM) provides a structured way to make visual changes to the user interface from code. The `VSM` contains a visual state group named `CommonStates` which includes the `Focused` state.

The code sample below shows how to change the background color of an entry on focus.

```xml
<Style TargetType="Entry">
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
