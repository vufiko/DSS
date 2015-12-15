INFO FOR SKINNERS - How to use this addon in your skin:


RunScript(script.image.resource.select,property=Foo&amp;type=Bar)
where 'Property' is the name of the skin setting that needs to be set
and 'Bar' is the type of image resource addon (weatherfanart / moviegenreicons / studios / etc..).

If you run the script like this, it will open a select dialog with all installed image resource addons of the given type.
The first item in the list (none) can be used to remove the current mapping.
The last item in the list (get more..) will allow users to install additional image resource addons.

After selecting one, the script will set the following skin settings:
Foo.name  (string)
Foo.path  (string)
Foo.multi (bool)

You can now use $INFO[Skin.String(Foo.path)] to access the images inside the image resource addon
and $INFO[Skin.String(Foo.name)] to display the name of the selected addon.
Foo.multi will tell you if the resource addon should be used with a multiimage control.


example usage:
- RunScript(script.image.resource.select,property=Foo&studiologos;type=resource.images.studios)
- $INFO[Skin.String(studiologos.name)]
- $INFO[Skin.String(studiologos.path)]
- Skin.HasSetting(studiologos.multi)
